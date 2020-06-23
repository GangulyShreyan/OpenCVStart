'''

To remove white noise or noise in general

'''

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

    kernal = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(mask, kernal, iterations = 1) #creates a block which moves around the binary image, if one pixel in that block is white, it turns into black
    dilation = cv2.dilate(mask, kernal, iterations = 1)

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal) #removes false posiive in the background
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal) #removes false negative within the target object
    
    #tophat can be used fir the difference between input image and the opening of the image
    #blackhat can be used for the difference between the input image and the closign of the image
    
    
    cv2.imshow('frame', frame) 
    cv2.imshow('res', res)
    cv2.imshow('mask', mask)
    cv2.imshow('erode', erosion)
    cv2.imshow('dilate', dilation)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)

  

    if cv2.waitKey(1) & 0xFF == ord('q'): #if key 'q' is pressed, then exit
        break

cv2.destroyAllWindows()
cv2.release()



