/* eslint no-magic-numbers: 0 */
import React, { Component } from 'react';
import "./App.css";

import { ActivitySelector } from '../lib';

const activities = [
    { id: "0", name: "Warmup Stretch", start_date: "2020-03-14", has_heartrate: false },
    { id: "1", name: "Run", start_date: "2020-03-14", has_heartrate: true, average_heartrate: 165, max_heartrate: 180 },
    { id: "2", name: "Yoga", start_date: "2021-03-15", has_heartrate: true, average_heartrate: 60, max_heartrate: 90 },
    { id: "3", name: "Workout", start_date: "2021-03-15", has_heartrate: true, average_heartrate: 145, max_heartrate: 172 },
    { id: "4", name: "Workout", start_date: "2021-03-15", has_heartrate: true, average_heartrate: 145, max_heartrate: 172 },
    { id: "5", name: "Workout", start_date: "2021-03-15", has_heartrate: true, average_heartrate: 145, max_heartrate: 172 },
    { id: "6", name: "Workout", start_date: "2019-03-15", has_heartrate: true, average_heartrate: 145, max_heartrate: 172 },
    { id: "7", name: "Workout", start_date: "2019-03-15", has_heartrate: true, average_heartrate: 145, max_heartrate: 172 },
    { id: "8", name: "Workout", start_date: "2019-03-15", has_heartrate: true, average_heartrate: 145, max_heartrate: 172 },
    { id: "9", name: "Workout", start_date: "2019-03-15", has_heartrate: true, average_heartrate: 145, max_heartrate: 172 },
    { id: "10", name: "Workout", start_date: "2019-03-15", has_heartrate: true, average_heartrate: 145, max_heartrate: 172 },
    { id: "11", name: "Workout", start_date: "2019-03-15", has_heartrate: true, average_heartrate: 145, max_heartrate: 172 },
    { id: "12", name: "Workout", start_date: "2019-03-15", has_heartrate: true, average_heartrate: 145, max_heartrate: 172 },
    { id: "13", name: "Workout", start_date: "2019-03-15", has_heartrate: true, average_heartrate: 145, max_heartrate: 172 },
    { id: "14", name: "Workout", start_date: "2019-03-15", has_heartrate: true, average_heartrate: 145, max_heartrate: 172 },
]
class App extends Component {

    constructor() {
        super();
        const defaultYear = 2021
        const filteredActivities = activities.filter(e => parseInt(e.start_date.slice(0, 4)) === defaultYear)
        this.state = {
            selectedActivity: filteredActivities[0],
            selectedYear: defaultYear,
            activityList: filteredActivities
        };
        this.setProps = this.setProps.bind(this);
    }

    setProps(newProps) {
        if (newProps.selectedYear) {
            // simulate side effects out of scope of this component
            const filteredActivities = activities.filter(e => parseInt(e.start_date.slice(0, 4)) === newProps.selectedYear)
            this.setState({...newProps, activityList: filteredActivities});
        } else {
            this.setState(newProps);
        }
    }

    render() {
        return (
            <div className="app">
                <ActivitySelector
                    setProps={this.setProps}
                    selectedActivity={this.state.selectedActivity}
                    selectedYear={this.state.selectedYear}
                    activityList={this.state.activityList}
                />
                <pre className="showState">
{`Selected Year: ${this.state.selectedYear}
Selected Activity: ${JSON.stringify(this.state.selectedActivity, null, 2)}
Activity list: ${JSON.stringify(this.state.activityList, null, 2)}
                    `}
                </pre>
            </div>
        )
    }
}

export default App;
