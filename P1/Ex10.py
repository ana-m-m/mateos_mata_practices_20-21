from Seq1 import Seq
import Seq1


print("-----| Practice 1, Exercise 10 |------")
IDS = ["U5.txt", "ADA.txt", "FRAT1.txt", "FXN.txt", "RNU6_269P.txt"]
FOLDER = "../P0/Sequences/"
for ID in IDS:
    s = Seq()
    s.read_fasta(FOLDER + ID)
    max_base_count = max(s.count().values())
    print(f"Gene {ID[:-4]}: Most frequent Base: {Seq1.get_key(max_base_count, s.count())}")
