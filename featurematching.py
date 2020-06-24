import cv2 
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('media/input/featurematching2.jpg', 0)
img2 = cv2.imread('media/input/featurematching1.jpg', 0)

orb = cv2.ORB_create() #defining detector of similarity

kp1, des1 = orb.detectAndCompute(img1, None) #finding key points and descriptor
kp2, des2 = orb.detectAndCompute(img2, None) #finding key points and descriptor

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True) #BruteForce Matching

matches = bf.match(des1, des2)

matches = sorted(matches, key = lambda x:x.distance) 

img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags = 2)

plt.imshow(img3)
plt.show()