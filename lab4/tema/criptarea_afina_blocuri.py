import string
import math

def criptarea_afina_flux(cuvant, cheie1, cheie2):
    pozitii_clar = []
    cod = ''
    
    for el in cuvant:
        pozitii_clar += [string.ascii_lowercase.index(el)]

    for i in range(len(pozitii_clar)):
        pozitii_clar[i] = (pozitii_clar[i] * cheie1 + cheie2) % 26
    for el in pozitii_clar:
        cod += chr(el + 97)

    return cod

def criptarea_afina_bloc(clar, chei, lungime_blocuri):
    blocuri = [clar[i:i+lungime_blocuri] for i in range(0, len(clar), lungime_blocuri)]
    cod = ''
    for i in range(len(blocuri)):
        cod += criptarea_afina_flux(blocuri[i], chei[i][0], chei[i][1])
    return cod

if __name__ == '__main__':
    cuvant = input('Cuvant: ')
    b = int(input('Lungime blocuri: '))
    bloc1cheie1 = int(input("Cheie1: "))
    bloc1cheie2 = int(input("Cheie2: "))
    chei = [(bloc1cheie1,bloc1cheie2)]

    for i in range(math.ceil(len(cuvant)/b)):
        chei.append((chei[i][0]**2, chei[i][1]**2))

    print(criptarea_afina_bloc(cuvant, chei, b))