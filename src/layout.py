import dash_core_components as dcc
import dash_html_components as html
from stravalib import Client
import style
import settings
from appserver import app

client = Client()
strava_authorization_url = client.authorization_url(
    client_id=settings.STRAVA_CLIENT_ID,
    redirect_uri=settings.APP_URL,
    state='strava-dash-app'
)

app.layout = html.Div([
    html.Link(rel='stylesheet', href='/static/style.css'),
    dcc.Store(id='strava-auth', storage_type='session'),
    dcc.Store(id='strava-activity_list', storage_type='session'),
    dcc.Store(id='strava-activity-data', storage_type='local'),
    dcc.Store(id='strava-selected-activity', storage_type='memory'),
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
            dcc.Graph(id="graph"),
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
        ]
    )
])
