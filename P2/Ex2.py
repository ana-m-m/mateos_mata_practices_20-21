from Client0 import Client

PRACTICE = 2
EXERCISE = 2

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
PORT = 8081
IP = "127.0.0.1"

c = Client(IP, PORT)
c.advanced_ping()
print(c)
