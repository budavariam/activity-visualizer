import dash_core_components as dcc
import dash_html_components as html
from stravalib import Client

import settings
from appserver import app


app.layout = html.Div([
    dcc.Store(id='strava-auth', storage_type='session'),
    dcc.Location(id='url', refresh=False),
    html.H1(children='Strava Dash boilerplate app'),
    html.Div(id='body')
])


client = Client()
strava_authorization_url = client.authorization_url(
    client_id=settings.STRAVA_CLIENT_ID,
    redirect_uri=settings.APP_URL,
    state='strava-dash-app'
)

strava_login_layout = html.Div([
    html.A(
        html.Img(src='static/btn_strava_connectwith_orange.png'),
        'Connect with Strava',
        href=strava_authorization_url
    )
])


app_layout = html.Div([
    html.P(id='app-layout-body')
])
