# adapted from https://nickhuber.ca/blog/python-opencv-camera-websockets

import threading
import time
import cv2

class Camera:
    
    def __init__(self, camIndex):
        self.thread = None
        self.current_frame  = None
        self.is_running: bool = False
        self.camera = cv2.VideoCapture(camIndex)
        if not self.camera.isOpened():
            raise Exception("Could not open video device")
        # self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        # self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    def __del__(self):
        self.camera.release()

    def start(self):
        if self.thread is None:
            self.thread = threading.Thread(target=self._capture)
            self.thread.start()

    def get_frame(self):
        return self.current_frame

    def stop(self):
        self.is_running = False
        self.thread.join()
        self.thread = None
        self.current_frame  = None

    def _capture(self):
        self.is_running = True
        while self.is_running:
            time.sleep(0.04)
            ret, frame = self.camera.read()
            if ret:
                self.current_frame = frame
            else:
                print("Failed to capture frame")

        print("Camera thread stopped")
        self.thread = None
        self.is_running = False
        self.current_frame  = None