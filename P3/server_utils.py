def print_colored(message, color):
    import termcolor
    import colorama
    colorama.init(strip="False")
    print(termcolor.colored(message, color))

def format_command(command):
    return command.replace("\r", "")

def ping(cs):
    print_colored("ping command", "green")
    response = "OK"
    cs.send(str(response).encode())
def get(cs, list_sequences, argument):
    print_colored(("GET", "yellow"))
    response = list_sequences[int(argument)]
    print(response)
    cs.send(response.encode())


        #cs.send(str(response).encode())
