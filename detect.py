from ultralytics import YOLO
import math
import cv2 as cv
from collections import namedtuple
import os
import torch

Detection = namedtuple('Detection', ['robots', 'ball'])
Robot = namedtuple('Robot', ['id','center_x', 'center_y','orientation'])
Ball = namedtuple('Ball', ['center_x', 'center_y'])

class BallnetPose:
    def __init__(self):
        self.torch = torch.cuda.is_available()
        
        if not self.torch:
            raise NameError("Can't reach GPU.")
    
    def search_path(self, given_path):
        if not os.path.exists(given_path):
            raise NameError("File doesn't exist.")
        
        if os.path.isdir(given_path):
            file_list = os.listdir(given_path)
            
            return [os.path.join(given_path, file) for file in file_list] 
        
        return [given_path]
    
    def detect(self, image_path):
        print("Checking image path...")
        image_list = self.search_path(image_path)
        print("Ok.")
                
        print('Loading model...')
        model = YOLO('./ballnet-pose.pt', task='pose')
        print('Ok.')
        
        print('Detecting...')
        results = model.predict(image_list, iou=0.7, imgsz=640, save=False)
        n_results = len(results)
        print(f'{n_results} detections.')
        
        detections = list()
        
        for n in range(n_results):
            robots = list()
            
            for cls, center, keypoints in zip(results[n].boxes.cls, results[n].boxes.xywh, results[n].boxes.xyxy):
                cls = cls.tolist()
                center = center.tolist()[:2]
                keypoints = keypoints.tolist()
                
                if cls == 3:
                    ball = Ball(center[0], center[1])
                else:                    
                    front = keypoints[:2]
                    back = keypoints[2:]
                                
                    orientation = self.__calc_orientation(front[0], front[1], back[0], back[1])
                    
                    robots.append(Robot(cls, center[0], center[1], orientation))
                    
            detections.append(Detection(robots, ball))
        
        return detections
         

    def __calc_orientation(self, x_front, y_front, x_back, y_back):
        dx = x_back - x_front
        dy = y_back - y_front
        
        orientation_rad = math.atan2(dy, dx)

        orientation_deg = math.degrees(orientation_rad)
        orientation_deg = (orientation_deg + 360) % 360

        return orientation_deg        
        

if __name__ == '__main__':
    detector = BallnetPose()
    path = "imgs"
    locations = detector.detect(path)
    print(locations)