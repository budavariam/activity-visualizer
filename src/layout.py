import dash_core_components as dcc
import dash_html_components as html
import activity_selector
from stravalib import Client
import style
import settings
from appserver import app
import datetime
now = datetime.datetime.now()


client = Client()
strava_authorization_url = client.authorization_url(
    client_id=settings.STRAVA_CLIENT_ID,
    redirect_uri=settings.APP_URL,
    state='strava-dash-app'
)

app.layout = html.Div(
    className="container",
    children=[
    html.Link(rel='stylesheet', href='/static/style.css'),
    dcc.Store(id='strava-auth', storage_type='session'),
    dcc.Store(id='strava-activity_list', storage_type='session'),
    dcc.Store(id='strava-activity-data', storage_type='local'),
    html.Div(id='strava-config', **{
        "data-debug-mode": False,
        "data-year": 2021,
        "data-activities-limit": 500,
    }),
    dcc.Location(id='url', refresh=False),
    html.H1(children='Strava Activity Visualizer'),
    html.Div(
        id="container-unauthenticated",
        style=style.SHOW,
        children=[
            html.A(
                html.Img(src='static/btn_strava_connectwith_orange.png'),
                'Connect with Strava',
                href=strava_authorization_url,
            ),
        ]
    ),
    html.Div(
        id="container-authenticated",
        style=style.HIDE,
        children=[
            html.Div(
                className="profile",
                children=[
                    html.Img(
                        id='profile-picture',
                        src='static/blank_profile.jpg',
                    ),
                    html.Span(
                        id='welcome-message',
                    ),
                ]
            ),
            activity_selector.ActivitySelector(
                id="activity-selector",
                selectedActivity=None,
                selectedYear=now.year,
                activityList=[],
            ),
            dcc.Graph(id="graph"),
        ]
    )
])
