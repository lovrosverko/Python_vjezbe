def je_prost(broj):
  """
  Provjerava je li dani broj prost.

  Argument:
    broj: Cijeli broj za provjeru.

  Vraća:
    True ako je broj prost, False inače.
  """
  # Prost broj mora biti veći od 1
  if broj <= 1:
    return False
  # Provjeravamo djeljivost s brojevima od 2 do korijena broja
  for i in range(2, int(broj**0.5) + 1):
    if broj % i == 0:
      return False
  return True

# Primjeri korištenja funkcije
print(je_prost(2))   # Ispis: True
print(je_prost(10))  # Ispis: False
print(je_prost(17))  # Ispis: True