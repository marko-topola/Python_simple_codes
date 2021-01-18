def unos():
    try:
        n = int(input("Broj clanova liste?>>>"))
        lista = []
        while n != 0:
            broj = int(input("Unesi broj>>>"))
            lista.append(broj)
            n -= 1
    except ValueError:
        print("Unesite brojeve!")
    return lista

def najveci_parni(lista):
    for i in sorted(lista, reverse=True):
        if i % 2 == 1:
            return i



lista = unos()
najveci_parni_broj = najveci_parni(lista)
print(lista)
print(najveci_parni_broj)

input("\nPretisni enter da izadjes")