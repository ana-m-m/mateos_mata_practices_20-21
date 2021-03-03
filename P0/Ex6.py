import Seq0
ID = "U5.txt"
FOLDER = "./Sequences/"
U5_Seq = Seq0.seq_read_fasta(FOLDER + ID)[0:20]
print("Gene U5:")
print("Frag:", U5_Seq)
print("Rev:", Seq0.seq_reverse(U5_Seq))
