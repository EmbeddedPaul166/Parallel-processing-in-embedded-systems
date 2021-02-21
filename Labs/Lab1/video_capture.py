import time
import numpy as np
import cv2

# Camera indexes range from 0 to 5
CAMERA_INDEX = 0
GSTREAMER_PIPELINE_STRING = "v4l2src device=/dev/video" + str(CAMERA_INDEX) + " ! video/x-raw,format=UYVY,width=1920, height=1080, framerate=30/1 ! nvvidconv ! video/x-raw(memory:NVMM), format=I420 ! nvvidconv ! video/x-raw,format=(string)BGRx ! videoconvert ! video/x-raw,format=(string)BGR ! appsink sync=0"

def prepare_display_window():
    window = None
    cv2.namedWindow(window, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window, 1280, 720)
    cv2.moveWindow(window, 0, 0)
    cv2.setWindowTitle(window, "Video capture")
    return window

def capture_video():
    video_capture = cv2.VideoCapture(GSTREAMER_PIPELINE_STRING, cv2.CAP_GSTREAMER)
    window = prepare_display_window()
    
    fps = 0
    frame_counter = 0
    start = time.time()
    
    while(1): 
        #Read camera frame
        status, frame = video_capture.read()
        
        if (not status):
            print("Failed to read camera frame")
            break;
         
        #Display frame
        cv2.imshow(window, frame)
         
        frame_counter += 1
        
        print("FPS: ", fps)
        
        # If q is pressed, exit app
        key = cv2.waitKey(1)
        if key == ord("q"):
            break
        
        #Update FPS
        end = time.time()
        if (end - start) >= 1:
            fps = frame_counter
            frame_counter = 0
            start = end
        
    video_capture.release()

if __name__ == "__main__":
    capture_video()
