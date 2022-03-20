import torch
import torchvision
import cv2
import numpy as np

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5m, yolov5l, yolov5x, custom





cap = cv2.VideoCapture(0) 

while cap.isOpened():
    ret , frame = cap.read()
    result = model(frame)
    cv2.imshow("object detection" , np.squeeze(result.render()))
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()