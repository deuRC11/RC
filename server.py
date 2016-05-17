// server 파일
from bottle import route,run,get,post,response,static_file,request
import cv2


#control rccar
@post('/motor')
def control_rccar():
    command=request.forms.get('command')
    print command
    if command == "GO":         forward()
    elif command == "LEFT":    left()
    elif command == "STOP":    stop()
    elif command == "RIGHT":  right()
    elif command == "BACK":    backward()
    return ''

@route('/')
def do_route():
    return static_file("index.html", root=".")

initMotors()
run(host='192.168.10.100', port=8080, debug='true')

