
serialConnectionCode: str = """
#pyserial v3.5

import serial
import time

class SerialConn(serial.Serial):
    def __init__(self, port: str, baudRate: int, *args, **kwargs) -> None:
        super(SerialConn, self).__init__(port, baudRate, *args, **kwargs)
        time.sleep(1)
        self.timeout = 1
        
    def write(self, literal: str) -> None:
        try:
            super().write(literal.encode())
            time.sleep(1)
            
        except serial.serialutil.SerialException:
            self.__init__(self.port, self.baudRate)
            self.write(literal.encode())

if __name__ == '__main__':
    conn = SerialConn('COM6', 9600)
    conn.write('9')
    conn.close()
"""

#---------------------------------------------------------------

objectDetectionCode = """
import cv2
import cvlib
import numpy as np

from cvlib.object_detection import draw_bbox

ESC_KEY: int = 27

class SmartWebCam(cv2.VideoCapture):
    def __init__(self, url: str, *args, **kwargs) -> None:
        super(SmartWebCam, self).__init__(url, *args, **kwargs)
        self.mainLoop()
        
        
    def mainLoop(self) -> None:
        try:
            while True:
                frame: np.ndarray = self.read()[1]
                boundBox, label, confidence = cvlib.detect_common_objects(frame, model='yolov4-tiny')
                outputImg: np.ndarray = draw_bbox(frame, boundBox, label, confidence)
            
                cv2.imshow('smart web cam', outputImg)
            
                if cv2.waitKey(1) == ESC_KEY:
                    break
            
            self.release()
            cv2.destroyAllWindows()
            
        except AttributeError:
            print('invalid url')
        
if __name__ == '__main__':
    smartWebCam = SmartWebCam('https://192.168.1.3:8080/video')
    smartWebCam.mainLoop()
"""