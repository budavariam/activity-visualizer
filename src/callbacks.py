from urllib.parse import urlparse, parse_qs

import dash
from stravalib import Client

import settings
from layouts import app_layout, strava_login_layout
from appserver import app


@app.callback(
    output=[
        dash.dependencies.Output('body', 'children'),
        dash.dependencies.Output('strava-auth', 'data')
    ],
    inputs=[
        dash.dependencies.Input('url', 'search')
    ],
    state=[
        dash.dependencies.State('strava-auth', 'data')
    ]
)
def display_page(query_string, strava_auth):
    if strava_auth is None:
        strava_auth = {}

    body = strava_login_layout

    if strava_auth.get('authenticated', False):
        body = app_layout
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
            body = app_layout

    return body, strava_auth


@app.callback(
    output=[
        dash.dependencies.Output('app-layout-body', 'children'),
    ],
    inputs=[
        dash.dependencies.Input('strava-auth', 'data')
    ]
)
def app_layout_body(strava_auth):
    client = Client(access_token=strava_auth['access_token'])
    athlete = client.get_athlete()

    for activity in client.get_activities(after = "2010-01-01T00:00:00Z",  limit=25):
        print(activity)
        print("{0.name} {0.moving_time}".format(activity))

    # Activities can have many streams, you can request desired stream types
    types = ['time', 'latlng', 'altitude', 'heartrate', 'temp', ]

    streams = client.get_activity_streams(activity.id, types=types, resolution='medium')

    #  Result is a dictionary object.  The dict's key are the stream type.
    if 'heartrate' in streams.keys():
        print(streams['heartrate'].data)
        # TODO: print as a plot

    return [f'Welcome, {athlete.firstname} {athlete.lastname}']
