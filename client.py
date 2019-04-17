# Python TCP Client A
import json
import socket
import time
import threading
import ftplib

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


def send_message(temp_id, loc, temp_reading):
    message = {
        "MessageType": "status",
        "ProbeID": temp_id,
        "Location": loc,
        "Temperature": temp_reading
    }
    tcpClient.send(json.dumps(message).encode('utf-8'))
    data_p = tcpClient.recv(BUFFER_SIZE)
    data = json.loads(data_p.decode('utf-8'))
    print(data)


# TO DO: Implement with probe
def get_temp(fakeTemp):
    fakeTemp = int(fakeTemp)+1
    return str(fakeTemp)


if __name__ == "__main__":

    temperature=1

    host_centralServer = "localhost"
    port_centralServer = 2019
    BUFFER_SIZE = 1000

    print("Trying to connect to central server..\n")
    tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpClient.connect((host_centralServer, port_centralServer))

    tempID=input("Enter temperature probe ID: ")
    location=input("Enter location of temperature probe: ")

    while 1:
        temperature=get_temp(temperature)
        send_message(tempID, location, temperature)
        time.sleep(2)
