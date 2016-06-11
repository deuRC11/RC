# web server
from bottle import route,run,get,post,response,static_file,request
import cv2

@post('/motor') 
def control_rccar(): # rc카를 제어하기 위한 함수
    command=request.forms.get('command') # 커맨드값을 받아서 커맨드변수에 입력
    print command 
    # 커맨드 입력에 따라 상하좌우정지 제어를 할수 있다.
    if command == "GO":         forward()
    elif command == "LEFT":    left()
    elif command == "STOP":    stop()
    elif command == "RIGHT":  right()
    elif command == "BACK":    backward()
    return ''

@route('/')
def do_route():
    return static_file("index.html", root=".") # index html 파일에 리턴시킨다.

initMotors() # motor.py의 gpio기본 셋업 함수가 담겨있는 initmotors를 실행함
run(host='192.168.0.21', port=8080, debug='true') 
# 웹서버 호스트 주소와 포트를 설정함 사용자에 따라 변경되어야 한다.
# debug 옵션은 웹서버 테스트를 위해 켜두었음
