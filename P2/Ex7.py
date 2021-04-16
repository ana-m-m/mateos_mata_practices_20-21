from Client0 import Client

from Seq2 import Seq
PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
PORT = 8080
PORT_2 = 8081
IP = "127.0.0.1"
FOLDER = "../P0/Sequences/"
c = Client(IP, PORT)
c_2 = Client(IP, PORT_2)

s = Seq()
s.read_fasta(FOLDER + "FRAT1.txt")

count = 0
i = 0
while i < len(s.strbases) and count < 5:
    fragment = s.strbases[i: i + 10]
    count += 1
    i += 10
    print("Fragment", count, ":", fragment)
    if count % 2 == 0:
        print(c_2.talk("Fragment " + str(count) + ":" + fragment))
    else:
        print(c.talk("Fragment " + str(count) + ":" + fragment))
