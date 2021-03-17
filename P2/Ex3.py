from Client0 import Client

PRACTICE = 2
EXERCISE = 3

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
PORT = 8081
IP = "127.0.0.1"

c = Client(IP, PORT)
print(c)
# -- Send a message to the server

print("Sending a message to the server...")
response = c.talk("Testing!!!")
print(f"Response: {response}")