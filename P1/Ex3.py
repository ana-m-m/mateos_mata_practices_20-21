from Seq1 import test_sequences


def print_result(seq_list):
    for seq in seq_list:
        print(f"Sequence 1: {seq}")

print("-----| Practice 1, Exercise 3 |------")

sequences_list = list(test_sequences())
print_result(sequences_list)
