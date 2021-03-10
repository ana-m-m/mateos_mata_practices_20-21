from pathlib import Path


class Seq:

    def __init__(self, bases="NULL"):
        self.strbases = bases
        if self.strbases == "NULL":
            print("NULL Sequence created")
        else:
            if valid_sequence(self.strbases):
                print("New sequence is created")
            else:
                self.strbases = "ERROR"
                print("INVALID Seq!")

    def __str__(self):
        return self.strbases

    def len(self):
        if valid_sequence(self.strbases):
            return len(self.strbases)
        else:
            return 0

    def count_base(self, base):
        base_count = 0
        if valid_sequence(self.strbases):
            for i in self.strbases:
                if i == base:
                    base_count += 1
        return base_count

    def count(self):
        base_dict = {"A": 0, "C": 0, "T": 0, "G": 0}
        if valid_sequence(self.strbases):
            for i in self.strbases:
                base_dict[i] += 1
        return base_dict

    def reverse(self):
        if valid_sequence(self.strbases):
            return self.strbases[::-1]
        else:
            return self.strbases

    def complement(self):
        if valid_sequence(self.strbases):
            comp_bases = {"A": "T", "T": "A", "C": "G", "G": "C"}
            comp_seq = ""
            for i in self.strbases:
                comp_seq += comp_bases[i]
            return comp_seq
        else:
            return self.strbases

    def read_fasta(self, filename):
        sequence = Path(filename).read_text()
        sequence = sequence[sequence.find("\n") + 1:].replace("\n", "")
        self.strbases = sequence


def valid_sequence(bases):
    nucleic_bases = "ACGT"
    for base in bases:
        if base not in nucleic_bases:
            return False
    return True


def get_key(val, my_dict):
    for key, value in my_dict.items():
         if val == value:
             return key
