import math
import cv2
import numpy as np 
from time import time
import mediapipe as mp 
import matplotlib.pyplot as plt


'''
Pose Detection Model using MediaPipe (Google).
Developed by Rafat Khan
Version 1
Description:
Creating preloaded models to call to outside of 'pose_detect.py'.
Since models are intitialized at init, only the media path needs to be called in 'detect_image' or 'detect_vide' functions.

Input: media path
Output: output image and dictionary of locations.
'''


class PoseDetection:
    def __init__(self):
        return None
    
    def detect_image(input_image_path):

        mp_pose = mp.solutions.pose
        pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence = 0.3, model_complexity=2)
        mp_drawing = mp.solutions.drawing_utils

        
        input_image = cv2.imread('videos/sample_img.jpeg')
        results = pose.process(cv2.cvtColor(input_image,cv2.COLOR_BGR2RGB))

        landmark_points = {}

        if results.pose_landmarks:
            for i in range(32):

                landmark_points[i] = {mp_pose.PoseLandmark(i).name: 
                                        {
                                            "x": results.pose_landmarks.landmark[mp_pose.PoseLandmark(i).value].x,
                                            "y": results.pose_landmarks.landmark[mp_pose.PoseLandmark(i).value].y
                                        }
                                        }

        # return output_image, landmark_points
        return landmark_points

test = PoseDetection
input_path = "sample_img.jpeg"
lp = test.detect_image(input_image_path=input_path)

print(lp)