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
            "dout": [],  # cabinet digital output
            "din": [],   # cabinet digital input
            "aout": [],  # cabinet analog output
            "ain": []    # cabinet analog input
        },
        "TOOL": {
            "tio_dout": [],  # tool digital output
            "tio_din": [],   # tool digital input
            "tio_ain": []    # tool analog input
        },
        "EXTEND": {
            "extio": [],  # external extension IO
            "out": [],
            "in": [], 
        }
    }

    all_IO["CABINET"]["dout"].append(status[1][10])
    all_IO["CABINET"]["din"].append(status[1][11])
    all_IO["CABINET"]["aout"].append(status[1][12])
    all_IO["CABINET"]["ain"].append(status[1][13])
    all_IO["TOOL"]["tio_dout"].append(status[1][14])
    all_IO["TOOL"]["tio_din"].append(status[1][15])
    all_IO["TOOL"]["tio_ain"].append(status[1][16])
    all_IO["EXTEND"]["extio"].append(status[1][17])

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
        eventlet.sleep(1)

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
    rc = jkrc.RC("192.168.0.140")
    rc.login()
    eventlet.spawn(fetch_robot_status, rc)
    socketio.run(app, host='0.0.0.0', port=5000)
    rc.logout()

if __name__ == '__main__':
    __common.init_env()
    main()