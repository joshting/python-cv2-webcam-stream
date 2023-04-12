# Streaming Live Video from Webcam to Web Using Python and OpenCV

## Overview
This is to demonstrate a way to broadcast video from a webcam to web clients (browsers) using:

- Python
- OpenCV (opencv-python) - getting frames from camera and apply face detection
- WebSocket
- Http server

## Concepts Covered in the source codes
- Using OpenCV (*cv2*) to read frames from the webcam
- Using OpenCV to process the frames
- Using WebSocket to push the frames to connected clients (browsers)
- Asynchronous tasks using *asyncio*
- Multi-threading using *threading*

## Getting started
This will require you computer having a webcam.  It assumes that the webcam device index to be zero.  Change it in [camera.py](camera.py) if necessary.
Install Python dependencies (Python 3.11 or greater is recommended)
```
pip install -r requirements.txt
```
Run [main.py](main.py):
```
python main.py
```
Open a browser and navigate to [localhost:8080](localhost:8080).  This works for multiple clients.  Hence, you may open multiple browser windows/tabs to test.

## Disclaimer
There are numerous ways to do this and the way used here might not be the best.  This is experimental, learn as you code and no way near to anything for production. Therefore, there is no guarantee in terms of performance and security.  Suggestions to a better way or how it can be improved are welcomed.

## Testing output of face detection
The metadata for the face detections comes in the same payload as the frames.  To test, use the [https://github.com/joshting/golang-react-video-wall](https://github.com/joshting/golang-react-video-wall)

## Resources
1. [https://websockets.readthedocs.io/en/stable/topics/broadcast.html](https://websockets.readthedocs.io/en/stable/topics/broadcast.html)
2. [https://nickhuber.ca/blog/python-opencv-camera-websockets](https://nickhuber.ca/blog/python-opencv-camera-websockets)