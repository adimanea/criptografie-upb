import string
def caesar_flux(cuvant, cheie):
    pozitii_clar = []
    cod = ''

    for el in cuvant:
        pozitii_clar += [string.ascii_lowercase.index(el)]

    for i in range(len(pozitii_clar)):

        pozitii_clar[i] = (pozitii_clar[i] + cheie) % 26
    for el in pozitii_clar:
        cod += chr(el + 97)

    return cod

if __name__ == '__main__':
    cuvant = input()
    cheie = int(input())
    print(caesar_flux(cuvant, cheie))