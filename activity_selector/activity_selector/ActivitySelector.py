# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ActivitySelector(Component):
    """An ActivitySelector component.
ActivitySelector lets the user select 
the activity from the list of activities given.
Has the option to change the year, 
that triggers the list to change 
out of the scope of this component.

Keyword arguments:
- id (string; optional): The ID used to identify this component in Dash callbacks.
- activityList (list of dicts; required): List of loaded activities
- selectedActivity (dict; optional): Data of the selected activity
- selectedYear (number; required): Activities are shown from the current selected year
- debugMode (boolean; default False): Activities are shown from the current selected year"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, activityList=Component.REQUIRED, selectedActivity=Component.UNDEFINED, selectedYear=Component.REQUIRED, debugMode=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'activityList', 'selectedActivity', 'selectedYear', 'debugMode']
        self._type = 'ActivitySelector'
        self._namespace = 'activity_selector'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'activityList', 'selectedActivity', 'selectedYear', 'debugMode']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['activityList', 'selectedYear']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(ActivitySelector, self).__init__(**args)
