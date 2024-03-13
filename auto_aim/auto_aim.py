import torch
import numpy as np
import cv2
import time
import pyautogui
from PIL import ImageGrab
from KBcmd import ReleaseKey, PressKey, K

model = torch.hub.load('ultralytics/yolov5', 'custom', path='./best.pt', force_reload=True)
last_time = time.time()

def shoot():
    PressKey(K)

def stop():
    ReleaseKey(K)

while(True):
    screen = np.array(ImageGrab.grab(bbox=(0,40,800,600)))
    results = model(screen)
    detections = results.pandas().xyxy[0]
    detections = detections[detections['confidence'] >= 0.5]

    for i, detection in detections.iterrows():
        xmin, ymin, xmax, ymax = detection['xmin'], detection['ymin'], detection['xmax'], detection['ymax']
        if detection['name'] == 'person':
            centerX, centerY = (xmin+xmax)/2, (ymin+ymax)/2+40
            print('find')
            pyautogui.moveTo(centerX, centerY,duration=0.1)
            shoot()
        else:
            stop()
            
    print(detections)
    print('Loop took {} second'.format(time.time()-last_time))

    last_time = time.time()
    cv2.imshow('YOLO', cv2.cvtColor(np.squeeze(results.render()), cv2.COLOR_BGR2RGB))

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
