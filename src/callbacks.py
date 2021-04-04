import dash
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
from urllib.parse import urlparse, parse_qs
from stravalib import Client
from appserver import app
import settings
import style
import copy
from dash.exceptions import PreventUpdate


@app.callback(
    output=[
        Output('container-unauthenticated', 'style'),
        Output('container-authenticated', 'style'),
        Output('strava-auth', 'data'),
    ],
    inputs=[
        Input('url', 'search'),
    ],
    state=[
        State('strava-auth', 'data'),
    ]
)
def login_verdict(query_string, strava_auth):
    unauthenticated = style.SHOW
    authenticated = style.HIDE

    if strava_auth is None:
        strava_auth = {}

    if strava_auth.get('authenticated', False):
        unauthenticated = style.HIDE
        authenticated = style.SHOW
    elif query_string is not None:
        query = parse_qs(str(query_string[1:]))
        if 'code' in query:
            client = Client()
            response = client.exchange_code_for_token(
                client_id=settings.STRAVA_CLIENT_ID,
                client_secret=settings.STRAVA_CLIENT_SECRET,
                code=query['code']
            )
            strava_auth.update(response)
            strava_auth['authenticated'] = True
            unauthenticated = style.HIDE
            authenticated = style.SHOW

    return unauthenticated, authenticated, strava_auth


@app.callback(
    output=[
        Output('strava-activity_list', 'data'),
        Output('activity-selector', 'activityList'),
        Output('activity-selector', 'selectedActivity'),
    ],
    inputs=[
        Input('strava-auth', 'data'),
        Input('strava-config','data-year'),
        Input('strava-config','data-activities-limit'),
    ],
)
def get_activity_list(strava_auth, selected_year, activities_limit):
    if not 'access_token' in strava_auth:
        raise PreventUpdate
    client = Client(access_token=strava_auth['access_token'])

    start_date = f"{selected_year}-01-01T00:00:00Z"
    end_date = f"{selected_year+1}-01-01T00:00:00Z"

    activities = client.get_activities(
        after=start_date,  
        before=end_date,  
        limit=activities_limit,
    )
    store_activities = [
        {
            "id": activity.id,
            "name": activity.name,
            "max_heartrate": activity.max_heartrate,
            "has_heartrate": activity.has_heartrate,
            "kudos_count": activity.kudos_count,
            "average_heartrate": activity.average_heartrate,
            "start_date": activity.start_date,
        } for activity in activities]

    return [
        {"activities": store_activities},
        store_activities,
        store_activities[-1] if len(store_activities) > 0 else None
    ]

@app.callback(
    output=[
        Output('profile-picture', 'src'),
        Output('welcome-message', 'children'),
    ],
    inputs=[
        Input('strava-auth', 'data'),
    ]
)
def welcome_user(strava_auth):
    if not 'access_token' in strava_auth:
        raise PreventUpdate
    client = Client(access_token=strava_auth['access_token'])
    athlete = client.get_athlete()

    # print(activity, )
    # print("{0.name} {0.moving_time}".format(activity))
    return [
        athlete.profile,
        f'Welcome, {athlete.firstname} {athlete.lastname}!',
    ]


@app.callback(
    output=[
        Output("graph", "figure"),
        State("strava-activity-data", "data"),
    ],
    inputs=[
        Input("strava-auth", "data"),
        Input("activity-selector", "selectedActivity"),
    ],
    state=[
        State("strava-activity-data", "data"),
    ]
)
def generate_plot(strava_auth, selected_activity, strava_activity_data):
    if strava_auth is None or selected_activity is None:
        raise PreventUpdate
    current = selected_activity
    activity_cache = dash.no_update
    if (not strava_activity_data is None) and (str(current['id']) in strava_activity_data):
        graph_data = strava_activity_data[str(current['id'])]
    else:
        # Activities can have many streams, you can request desired stream types
        types = ['time', 'latlng', 'altitude', 'heartrate', 'temp', 'distance']
        #  Result is a dictionary object.  The dict's key are the stream type.
        client = Client(access_token=strava_auth['access_token'])
        streams = client.get_activity_streams(
            current['id'],
            types=types,
            resolution='medium'
        )
        activity_data = {
            'time': streams['time'].data if 'time' in streams.keys() else [],
            'distance': streams['distance'].data if 'distance' in streams.keys() else [],
            'heartrate': streams['heartrate'].data if 'heartrate' in streams.keys() else [],
        }

        new_data = {} if strava_activity_data is None else copy.deepcopy(
            strava_activity_data)
        new_data[current['id']] = activity_data
        activity_cache = new_data

        graph_data = activity_data
    x = []
    y = []
    if 'heartrate' in graph_data and 'distance' in graph_data:
        x = graph_data['distance']
        y = graph_data['heartrate']

    figure = go.Figure(
        data=[
            go.Scatter(
                x=x,
                y=y,
                customdata=list(zip(
                    [style.format_time(t) for t in graph_data['time']],   # %{customdata[0]}
                    graph_data['distance'],                               # %{customdata[1]}
                )),
                hovertemplate="%{customdata[0]} min<br>"
                "%{customdata[1]:.1f} m<br>"
                "<b>%{y} bpm</b><extra></extra>"
            )
        ]
    )
    return [figure, activity_cache]
