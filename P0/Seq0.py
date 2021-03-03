from pathlib import Path


def seq_pin():
    print("OK")


def seq_read_fasta(filename):
    sequence = Path(filename).read_text()
    sequence = sequence[sequence.find("\n") + 1:].replace("\n", "")
    return sequence


def seq_len(seq):
    return len(seq)


def seq_count_base(seq, base):
    return seq.count(base)


def seq_count(seq):
    gene_dict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for d in seq:
        gene_dict[d] += 1
    return gene_dict


def seq_reverse(seq):
    reversed_seq = seq[::-1]
    return reversed_seq


def seq_complement(seq):
    complements_dict = {"A": "T", "T": "A", "C": "G", "G": "C"}
    comp_seq = ""
    for i in seq:
        comp_seq += complements_dict[i]
    return comp_seq

