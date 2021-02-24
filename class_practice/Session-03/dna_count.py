def counter_of_bases(dna):
    a, c, g, t = 0, 0, 0, 0
    for i in dna:
        if i == "A":
            a += 1
        elif i == "C":
            c += 1
        elif i == "G":
            g += 1
        else:
            t += 1
    return a, c, g, t
dna = input("Enter sequence: ")
print("total length: ", len(dna))
a, c, g, t = counter_of_bases(dna)
print("A: ", a)
print("C: ", c)
print("G: ", g)
print("T: ", t)