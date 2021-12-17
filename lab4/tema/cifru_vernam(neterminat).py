import string
import random

def vernam(clar):
    pozitii_clar = []
    cod = []
    stream = [random.choice(range(5000)) for i in range(len(clar))]
    pozitii_clar = [string.ascii_lowercase.index(el) for el in clar]

    for i in range(len(clar)):
        cod.append(stream[i] ^ pozitii_clar[i])
    return cod

if __name__ == '__main__':
    cuvant = input('Cuvant: ')

    print(vernam(cuvant))