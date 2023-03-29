import zmq
import time
import tqdm
import socket
import os

BUFFER_SIZE = 4096
separator = "<SEPARATOR>"
clientAddress = "tcp://*:5555"

print("Connecting to GEOTIFF over ZMQ...")
context = zmq.Context()
subscriber = context.socket(zmq.SUB)
subscriber.bind(clientAddress)
subscriber.setsockopt_string(zmq.SUBSCRIBE, '')

print(f"Listening over {subscriber}...")
fileSocket, serverAddress = subscriber.recv_string()
fileSocket = context.socket(zmq.SUB)
print(f"{serverAddress} has connected to {clientAddress}.")

fileBuffer = fileSocket.recv(BUFFER_SIZE).decode()
fileName, size = fileBuffer.split(separator)
fileName = os.path.basename(fileName)
size = int(size)

progress = tqdm.tqdm(range(size), f"Receiving {fileName}", unit="B", unit_scale=True, unit_divisor=1024)

with open(fileName, "rb") as f:
    while True:
        bytes_read = fileSocket.recv(BUFFER_SIZE)
        if not bytes_read:
            break
        else:
            f.write(bytes_read)
            progress.update(len(bytes_read))

fileSocket.close
subscriber.close
    
time.sleep(5)
