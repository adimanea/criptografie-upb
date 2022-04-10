# exemplu: 
#   - `python3 M3P5.py 14` => verificam daca 14 este prim, si vom returna primul 'b' pentru care nu este prim
#   - `python3 M3P5.py 999999999` ...
import argparse

parser = argparse.ArgumentParser(description='Testul Solovay-Strassen exact. Afisam primul b pentru care b^{(n-1)/2} != (b/n) mod n, daca n nu este prim.')
parser.add_argument('n', metavar='n', type=int, nargs='+',
                    help='numarul pe care il testam')
args = parser.parse_args()
n = args.n[0]
print(f'Testam daca numarul {n} este prim.')

Zn = {1}
for i in range(1, n-1):
    Zn.add(pow(i, 2) % n)
print(f'Zn = {Zn}')

# calculeaza simbolul iacboi pentru (b/n)
def iacobi(b, n, Zn):
    if (n % 2 == 0):
        print('pentru calculul Simbolului Iacobi, n trebuie sa fie impar!')
        exit(-1)
    if (b % n == 0):
        return 0
    if b in Zn:
        return 1
    return -1

prim = True
mid = int((n-1) / 2)
for i in range(1, n-1):
    iacobi_curent = iacobi(i, n, Zn)
    # b in sens de b = b^{(n-1)/2}
    b = pow(i, mid)
    if (iacobi_curent != b % n and iacobi_curent != b % -n):
        prim = False
        print(f'{n} nu este prim pentru ca {i}^{mid}={b} mod {n} = {b % n} = {b % -n}, diferit de (b/n) = {iacobi_curent}')
        break
    # pentru a imbunatati, daca b%n nu apartine {-1, 0, 1}, atunci putem sa spunem direct ca nu e prim, fara sa mai calculam simbolul Iacobi

if prim:
    print(f'{n} este prim.')
