from Client0 import Client

PRACTICE = 3
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

PORT = 8080
IP = "127.0.0.1"


print(f"Connection to SERVER at {IP}, PORT: {PORT}")
c = Client(IP, PORT)


# communicate with server, commands-arguments
exit = False
while not exit:
    msg = input("Enter command argument: ")
    if msg == "":
        exit = True
    else:
        print(c.talk(msg))
        print()



