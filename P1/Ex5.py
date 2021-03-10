from Seq1 import test_sequences


def print_result(seq_list):
    nucleobases_dna = ["A", "C", "T", "G"]
    for sequence in seq_list:
        print(f"Sequence {seq_list.index(sequence)}: (Length: {sequence.len()}) {sequence}")
        for base in nucleobases_dna:
            print(f"   {base}: {sequence.count_base(base)},", end="")
        print()


print("-----| Practice 1, Exercise 5 |------")
list_seq = list(test_sequences())
print_result(list_seq)
