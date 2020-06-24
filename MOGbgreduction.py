import cv2
import numpy as np

'''
removes background considering its static, keeps foreground considering its moving
'''

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    _, frame = cap.read()
    fgmask = fgbg.apply(frame)

    cv2.imshow('original', frame)
    cv2.imshow('fg', fgmask)

    if cv2.waitKey(1) & 0xFF == ord('q'): #if key 'q' is pressed, then exit
        break

cap.release() #Releases Webcam
cv2.destroyAllWindows()