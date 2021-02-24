#program that prinnts on the console the first 11 terms of the fibonacci series, starting from 0.
#execute step by step
#mal hecho, solo para probar
series = [0, 1, 1]
a, b = 0, 1
for i in range (1, 13):
    c = b +a
    a, b = b, c
print(series)