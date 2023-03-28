import zmq
import socket
import tqdm
import time
import os

separator = "<SEPARATOR>"
BUFFER_SIZE = 4096

print("GEOTIFF over ZMQ initializing...")
context = zmq.Context()
publisher = context.socket(zmq.PUB)
publisher.bind("tcp://*:5555")
time.sleep(1)
ourFile = 'C:\Personal Projects\geotiff_over_zmq\sample.tif'
size = os.stat(ourFile).st_size
print(f"The size of this file is: {size} bytes")

target = open(ourFile, 'rb')
file = target.read(size)
if file:
    publisher.send(file)


publisher.close
context.term
target.close
time.sleep(10)


