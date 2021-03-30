import dash
import plotly.graph_objects as go
from urllib.parse import urlparse, parse_qs
from stravalib import Client
from appserver import app
import settings
import style
from dash.exceptions import PreventUpdate


@app.callback(
    output=[
        dash.dependencies.Output('container-unauthenticated', 'style'),
        dash.dependencies.Output('container-authenticated', 'style'),
        dash.dependencies.Output('strava-auth', 'data'),
    ],
    inputs=[
        dash.dependencies.Input('url', 'search'),
    ],
    state=[
        dash.dependencies.State('strava-auth', 'data'),
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
        dash.dependencies.Output('profile-picture', 'src'),
        dash.dependencies.Output('welcome-message', 'children'),
        dash.dependencies.Output('strava-activities', 'data'),
        dash.dependencies.Output('strava-selected-activity', 'data'),
    ],
    inputs=[
        dash.dependencies.Input('strava-auth', 'data'),
    ]
)
def welcome_user(strava_auth):
    if strava_auth is None:
        raise PreventUpdate
    client = Client(access_token=strava_auth['access_token'])
    athlete = client.get_athlete()
    activities = client.get_activities(after="2010-01-01T00:00:00Z",  limit=25)
    store_activities = [
        {
            "id": activity.id,
            "name": activity.name,
            "max_heartrate": activity.max_heartrate,
            "kudos_count": activity.kudos_count,
            "average_heartrate": activity.average_heartrate,
            "start_date": activity.start_date,
        } for activity in activities]
    # print(activity, )
    # print("{0.name} {0.moving_time}".format(activity))
    return [
        athlete.profile,
        f'Welcome, {athlete.firstname} {athlete.lastname}',
        {"activities": store_activities},
        {"selected-activity": store_activities[-1]
         } if len(store_activities) > 0 else None
    ]


@app.callback(
    output=dash.dependencies.Output("graph", "figure"),
    inputs=[
        dash.dependencies.Input('strava-auth', 'data'),
        dash.dependencies.Input('strava-selected-activity', 'data'),
    ],
)
def generate_plot(strava_auth, selected_activity):
    if strava_auth is None or selected_activity is None:
        raise PreventUpdate
    current = selected_activity["selected-activity"]
    # Activities can have many streams, you can request desired stream types
    # heartrate, distance, time
    types = ['time', 'latlng', 'altitude', 'heartrate', 'temp', ]
    #  Result is a dictionary object.  The dict's key are the stream type.
    client = Client(access_token=strava_auth['access_token'])
    streams = client.get_activity_streams(
        current['id'],
        types=types,
        resolution='medium'
    )
    x = []
    y = []
    if 'heartrate' in streams.keys() and 'time' in streams.keys():
        print("Heartrate", len(streams['heartrate'].data))
        x = streams['time'].data
        y = streams['heartrate'].data

    figure = go.Figure(
        data=[
            go.Scatter(x=x, y=y)
        ]
    )
    return figure
