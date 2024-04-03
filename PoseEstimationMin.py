import cv2 
import mediapipe as mp
import time
import numpy as np

def calculate_angle(a,b,c):
    a = np.array(a) # First
    b = np.array(b) # Mid
    c = np.array(c) # End
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    
    if angle >180.0:
        angle = 360-angle
        
    return angle 

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture('./media/rosca_direta.mp4')
#Getting resolution
frame_width = int(cap.get(3))
frame_height = int(0.9*cap.get(4)) 

#cap = cv2.VideoCapture(0) #0 or 1 is for WEBCAM this is HW dependant
previousTime = 0
currentTime = 0

angle_min=180
angle_max=0

while cap.isOpened():
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)

    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        landmarks = results.pose_landmarks.landmark       
        
        # Get coordinates
        shoulder = [landmarks[mpPose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mpPose.PoseLandmark.LEFT_SHOULDER.value].y]
        elbow = [landmarks[mpPose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mpPose.PoseLandmark.LEFT_ELBOW.value].y]
        wrist = [landmarks[mpPose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mpPose.PoseLandmark.LEFT_WRIST.value].y]

        # Calculate angle
        angle = calculate_angle(shoulder, elbow, wrist)
        if angle >  angle_max:
            angle_max = angle
        if angle < angle_min:
            angle_min = angle

        # Visualize angle
        cv2.putText(img, "Angle: " + str(round(angle,1)), (10,frame_height), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(img, "Angle Min: " + str(round(angle_min,1)), (10,frame_height+20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(img, "Angle Max: " + str(round(angle_max,1)), (10,frame_height+40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

    currentTime = time.time()
    fps = 1/(currentTime - previousTime)
    previousTime = currentTime

    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)