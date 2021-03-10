class Seq:
    def __init__(self, bases="NULL"):
        self.strbases = bases
        if self.strbases == "NULL"
            print("NULL Sequence created")
        else:
            self.strbases = strbases
            print("New sequence is created")
    def __str__(self):
        return self.strbases
    def len(self):
        return len(self.strbases)
class Gene(Seq):
    def __init__(self, strbases, name=""):
        super().__init__(strbases) #initialize
        self.name = name
        print("new gene is created")
    def __str__(self):
        return self.name + "-" + self.strbases
    def len(self):
        if len(self.strbases) < 10:
            return "Sequence " + self.strbases + "is too long"
        else:
            return "Sequence " + self.strbases + "is long"

s1 = Seq("AGTACAATCTGGT")
s1.strbases = "AGTGGTGG"
s1.len()
g = Gene("CGTAAAAGCTGC", "FRAT1")
print(f"Sequence 1 : {s1}")
print(f"gene: {g}")


