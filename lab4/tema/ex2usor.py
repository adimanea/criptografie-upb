import string
def caesar_flux(cuvant):
    pozitii_clar = []
    cod = ''
    
    for el in cuvant:
        pozitii_clar += [string.ascii_lowercase.index(el)]
    
    cheie = string.ascii_lowercase.index(cuvant[-1])
    if cuvant[-1] == 'a' and cuvant[0] != 'a':
        cheie = string.ascii_lowercase.index(cuvant[0])
    elif cuvant[0] == 'a': 
        cheie = sum(pozitii_clar)
    
    print(cheie)
    print(pozitii_clar)

    for i in range(len(pozitii_clar)):
        pozitii_clar[i] = (pozitii_clar[i] + cheie) % 26

    for el in pozitii_clar:
        cod += chr(el + 97)

    return cod

if __name__ == '__main__':
    cuvant = input()
    print(caesar_flux(cuvant))