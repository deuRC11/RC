import numpy as np
import cv2

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,320)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,240)

while (True):

    s, img = cam.read()

    edges = cv2.Canny(img, 50, 200)
    edges2 = cv2.Canny(img, 50, 200)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180 , 40, None, 70, 10)
    lines2 = cv2.HoughLinesP(edges2, 2, np.pi / 90 , 50, None, 70, 15)

    if lines is not None:
        for line in lines[0]:
            pt1 = (line[0], line[1])
            pt2 = (line[2], line[3])

            cv2.line(img, pt1, pt2, (0, 0, 255), 3, cv2.LINE_AA)
    if lines2 is not None:
        for line2 in lines2[0]:
            pt3 = (line2[0], line2[1])
            pt4 = (line2[2], line2[3])

            cv2.line(img, pt3, pt4, (0, 0, 255), 3, cv2.LINE_AA)

    cv2.imshow('edges', img)
    if cv2.waitKey(10) & 0xff == ord('q'):
     break
 
cam.release()
cv2.destroyAllWindows()

