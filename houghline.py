import numpy as np
import cv2

cam = cv2.VideoCapture(0)

while (True):

    s, img = cam.read()

    edges = cv2.Canny(img, 100, 200)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180 , 40, None, 50, 10)

    if lines is not None:
        for line in lines[0]:
            pt1 = (line[0], line[1])
            pt2 = (line[2], line[3])

            cv2.line(img, pt1, pt2, (0, 0, 255), 3)

    cv2.imshow('edges', img)

    if cv2.waitKey(10) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
