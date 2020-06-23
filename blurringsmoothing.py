import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #hsv hue sat value
    lower_green = np.array([70, 30 , 30])
    upper_green = np.array([180, 180, 180])

    mask = cv2.inRange(hsv, lower_green, upper_green) #if the pixel value is within lower_green and upper_green, it returns 1, otherwise no.
    res = cv2.bitwise_and(frame, frame, mask = mask) #if the pixel's mask value is 1, the pixel gets its color from 'frame', otherwise it gets black color

    kernal = np.ones((15, 15), np.float32)/255 #Set filter size 
    smoothed = cv2.filter2D(res, -1, kernal)

    blur = cv2.GaussianBlur (res, (15, 15), 0)
    median = cv2.medianBlur(res, 15)
    bilateral = cv2.bilateralFilter(res, 15, 75, 75)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    cv2.imshow('smoothed', smoothed)
    cv2.imshow('blur', blur)
    cv2.imshow('median', median)
    cv2.imshow('bilateral', bilateral)
  

    if cv2.waitKey(1) & 0xFF == ord('q'): #if key 'q' is pressed, then exit
        break

cv2.destroyAllWindows()
cv2.release()
