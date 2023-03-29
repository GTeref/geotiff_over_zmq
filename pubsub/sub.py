import zmq
import time
import tqdm
import socket
import os

host = "0.0.0.0"
port = 5001
BUFFER_SIZE = 4096
separator = "<SEPARATOR>"


print("Connecting to GEOTIFF over ZMQ...")
context = zmq.Context()
subscriber = context.socket(zmq.SUB)
subscriber.bind("tcp://*:5555")
subscriber.setsockopt_string(zmq.SUBSCRIBE, '')

print(f"Listening over {subscriber}...")


fileBuffer = subscriber.recv.buffer()
subscriber.send("Received!")
fileName = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'sample.tif')
fileHandle = open(fileName, "w")
fileHandle.write(fileBuffer)
fileHandle.close
subscriber.close
context.term
    
time.sleep(5)
