import zmq
import time
import os
import sys

bindPort = ("tcp://0.0.0.0:135")
print("Connecting to file server...")
context = zmq.Context()
publisher = context.socket(zmq.PUB)
publisher.bind(bindPort)
time.sleep(1)
ourFile = 'C:\Personal Projects\geotiff_over_zmq\sample.tif'

size = os.path.getsize(ourFile)

target = open(ourFile, 'rb')
file = target.read(size)
if file:
    publisher.send(file)

publisher.close
context.term
target.close
time.sleep(10)


