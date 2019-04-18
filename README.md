This temperature monitoring program aggregates data from various client sensors at a centralized server.

server.py
The server allows multiple TCP clients. Once connected to a client, the server will display the temperature the client sends it. 

client.py
Each temperature sensor runs an instance of client.py.Each instance will give its probe ID and its location. Once connected to the server, the client will send updates to the server about its temperature. 
