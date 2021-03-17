from Client0 import Client
from pathlib import Path
PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
PORT = 8081
IP = "127.0.0.1"
FOLDER = "../P0/Sequences/"
c = Client(IP, PORT)
print(c)
print(c.talk("Sending the U5 to the server..."))
print(c.talk(Path(FOLDER + "U5.txt").read_text()))
