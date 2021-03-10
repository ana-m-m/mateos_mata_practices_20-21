from Seq1 import Seq


def print_result(seq_list):
    nucleobases_dna = ["A", "C", "T", "G"]
    for sequence in seq_list:
        print(f"Sequence {seq_list.index(sequence)}: (Length: {sequence.len()}) {sequence}")
        for base in nucleobases_dna:
            print(f"   {base}: {sequence.count_base(base)},", end="")
        print()


print("-----| Practice 1, Exercise 5 |------")
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")
list_seq = [s1, s2, s3]
print_result(list_seq)
