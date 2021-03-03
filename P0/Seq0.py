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


def seqs_max_base(ids, genes):
    max_bases = []
    for gene in genes:
        base_counter = {"A": 0, "C": 0, "T": 0, "G": 0}
        for i in gene:
            base_counter[i] += 1
        max_base_index = list(base_counter.values()).index(max(base_counter.values()))
        max_bases.append(list(base_counter.keys())[max_base_index])
    ids_max_bases = dict(zip(ids, max_bases))
    return ids_max_bases


def print_seqs_max_bases(ids_max_bases):
    for id, max_base in ids_max_bases.items():
        id = id[:-4]
        print("Gene", id, ": Most frequent Base:", max_base)
