import socket
import time
import picamera
import numpy 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.8.116',8002))  
camera = picamera.PiCamera()
try:
    camera.start_preview()
    time.sleep(5)
    camera.capture('q.jpg')
    camera.stop_preview()
    f = open('q.jpg','rb')
    data = f.read()
    sock.send(data)
finally:
    f.close()
    sock.close()
