import zmq
import time
import tqdm
import socket
import os

BUFFER_SIZE = 4096

while True:

    print("Connecting to GEOTIFF over ZMQ...")
    context = zmq.Context()
    subscriber = context.socket(zmq.SUB)
    subscriber.connect("tcp://*:5555")
    subscriber.setsockopt_string(zmq.SUBSCRIBE, '')

    fileBuffer = subscriber.recv(copy=False).buffer()
    subscriber.send("Received!")
    fileName = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'sample.tif')
    fileHandle = open(fileName, "w")
    fileHandle.write(fileBuffer)
    fileHandle.close
    subscriber.close
    context.term
    
    time.sleep(5)
