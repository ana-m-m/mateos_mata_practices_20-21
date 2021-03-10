from Seq1 import Seq


def print_result(sequence):
    print(f"Sequence 1: {sequence}")


# -- Create a Null sequence
s1 = Seq()

# -- Create a valid sequence
s2 = Seq("ACTGA")

# -- Create an invalid sequence
s3 = Seq("Invalid sequence")
print_result(s1)
print_result(s2)
print_result(s3)
