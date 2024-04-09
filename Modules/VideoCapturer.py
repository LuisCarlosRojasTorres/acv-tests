import cv2 
import mediapipe as mp
import time
import numpy as np

class VideoCapturer:
    capture = None
    frame_width = 0
    frame_height = 0
    
    def __init__(self,videoSource):
        self.capture=cv2.VideoCapture(videoSource)
        self.frame_width = int(self.capture.get(3))
        self.frame_height = int(self.capture.get(4)) 

    def getCapture(self):
        return self.capture

    def getWidth(self):
        return self.frame_width
    
    def getHeight(self):
        return self.frame_height
    
    def ReadCapture(self):
        return self.capture.read()
    
mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

videoSource = './media/rosca_direta.mp4'
vcap = VideoCapturer(videoSource)

##cap = cv2.VideoCapture(videoSource)
#cap = cv2.VideoCapture(0) #0 or 1 is for WEBCAM this is HW dependant
#Getting resolution

##frame_width = int(cap.get(3))
##frame_height = int(cap.get(4)) 

frame_width = vcap.frame_width
frame_height = vcap.frame_width 

previousTime = 0
currentTime = 0

while True:
    success, frame = vcap.ReadCapture()
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(frameRGB)
    
    if results.pose_landmarks:
        mpDraw.draw_landmarks(frame, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        landmarks = results.pose_landmarks.landmark       
                
    currentTime = time.time()
    fps = 1/(currentTime - previousTime)
    previousTime = currentTime

    cv2.putText(frame, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

    cv2.imshow("Image", frame)
    cv2.waitKey(1)



    
#class Landmarker:

    

