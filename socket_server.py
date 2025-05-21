'''
https://www.geeksforgeeks.org/simple-calculator-in-python-socket-programming/#
https://stackoverflow.com/questions/10810249/python-socket-multiple-clients
'''

# Import socket module
import socket
from threading import Thread

# Here we use localhost ip address
# and port number
LOCALHOST = "127.0.0.1"
PORT = 8080
# calling server socket method
server = socket.socket(socket.AF_INET,
					socket.SOCK_STREAM)
server.bind((LOCALHOST, PORT))
server.listen(1)
print("Server started")
print("Waiting for client request..")

def new_client(clientConnection, clientAddress):
    msg = ''
    # Running infinite loop
    while True:
        data = clientConnection.recv(1024)
        msg = data.decode()
        if msg == 'Over':
            print("Connection is Over")
            break

        print("Equation is received")
        result = 0
        operation_list = msg.split()
        oprnd1 = operation_list[0]
        operation = operation_list[1]
        oprnd2 = operation_list[2]

        # here we change str to int conversion
        num1 = int(oprnd1)
        num2 = int(oprnd2)
        # Here we are perform basic arithmetic operation
        if operation == "+":
            result = num1 + num2
        elif operation == "-":

            result = num1 - num2
        elif operation == "/":
            result = num1 / num2
        elif operation == "*":
            result = num1 * num2

        print("Send the result to client")
        # Here we change int to string and
        # after encode send the output to client
        output = str(result)
        clientConnection.send(output.encode())
    clientConnection.close()
    thread.join()


# client_list = []
# Here server socket is ready for
# get input from the user
if __name__ == "__main__":
    while True:
        clientConnection, clientAddress = server.accept()
        print("Connected client :", clientAddress)
        thread = Thread(target=new_client,args=(clientConnection,clientAddress))
        thread.start()