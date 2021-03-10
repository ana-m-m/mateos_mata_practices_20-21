from Seq1 import Seq
print("-----| Practice 1, Exercise 5 |------")
# -- Create a Null sequence
s1 = Seq()

# -- Create a valid sequence
s2 = Seq("ACTGA")

# -- Create an invalid sequence
s3 = Seq("Invalid sequence")
seq_list = [s1, s2, s3]
nucleobases_dna = ["A", "C", "T", "G"]
for sequence in seq_list:
    print(f"Sequence {seq_list.index(sequence)}: (Length: {sequence.len()}) {sequence}")
    for base in nucleobases_dna:
        print(f"   {base}: {sequence.count_base(base)},", end="")
    print()
