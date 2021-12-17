import string
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

if __name__ == '__main__':
    cuvant = input()
    cheie1 = int(input())
    cheie2 = int(input())
    print(criptarea_afina_flux(cuvant, cheie1, cheie2))