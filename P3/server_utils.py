import termcolor
import colorama
from Seq3 import Seq


def print_colored(message, color):

    colorama.init()
    print(termcolor.colored(message, color))


def format_command(command):
    return command.replace("\r", "")


def ping(cs):
    print_colored("PING command!", "yellow")
    response = "OK!"
    print(response)
    cs.send(str(response).encode())


def get(cs, list_sequences, argument):
    print_colored("GET", "yellow")
    response = list_sequences[int(argument)]
    cs.send(response.encode())
    return response


def info(cs, argument):
    print_colored("INFO", "yellow")
    sequence = Seq(argument)
    seq_len = sequence.len()
    bases_count = list(sequence.count().values())
    bases_percent = list(sequence.base_percentage().values())
    bases = list(sequence.count().keys())
    msg = f"Sequence: {sequence}\n" \
          f"Total length: {seq_len}\n"
    for i in range(len(bases)):
        msg += f"{bases[i]}: {bases_count[i]} ({bases_percent[i]}%)\n"

    cs.send(str(msg).encode())
    return msg


def comp(cs, argument):
    print_colored("COMP", "yellow")
    sequence = Seq(argument)
    comp = sequence.complement()
    cs.send(str(comp).encode())
    return comp


def rev(cs, argument):
    print_colored("REV", "yellow")
    sequence = Seq(argument)
    rev = sequence.reverse()
    cs.send(str(rev).encode())
    return rev


def gene(cs, argument):
    print_colored("GENE", "yellow")
    gene = Seq()
    folder = "../P0/Sequences/"
    gene.read_fasta(folder + argument + ".txt")
    cs.send(str(gene).encode())
    return gene

