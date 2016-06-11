# huff transform algorithm file
import numpy as np
import cv2

cam = cv2.VideoCapture(0)  # 비디오 캡쳐를 위한 cv2 함수
cam.set(cv2.CAP_PROP_FRAME_WIDTH,320) # 영상의 가로 크기를 320으로 조절한다.
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,240) # 영상의 세로 크기를 240으로 조절한다.

while (True):

    s, img = cam.read()  # 영상의 값을 읽어옴
    
    # 변수가 두개씩인 이유는 허프선을 두개 검출하고 양옆의 선을 토대로 운전하게 하기 위함
    edges = cv2.Canny(img, 50, 200) # canny edge 검출을 위한 cv2 함수
    edges2 = cv2.Canny(img, 50, 200)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180 , 40, None, 70, 10) # canny edge 검출이된 영상에 huff transform 알고리즘을 적용한다.
    lines2 = cv2.HoughLinesP(edges2, 2, np.pi / 90 , 50, None, 70, 15)

    if lines is not None:  # 선이 검출되었을때
""" 영상에서 특정조건을 만족하는 점들을 계속 추출하고 원하는 직선을
     검출 했다면 빨간선으로 출력한다. """
     
        for line in lines[0]: 
            pt1 = (line[0], line[1])
            pt2 = (line[2], line[3])

            cv2.line(img, pt1, pt2, (0, 0, 255), 3, cv2.LINE_AA)
    if lines2 is not None:
        for line2 in lines2[0]:
            pt3 = (line2[0], line2[1])
            pt4 = (line2[2], line2[3])

            cv2.line(img, pt3, pt4, (0, 0, 255), 3, cv2.LINE_AA)

    cv2.imshow('edges', img) # 최종적으로 허프트랜스폼 알고리즘이 적용된 영상을 뿌려준다.
    if cv2.waitKey(10) & 0xff == ord('q'): # 키보드로 부터 키입력을 기다림
     break
 
cam.release() # 메모리 과다 사용방지를 위한 함수 사용
cv2.destroyAllWindows() # 모든 창을 종료함

