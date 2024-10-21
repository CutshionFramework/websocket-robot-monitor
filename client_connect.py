import asyncio
import socketio

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print('Connection established')

@sio.event
async def disconnect():
    print('Disconnected from server')

@sio.event
async def robot_status(data):
    print(f"Received robot status: {data}")

async def listen():
    url = "http://localhost:5000"  # Change this to your server's IP if needed
    try:
        await sio.connect(url)
        print("Connected to server, waiting for messages...")  
        await sio.wait()
    except Exception as e:
        print(f"An error occurred: {e}")

asyncio.run(listen())