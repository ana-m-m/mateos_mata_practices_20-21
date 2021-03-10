from Seq1 import Seq
print("-----| Practice 1, Exercise 9 |------")
# -- Create a Null sequence
s = Seq()
FOLDER = "../P0/Sequences/"
# -- Initialize the null seq with the given file in fasta format
s.read_fasta(FOLDER + "U5.txt")
print(f"Sequence : (Length: {s.len()}) {s}")
print("  Bases:", s.count())
print("  Rev:", s.reverse())
print("  Comp:", s.complement())
