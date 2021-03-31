/* eslint no-magic-numbers: 0 */
import React, {Component} from 'react';

import { ActivitySelector } from '../lib';

class App extends Component {

    constructor() {
        super();
        this.state = {
            value: ''
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
                    {...this.state}
                />
                {this.state.value}
            </div>
        )
    }
}

export default App;
