from Seq1 import Seq, test_sequences


def print_result(seq_list):
    for sequence in seq_list:
        print(f"Sequence {seq_list.index(sequence) + 1}: (Length: {sequence.len()}) {sequence}")
        print("Bases:", sequence.count())


print("-----| Practice 1, Exercise 6 |------")

sequence_list = list(test_sequences())
print_result(sequence_list)
