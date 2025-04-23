def broji_rijeci(recenica):
    broj = 1
    for slovo in recenica:
        if slovo == " ":
            broj+=1
    return broj

broj = broji_rijeci("Python je zabavan programski jezik.")
print(broj) # Treba ispisati: 5