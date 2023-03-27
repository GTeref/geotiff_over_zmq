import zmq
import time
import os
import sys

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://0.0.0.0:135")
socket.setsockopt(zmq.SUBSCRIBE, '')
path = 'C:\Personal Projects\geotiff_over_zmq\sample_folder'

while True:
    message = socket.recv()
    print("Received request: %s" % message)
    time.sleep(1)
    socket.send(b"World")