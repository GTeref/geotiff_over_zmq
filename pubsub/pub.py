import zmq
import socket
import tqdm
import time
import os

separator = "<SEPARATOR>"
BUFFER_SIZE = 4096
fileName = "sample.tif"

print("GEOTIFF over ZMQ initializing...")
context = zmq.Context()
print("Creating publisher socket....")
publisher = context.socket(zmq.PUB)
publisher.connect("tcp://localhost:5555")
print(f"Connecting to {publisher}...")
time.sleep(1)
size = os.path.getsize(fileName)
print(f"The size of {fileName} is: {size} bytes.")

publisher.send_string(f"{fileName}{separator}{size}")

progress = tqdm.tqdm(range(size), f"Sending {fileName}", unit="B", unit_scale=True, unit_divisor=1024)
with open(fileName, "rb") as f:
    while True:
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            break
        else:
            publisher.send(bytes_read)
            progress.update(len(bytes_read))
publisher.close





