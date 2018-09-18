# -*- coding: utf-8 -*-

import socket
import cv2
server_socket = socket.socket()
server_socket.bind(('192.168.1.104', 8001))
server_socket.listen(1)

connection, addr = server_socket.accept()
try:
    block = connection.recv(4096)
    data = block
    while True:
        block = connection.recv(4096)
        if not block:
            break
        else:      
            data = data + block #
#    print(repr(data))
#    print(len(data))
    
    f = open('img21.jpg','wb')
    f.write(data)
    img = cv2.imread('img21.jpg')
    cv2.imshow('image',img)
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()
finally:
    f.close()
    connection.close()