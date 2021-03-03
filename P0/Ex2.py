import Seq0
ID = "U5.txt"
FOLDER = "./Sequences/"
# number of dots depending on the PARENT directory

# path created: ./sequences/U5.txt

U5_Seq = Seq0.seq_read_fasta(FOLDER + ID)
print("the first 20 bases are:", U5_Seq[0:20])
