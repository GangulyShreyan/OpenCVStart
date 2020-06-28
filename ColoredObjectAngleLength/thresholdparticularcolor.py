import cv2
import numpy as np
import math

cap  = cv2.VideoCapture(1)

while True:
    _, frame = cap.read()
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resImage = np.shape(frame)
    resScreen = resImage

    cv2.rectangle(frame, (50,50), (200, 200), (0, 0, 255))
    roi = frame[50:200 , 50:200]

    mask = cv2.inRange(frame, (94, 56, 0), (218, 167, 33), None)
    #mask = cv2.inRange(frame, (7, 35, 122), (15, 96, 206), None)
    mask2 = cv2.inRange(frame, (27, 144, 168), (61, 164, 181),  None)


    points = cv2.findNonZero(mask)
    points2 = cv2.findNonZero(mask2)
    
    if (points is not None) and (points2 is not None):

        lent = np.shape(points)
        lent2 = np.shape(points2)

        middlepointcoordinate = points[int(lent[0]/2)]
        middlepointcoordinate2 = points2[int(lent2[0]/2)]

        #np.set_printoptions(threshold=np.inf)

        middlepointcoordinate = (middlepointcoordinate[0][0], middlepointcoordinate[0][1])
        middlepointcoordinate2 = (middlepointcoordinate2[0][0], middlepointcoordinate2[0][1])
        avg = (int((middlepointcoordinate[0] + middlepointcoordinate2[0])/2) , int((middlepointcoordinate[1] + middlepointcoordinate2[1])/2))
        #print(middlepointcoordinate, middlepointcoordinate2)
        angle = math.degrees(np.arctan((middlepointcoordinate2[1] - middlepointcoordinate[1])/(middlepointcoordinate2[0] - middlepointcoordinate[0])))
        distance = math.sqrt((middlepointcoordinate2[0] - middlepointcoordinate[0])**2 + (middlepointcoordinate2[1] - middlepointcoordinate[1])**2)
        #print(type(angle))
        cv2.line(frame, middlepointcoordinate, middlepointcoordinate2, (0,255, 0))
        cv2.putText(frame, "Angle : " + str(angle), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)
        cv2.putText(frame, "Length : " + str(distance), (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)
        #cv2.putText(frame, "Angle : " : str(angle), avg, cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.circle(frame, middlepointcoordinate, 5, (0,0,255), 10)
        cv2.circle(frame, middlepointcoordinate2, 5, (0,0,255), 10)
        #points3 = cv2.bitwise_or(points, points, mask= points2)
        #cv2.imshow('framefiltered', points3)
        
    
    
    '''
    avg = np.mean(points, axis=0)
    pointInScreen = ((resScreen[0] / resImage[0]) * avg[0], (resScreen[1] / resImage[1]) * avg[1] )
    '''
    #frameonly = cv2.bitwise_and(frame, frame, mask = framefiltered)

    cv2.imshow('frame', frame)
    cv2.imshow('frame1', mask)
    cv2.imshow('frame2', mask2)

    #cv2.imshow('frameonly', frameonly)


    if cv2.waitKey(1) & 0xFF == ord('q'): #if key 'q' is pressed, then exit
        cv2.imwrite("saved.jpg", roi)
        break

cap.release()
cv2.destroyAllWindows()