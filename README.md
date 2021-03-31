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

## Develop alongside plugin

```bash
pip install -e ./activity_selector
```
