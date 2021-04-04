import React from 'react';
import PropTypes from 'prop-types';
import "./ActivitySelector.style.css"

/**
 * ExampleComponent is an example component.
 * It takes a property, `label`, and
 * displays it.
 * It renders an input with the property `value`
 * which is editable by the user.
 */
const ActivitySelector = (props) => {
    const {
        id,
        selectedActivity,
        selectedYear,
        activityList,
        setProps,
    } = props;

    /*
        * Send the new value to the parent component.
        * setProps is a prop that is automatically supplied
        * by dash's front-end ("dash-renderer").
        * In a Dash app, this will update the component's
        * props and send the data back to the Python Dash
        * app server if a callback uses the modified prop as
        * Input or State.
        */
    // e => setProps({ value: e.target.value })
    return (
        <div id={id} className="activity-selector-root" onClick={(e) => {
            // console.log(e, e.target.getAttribute("data-value"))
            const newActivityId = e.target.getAttribute("data-value")
            const newActivity = activityList.filter(e => ("" + e.id) === newActivityId)[0]
            if (newActivityId && newActivity) {
                setProps({ selectedActivity: newActivity })
                console.debug("Selected", newActivityId, newActivity)
            } else {
                console.warn("Can not read activity id", newActivityId)
            }
        }}>
            <div className="yearSelector">
                <button
                    className="prev"
                    onClick={() => setProps((prevProps) => ({ selectedYear: prevProps.selectedYear - 1 }))}
                >
                    {selectedYear - 1}
                </button>
                <span>{selectedYear}</span>
                <button
                    className="next"
                    onClick={() => setProps((prevProps) => ({ selectedYear: prevProps.selectedYear + 1 }))}
                >
                    {selectedYear + 1}
                </button>
            </div>
            <div className="activity-selector">
                {activityList.map((activity) => {
                    console.debug("selectedActivity", selectedActivity, activity.id)
                    return <div className={`activity-item ${selectedActivity && selectedActivity.id === activity.id ? "selected" : ""}`} key={activity.id} data-value={activity.id}>
                        {activity.start_date}&nbsp;
                    {activity.has_heartrate ? activity.average_heartrate + "bpm" : ""}&nbsp;
                    {activity.name}
                    </div>
                })}
            </div>
        </div>
    );
}

export default ActivitySelector

ActivitySelector.defaultProps = {};

ActivitySelector.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * List of loaded activities
     */
    activityList: PropTypes.arrayOf(PropTypes.object).isRequired,

    /**
     * Data of the selected activity
     */
    selectedActivity: PropTypes.object,

    /**
     * Activities are shown from the current selected year
     */
    selectedYear: PropTypes.string.isRequired,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};
