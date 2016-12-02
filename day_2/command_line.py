
import sys
import httplib

#loading http server ip
http_server =sys.argv[1]
#building the connection
connection_1= httplib.HTTPConnection(http_server)

while True:
   command= raw_input('Enter command (E.g GET index.html)')
   command = command.split()
   if command[0]=='exit': #Exit prompt
     break 
    #beginning Request Phase
    connection.request(command[0], command[1])

    #get from server
    responder=conn.getresponse()

    #Displaying Server response data
    print(response.status,response.reason)
    data_received=response.read()
    print(data_received)
connection.close()
