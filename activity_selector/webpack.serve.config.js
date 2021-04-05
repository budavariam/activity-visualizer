const config = require('./webpack.config.js');
const path = require('path');

config.entry = {main: './src/demo/index.js'};
config.output = {
    filename: './demo-output.js',
    path: path.resolve(__dirname),
};
if (process.env.NODE_ENV !== 'production') {
    config.mode = 'development';
}
config.externals = undefined; // eslint-disable-line
config.devtool = 'inline-source-map';
module.exports = config;
