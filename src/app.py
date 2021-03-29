import layouts
import callbacks  # layouts needs to be defined before creating callbacks
import routes
import appserver

server = appserver.app.server
if __name__ == "__main__":
    appserver.app.run_server(debug=True)