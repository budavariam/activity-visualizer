# activity-visualizer

Plotly app to visualize activities in Strava deployed to Heroku

See it live on [heroku](https://activity-visualizer.herokuapp.com/)

## Getting started

```bash
cd src
python3 -m venv venv
. ./venv/bin/activate
python3 app.py
```

## Interesting pages

- [Strava connection](https://github.com/AartGoossens/strava-dash-boilerplate)
- [Dash docs](https://plotly.com/python/getting-started/)
- [Strava playground](https://developers.strava.com/playground/#/Activities/getLoggedInAthleteActivities)
- [strarvalib](https://pythonhosted.org/stravalib/)

## Base requirements

- stravalib
- dash
- plotly
- gunicorn

## Develop plugin alongside code

- run `npm start` from activity_selector
- run vscode debug mode for server in a different shell
- sometimes run `npm run sdist:activated` to install new prod version as seen below

```bash
pushd activity_selector
npm run sdist:activated # create prod build 
popd
pushd src
. ./venv/bin/activate
pip install -e ../activity_selector
```
