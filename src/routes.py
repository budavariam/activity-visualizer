from flask import send_from_directory

from appserver import app


@app.server.route('/static/<path>')
def serve_static(path):
    return send_from_directory('assets', path)