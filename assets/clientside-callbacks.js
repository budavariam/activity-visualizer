"use strict";

// const NO_UPDATE = window.dash_clientside.no_update;
// const PREVENT_UPDATE = window.dash_clientside.PreventUpdate;

window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientside: {
        syncSelectedYear: function(newValue) {
            console.log("AAA")
            return [newValue];
        }
    }
});