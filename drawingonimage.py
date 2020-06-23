import numpy as np
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('media/input/me.jpg', 1)

cv2.line(img, (0,0), (150, 150), (255, 0, 0), 15)  # (<opencv object>, <starting index>, <ending index>, <color of line>, <line width>)
cv2.rectangle(img, (530,280), (890, 700), (255, 0, 0), 5) # (<opencv object>, <top coordinate index>, <bottom coordinate index>, <color of line>, <line width>)
cv2.circle(img, (710, 490), 180, (0,0,255), 0)   # (<opencv object>, <center coordinate index>, <radius>, <color of line>, <line width>)

pts = np.array([[10, 5], [200, 300], [700, 200], [500, 100]], np.int32)
cv2.polylines(img, [pts], True, (0,0,0), 1) # (<opencv object>, <vertex coordinate index>, <closed or not>, <color of line>, <line width>)

font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, 'Shreyan Ganguly', (530,130), font, 1, (200, 255,255), 2, cv2.LINE_AA)  # (<opencv object>, <Text>, <Starting coordinate>, <font>, <size>, <color>, <letterspacing>, <AntiAliasing>)


cv2.imshow('media/output/imagewithline', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('media/output/imagewithdrawing.png', img)


'''

Same approach can be applied on video.

'''