import numpy as np
import cv2

img = cv2.imread('media/input/phone.jpg', 1)

px = img[55,55] #reads the BGR value of a particluar pixel
img[55, 55] = [255,255,255] #assigns custom value to that pixel
print(px)

roi = img[100:150, 100:150]  #reads the BGR values of a block of pixels, [startingX:EndingX, StaringY:EndingY]
img[100:150, 100:150] = [255, 255, 255] #assigns a particular custom BGR value to that block of pixels


phone_face = img[37:111, 107:194] #reads the BGR values of a block of pixels, [startingX:EndingX, StaringY:EndingY]
img[0:74, 0:87] = phone_face #assigns a block of BGR value to the previous block of pixels


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows