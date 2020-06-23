import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #hsv hue sat value
    lower_green = np.array([00, 0 , 100])
    upper_green = np.array([150, 120, 120])

    mask = cv2.inRange(hsv, lower_green, upper_green) #if the pixel value is within lower_green and upper_green, it returns 1, otherwise no.
    res = cv2.bitwise_and(frame, frame, mask = mask) #if the pixel's mask value is 1, the pixel gets its color from 'frame', otherwise it gets black color
    

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
  

    if cv2.waitKey(1) & 0xFF == ord('q'): #if key 'q' is pressed, then exit
        break

cv2.destroyAllWindows()
cv2.release()
