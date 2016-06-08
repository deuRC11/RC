'''
test print line
'''

#!/usr/bin/env python

import cv2
import sys
import numpy as np
import math

if __name__ == '__main__':
    try:
        fn = sys.argv[1]
    except:
        fn = 0

    def nothing(*arg):
        pass

    cam = cv2.VideoCapture(0)

    while True:
        flag, img = cam.read()
        dst = cv2.Canny(img, 50, 200)
        cdst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)
        if True: # HoughLinesP
          lines = cv2.HoughLinesP(dst, 1, math.pi/180.0, 40, np.array([]), 50, 10)
                    a,b,c = lines.shape
          for i in range(a):
            cv2.line(cdst, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (0, $
        else:    # HoughLines
          lines = cv2.HoughLines(dst, 1, math.pi/180.0, 50, np.array([]), 0, 0)
          a,b,c = lines.shape
          for i in range(a):
                  rho = lines[i][0][0]
                  theta = lines[i][0][1]
                  a = math.cos(theta)
                  b = math.sin(theta)
                  x0, y0 = a*rho, b*rho
                  pt1 = ( int(x0+1000*(-b)), int(y0+1000*(a)) )
                  pt2 = ( int(x0-1000*(-b)), int(y0-1000*(a)) )
                  cv2.line(cdst, pt1, pt2, (0, 0, 255), 3, cv2.LINE_AA)

        cv2.imshow('edge', cdst)

        ch = cv2.waitKey(5) & 0xFF
        if ch == 27:
            break

