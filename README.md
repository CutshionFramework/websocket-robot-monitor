# WebSocket Robot Server

This project is a WebSocket server built using Flask-SocketIO to monitor and fetch the status, signals, and modbus of a robot. The server communicates with a robot controller and provides real-time status updates to connected clients.

## Usage

- **synchronous Operations**: Uses Flask-SocketIO with `eventlet` to handle multiple WebSocket connections.
- **Client-Server Communication**: The client connects  using `asyncio` and `python-socketio`.

## Installation

1. **Install Dependencies**:
    ```sh
    pip install flask-socketio eventlet python-socketio
    ```

## Usage

1. **Start WebSocket Server**:
    ```sh
    python socket_server.py
    ```

2. **Run Client Connection**:
    ```sh
    python client-connect.py
    ```
