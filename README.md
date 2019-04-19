This temperature monitoring program aggregates data from various client sensors at a centralized server.

server.py
  The server allows multiple TCP clients. Once connected to a client, the server will display the temperature the client sends it. 

clients
  Each temperature sensor runs an instance of client.py.Each instance will give its probe ID and its location. Once connected to the server, the client will send updates to the server about its temperature. 

  client.py
  This script simulates a signal. Instead of reading the temperature sensor we return some interger. This way we can develop without having to set up the actual controller. 

  client1-3.py
  Three clients are in the directory.  Each individual client is hardcoded per our cooresponding sensor IDs.  We did this for simplicity during presentation instead having to type the complex ID name for each instance of client. 
