import cv2
import numpy as np

img1 = cv2.imread('media/input/plot1arithmatic.jpg')
img2 = cv2.imread('media/input/logoarithmatic.jpg')

'''
Image Arithmatic

add = img1 + img2 #add two image on top of each other
add = cv2.add(img1, img2) #add two image in terms of their pixel values
weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0) #add two image on top of each other according to their weights (<img object1>, <weight1>, <img object2>, <weight2>, <gamma value>)

'''


#IMAGE LOGIC

rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV) # (<img object>, <threshold pixel value>, <Converted pixel value>, <..>), if the pixel value is above threshhold value, the pixel value gets converted to the vonverted pixel value

mask_inv = cv2.bitwise_not(mask) #inverted the color

img1_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask = mask)

dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('img2', img2)
cv2.imshow('mask', mask)
cv2.imshow('res', img1)
cv2.imshow('mask_inv', mask_inv)
cv2.imshow('img1_bg', img1_bg)
cv2.imshow('img2_fg', img2_fg)
cv2.imshow('dst', dst)

#cv2.imshow('mask',mask)
cv2.waitKey(0)
cv2.destroyAllWindows