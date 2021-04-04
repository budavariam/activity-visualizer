/* eslint no-magic-numbers: 0 */
import React, { Component } from 'react';

import { ActivitySelector } from '../lib';

class App extends Component {

    constructor() {
        super();
        this.state = {
            selectedActivity: null,
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
                    selectedYear="2021"
                    activityList={[
                        { id: "0", name: "Warmup Stretch", start_date: "2021-03-14", has_heartrate: false },
                        { id: "1", name: "Run", start_date: "2021-03-14", has_heartrate: true, average_heartrate: 165, max_heartrate: 180 },
                        { id: "2", name: "Yoga", start_date: "2021-03-15", has_heartrate: true, average_heartrate: 60, max_heartrate: 90 },
                        { id: "3", name: "Workout", start_date: "2021-03-15", has_heartrate: true, average_heartrate: 145, max_heartrate: 172 },
                    ]}
                // {...this.state}
                />
                {this.state.value}
            </div>
        )
    }
}

export default App;
