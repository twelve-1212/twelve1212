# -*- coding: utf-8 -*-

import socket
import cv2
server_socket = socket.socket()
server_socket.bind(('192.168.8.116', 8002))
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
    
    f = open('aa.jpg','wb')
    f.write(data)
    img = cv2.imread('aa.jpg')
    cv2.imshow('image',img)
    cv2.waitKey(0)
finally:
    f.close()
    connection.close()