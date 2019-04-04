# CIS457 Project 2
# Server.py
# Program to create a multi-threaded TCP server
# Server will accept multiple clients and listens for certain messages to search for files

from threading import Thread
import socket
import json
import ast


# Multithreaded Python server
class ThreadedServer(Thread):

    # set up server
    def __init__(self,conn, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.conn = conn
        print("[+] New server socket thread started for " + ip + ":" + str(port))

    def run(self):
        threadAlive=True
        while threadAlive:
            data_packed = self.conn.recv(2048)

            # look for valid return message
            if data_packed != b'':
                try:
                    data = json.loads(data_packed.decode('utf-8'))
                except ValueError:
                    print("Error with JSON decode")
                    return
                # add User to List with info
                if "status" == data["MessageType"]:
                    # message should already be in correct form, append to list
                    return_message = {"Result": "Success"}
                    print("Probe ID: ", data["ProbeID"], "\tLocation: ", data["Location"], "\tTemperature: ",
                          data["Temperature"])

                else:
                    return_message = {"Result": "Error"}
                # send response
                try:
                    self.conn.send(json.dumps(return_message).encode('utf-8'))
                except ValueError:
                    print("Error: Can't send response..")
                    self.conn.send(json.dumps({"Result": "Error"}).encode('utf-8'))


# Multithreaded Python server : TCP Server Socket Program
TCP_IP = '127.0.0.1'
TCP_PORT = 2019

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpServer.bind((TCP_IP, TCP_PORT))
threads=[]


# store user information
users_list = []

while True:
    tcpServer.listen(4)
    print("Multithreaded Python server : Waiting for connections from TCP clients...")
    (conn, (ip,port)) = tcpServer.accept()
    newthread = ThreadedServer(conn,ip, port)
    newthread.start()
    threads.append(newthread)

