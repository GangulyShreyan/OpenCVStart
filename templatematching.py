import numpy as np
import cv2

img_bgr = cv2.imread('media/input/template.jpg')
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

template = cv2.imread('media/input/templateto.jpg', 0)
w, h = template.shape[::-1]  #just to get the shape of he image

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED) #slides for the template in the main image, and returns the probabilty
#print(res)
threshold = 0.74
loc = np.where(res >= threshold) #returns address of the pixels where the probability is greater than the threshold
#print(loc)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_bgr, pt, (pt[0]+w, pt[1] + h), (0, 255, 255), 2) #draws reactangle around the object

cv2.imshow('detected', img_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()