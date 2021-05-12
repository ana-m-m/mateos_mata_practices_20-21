import pathlib

import termcolor
import colorama
from jinja2 import Template

#from Seq3 import Seq
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

def read_template_html_file(filename):
    content = Template(pathlib.Path(filename).read_text())
    return content

def get(list_sequences, seq_number):

    context = {"number": seq_number, "sequence": list_sequences[int(seq_number)]}
    contents = read_template_html_file("./html/get.html").render(context=context)
    return contents




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


def gene(seq_name):
    PATH = "./Sequences/" + seq_name + ".txt"
    s1 = Seq()
    s1.read_fasta(PATH)
    context = {"gene_name": seq_name, "gene_contents": s1.str_bases}
    contents = read_template_html_file("./html/gene.html").render(context=context)
    return contents
