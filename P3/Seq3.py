from pathlib import Path


class Seq:
    NULL_SEQUENCE = "NULL"
    INVALID_SEQUENCE = "ERROR"

    def __init__(self, bases=NULL_SEQUENCE):
        self.strbases = bases
        if self.strbases == Seq.NULL_SEQUENCE:
            print("NULL Sequence created")
        else:
            if Seq.valid_sequence(self.strbases):
                print("New sequence is created!")
            else:
                self.strbases = Seq.INVALID_SEQUENCE
                print("INVALID Seq!")

    def __str__(self):
        return self.strbases

    def len(self):
        if Seq.valid_sequence(self.strbases):
            return len(self.strbases)
        else:
            return 0

    def count_base(self, base):
        base_count = 0
        if Seq.valid_sequence(self.strbases):
            for i in self.strbases:
                if i == base:
                    base_count += 1
        return base_count

    def count(self):
        base_dict = {"A": 0, "C": 0, "G": 0, "T": 0}
        if Seq.valid_sequence(self.strbases):
            for i in self.strbases:
                base_dict[i] += 1
        return base_dict

    def reverse(self):
        if Seq.valid_sequence(self.strbases):
            return self.strbases[::-1]
        else:
            return self.strbases

    def complement(self):
        if Seq.valid_sequence(self.strbases):
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
        return sequence

    def base_percentage(self):
        base_count_dict = Seq.count(self)
        strbases_len = Seq.len(self)
        base_percent_list = []
        bases = []
        for base, count in base_count_dict.items():
            percent = (int(count)/strbases_len) * 100
            base_percent_list.append(round(percent, 1))
            bases.append(base)
        return dict(zip(bases, base_percent_list))

    @staticmethod
    def valid_sequence(bases):
            nucleic_bases = "ACGT"
            for base in bases:
                if base not in nucleic_bases:
                    return False
            return True


def test_sequences():
    s1 = Seq()
    s2 = Seq("ACTGA")
    s3 = Seq("Invalid sequence")
    return s1, s2, s3
