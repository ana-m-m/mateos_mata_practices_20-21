import socket

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Configure the Server's IP and PORT
PORT = 8080
IP = "127.0.0.1"

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")
count_connections = 0
client_address_list = []
while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()
        client_address_list.append(client_ip_port)
        count_connections += 1
        print("connection " + str(count_connections) + "client ip, port: " + str(client_ip_port))

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        ls.close()
        exit()

    # -- Execute this part if there are no errors
    #else:

    print("A client has connected to the server!")

    msg_raw = cs.recv(2048)

    msg = msg_raw.decode()

    # -- Print the received message
    print(f"Message received: {msg}")

    # -- Send a response message to the client
    try:
        response = int(msg) ** int(msg)
        print("response", response)
        cs.send(str(response).encode())
    except ValueError:
        cs.send("we need a number".encode())

    # -- The message has to be encoded into bytes


    # -- Close the data socket
    cs.close()
    if count_connections == 5:
        for i in range(0, len(client_address_list)):
            print("client "+ str(i) + " client ip, port : " + str(client_address_list[i]))
        exit(0)
# values in exit : -1 se acaba sin erminar bien
#                : 0 se acaba cuando se queria
#                : 1 se acaba por exeption, error
