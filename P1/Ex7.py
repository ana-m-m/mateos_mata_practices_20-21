from Seq1 import test_sequences


def print_result(seq_list):
    for sequence in seq_list:
        print(f"Sequence {seq_list.index(sequence)}: (Length: {sequence.len()}) {sequence}")
        print("  Bases:", sequence.count())
        print("  Rev:", sequence.reverse())


print("-----| Practice 1, Exercise 7 |------")

sequence_list = list(test_sequences())
print_result(sequence_list)
