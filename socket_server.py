import eventlet
eventlet.monkey_patch()

from flask import Flask
from flask_socketio import SocketIO, emit
import libs_64.__common as __common

app = Flask(__name__)
socketio = SocketIO(app, async_mode='eventlet', cors_allowed_origins="*", logger=True, engineio_logger=True)

def format_robot_status(status):
    all_IO = {
        "CABINET": {
            "dout": [status[1][10]],  # cabinet digital output
            "din": [status[1][11]],   # cabinet digital input
            "aout": [status[1][12]],  # cabinet analog output
            "ain": [status[1][13]]    # cabinet analog input
        },
        "TOOL": {
            "tio_dout": [status[1][14]],  # tool digital output
            "tio_din": [status[1][15]],   # tool digital input
            "tio_ain": [status[1][16]]    # tool analog input
        },
        "EXTEND": {
            "extio": [status[1][17]],  # external extension IO
            "out": [],
            "in": [], 
        }
    }

    return all_IO

def fetch_robot_status(rc):
    while True:
        try:
            print("Fetching robot status...")
            status = rc.get_robot_status()
            if status:
                formatted_status = format_robot_status(status)
                print(f"Fetched robot status: {formatted_status}")
                socketio.emit('robot_status', {'data': formatted_status})
                print("Emitted robot status")
            else:
                print("No status fetched from the robot.")
        except Exception as e:
            print(f"Error fetching robot status: {e}")
        eventlet.sleep(0.1)

@app.route('/')
def index():
    return "WebSocket server is running."

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

def main():
    import jkrc
    rc = jkrc.RC("192.168.0.127")
    rc.login()
    eventlet.spawn(fetch_robot_status, rc)
    socketio.run(app, host='0.0.0.0', port=5000)
    rc.logout()

if __name__ == '__main__':
    __common.init_env()
    main()