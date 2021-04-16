import socket
import subprocess
subprocess.call('', shell=True)
import termcolor
from termcolor import colored


class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def ping(self):
        print("Ok")

    def advanced_ping(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.ip, self.port))  # es un tuple!!
            print("Server is up")
        except ConnectionRefusedError:  # check good connection
            print(" Could not connect to the server. Is it running? Have you connected?")

    def __str__(self):
        return "Connection to SERVER at " + str(self.ip) + " PORT: " + str(self.port)

    def talk(self, msg):
        # -- Create the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port))

        # Send data.
        print("* Testing", msg.split(" ")[0], "...")  # mirar esto para Ex4.py
        s.send(msg.encode())

        # Receive data
        response = s.recv(200000).decode("utf-8")

        # Close the socket
        s.close()

        # Return the response
        return  response


    def debug_talk(self, msg):
        # -- Create the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port))

        # Send data.
        print("To Server:")
        termcolor.cprint(msg, "blue")
        msg = colored(msg, "green")
        s.send(msg.encode())

        # Receive data
        response = s.recv(2048).decode("utf-8")

        # Close the socket
        s.close()

        # Return the response
        print("From server: ")
        termcolor.cprint(response, 'green')
