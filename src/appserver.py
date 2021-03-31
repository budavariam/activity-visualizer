import dash

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
external_stylesheets = []


app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    requests_pathname_prefix='/',
    assets_folder="../assets",
    serve_locally=True,
)

app.title = 'Strava Activity Visualizer'
app.config.suppress_callback_exceptions = False
