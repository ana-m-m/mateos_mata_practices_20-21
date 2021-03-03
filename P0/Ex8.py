import Seq0
IDS = ["U5.txt", "ADA.txt", "FRAT1.txt", "FXN.txt"]
FOLDER = "./Sequences/"
GENES = []
for ID in IDS:
    GENES.append(Seq0.seq_read_fasta(FOLDER + ID))
IDS_MAX_BASES = Seq0.seqs_max_base(IDS, GENES)
Seq0.print_seqs_max_bases(IDS_MAX_BASES)

