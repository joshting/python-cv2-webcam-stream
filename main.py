import asyncio
import websockets
import cv2
import base64
import http.server
import socketserver
from camera import Camera
from httpserver import HttpServer

camera = Camera()
httpserver = HttpServer()
CLIENTS = set()

async def handler(websocket):
    CLIENTS.add(websocket)
    try:
        await websocket.wait_closed()
    finally:
        CLIENTS.remove(websocket)

async def send(websocket):
    frame = camera.get_frame()
    ret, encoded = cv2.imencode(".png",frame)
    if(ret):
        base64Frame = base64.b64encode(encoded).decode("ascii")
        try:
            await websocket.send(base64Frame)
        except (websockets.ConnectionClosed, AssertionError):
            pass
    else:
        print('failed to encode frame')


async def broadcast():
    while True:
        for websocket in CLIENTS:
            await send(websocket)
        await asyncio.sleep(0.04)

async def main():
    try:
        httpserver.start()
        camera.start()
        async with websockets.serve(handler, "", 8081):
            await broadcast()

    except KeyboardInterrupt:
        httpserver.stop()
        camera.stop()

if __name__ == "__main__":
    asyncio.run(main())




