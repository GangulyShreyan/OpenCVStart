import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('media/input/phone.jpg', 0)
#IMREAD_GRAYSCALE = 0
#IMREAD_COLOR = 1
#IMREAD_UNCHANGED = -1


#displaying image using opencv
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


'''
displaying image using matplotlib

plt.imshow(img, cmap = "gray", interpolation = 'bicubic')
plt.plot([50,100], [80,100], 'c', linewidth = 5)
plt.show()
'''

#saving an image
cv2.imwrite('media/output/grayphone.png', img)

