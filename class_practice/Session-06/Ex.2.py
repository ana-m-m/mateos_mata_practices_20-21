class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):

        # Initialize the sequence with the value
        # passed as argument when creating the object

        valid_bases = "ACGT"
        valid_base = 0
        for i in strbases:
            if i in valid_bases:
                valid_base += 1
            else:
                strbases = "ERROR"
        if valid_base == len(strbases):
            print("New sequence created!")
        else:
            print("INCORRECT Sequence detected")
        self.strbases = strbases

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)
    @staticmethod
    def print_seqs(seq_list):
        number_sequences = 0
        for sequence in seq_list:
            return "Sequence" + str(number_sequences) + ": (Length:" + str(Seq.len(sequence))+")" + sequence



class Gene(Seq):
    """This class is derived from the Seq Class
       All the objects of class Gene will inheritate
       the methods from the Seq class
    """
    def __init__(self, strbases, name=""):

        # -- Call first the Seq initilizer and then the
        # -- Gene init method
        super().__init__(strbases)
        self.name = name
        print("New gene created")

    def __str__(self):
        """Print the Gene name along with the sequence"""
        return self.name + "-" + self.strbases

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
r = Seq.print_seqs(seq_list)
print(r)