from Seq1 import Seq, test_sequences


def print_result(sequence_list):
    for sequence in sequence_list:
        print(f"Sequence 1: (Length: {sequence.len()}) {sequence}")


print("-----| Practice 1, Exercise 4 |------")
seq_list = list(test_sequences())
print_result(seq_list)
