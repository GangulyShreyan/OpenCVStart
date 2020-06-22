import cv2
import numpy as np

cap = cv2.VideoCapture(0) #0 = primary Webcam, we can insert video link in place of it

fourcc = cv2.VideoWriter_fourcc(*'XVID')  #For the saved video codec
out = cv2.VideoWriter('media/output/output.avi', fourcc, 20.0, (640, 480)) #For the saved video codec

while True:
    ret, frame = cap.read() # ret = True/False, Frame= Each FrameInput
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  #any operations we want to perform

    out.write(frame) #Saving video...

    cv2.imshow('name', frame) #show each frame of the video
    cv2.imshow('gray', gray)  #show each frame of the operated video   

    if cv2.waitKey(1) & 0xFF == ord('q'): #if key 'q' is pressed, then exit
        break

cap.release() #Releases Webcam
out.release() #Saves video
cv2.destroyAllWindows()