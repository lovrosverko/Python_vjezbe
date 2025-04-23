def jedinstveni_elementi(lista):
    
    for element in lista:
        if lista.count(element) > 1:
            lista.remove(element)
    
    
    return lista

print(jedinstveni_elementi([1, 2, 2, 3, 3, 3, 4, 5, 5])) # Treba ispisati: [1, 2, 3, 4, 5]
            