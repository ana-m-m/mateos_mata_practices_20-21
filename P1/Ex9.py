from Seq1 import Seq


def print_result(seq):
    print(f"Sequence : (Length: {seq.len()}) {seq}")
    print("  Bases:", seq.count())
    print("  Rev:", seq.reverse())
    print("  Comp:", seq.complement())


print("-----| Practice 1, Exercise 9 |------")
# -- Create a Null sequence
s = Seq()
FOLDER = "../P0/Sequences/"
# -- Initialize the null seq with the given file in fasta format
s.read_fasta(FOLDER + "U5.txt")
print_result(s)
