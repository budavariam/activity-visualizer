/* eslint no-magic-numbers: 0 */
import React, { Component } from 'react';

import { ActivitySelector } from '../lib';

class App extends Component {

    constructor() {
        super();
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
        this.state = {
            selectedActivity: activities[3],
            selectedYear: new Date().getFullYear(),
            activityList: activities
        };
        this.setProps = this.setProps.bind(this);
    }

    setProps(newProps) {
        this.setState(newProps);
    }

    render() {
        return (
            <div>
                <ActivitySelector
                    setProps={this.setProps}
                    selectedActivity={this.state.selectedActivity}
                    selectedYear={this.state.selectedYear}
                    activityList={this.state.activityList.filter(e => parseInt(e.start_date.slice(0, 4)) === this.state.selectedYear)}
                // {...this.state}
                />
                {this.state.value}
            </div>
        )
    }
}

export default App;
