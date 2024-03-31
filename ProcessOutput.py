import cv2 
import mediapipe as mp
import time

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

pathMedia='./media/'
inputFileName='biceps_errado.mp4'

cap = cv2.VideoCapture(pathMedia+inputFileName)

#Getting resolution
frame_width = int(cap.get(3))
frame_height = int(cap.get(4)) 
size = (frame_width, frame_height) 

print(' - Width: ' + str(frame_width))
print(' - Height: ' + str(frame_height))
#cap = cv2.VideoCapture(0) #0 or 1 is for WEBCAM this is HW dependant

outputVideo = cv2.VideoWriter('./outputMedia/AR_'+inputFileName, cv2.VideoWriter_fourcc(*'MP4V'), 20.0, size)

previousTime = 0
currentTime = 0

while True:
    ret, frame = cap.read()

    if ret:
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(frameRGB)

        if results.pose_landmarks:
            mpDraw.draw_landmarks(frame, results.pose_landmarks, mpPose.POSE_CONNECTIONS)

        currentTime = time.time()
        fps = 1/(currentTime - previousTime)
        previousTime = currentTime

        cv2.putText(frame, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
        outputVideo.write(frame)
        cv2.imshow("Image", frame)        
        cv2.waitKey(1)
    else:
        break

cap.release()
outputVideo.release()
cv2.destroyAllWindows()