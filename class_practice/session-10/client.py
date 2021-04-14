import Client0
c = Client0.Client("127.0.0.1", 8080)
for i in range(0,5):
    c.talk("message " + str(i))