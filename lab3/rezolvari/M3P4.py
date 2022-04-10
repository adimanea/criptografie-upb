# exemplu: 
#   - `python3 M3P4.py 14` => verificam daca 14 este prim, si vom returna primul 'a' pentru care nu este prim
#   - `python3 M3P4.py 999999999` ...
import argparse

parser = argparse.ArgumentParser(description='Testul Fermat exact. Afisam primul a pentru care a^{n-1} != 1 mod n, daca n nu este prim.')
parser.add_argument('n', metavar='n', type=int, nargs='+',
                    help='numarul pe care il testam')
args = parser.parse_args()
n = args.n[0]
print(f'Testam daca numarul {n} este prim.')

# aici incepe codul efectiv
prim = True
if (n !=2 and n % 2 == 0):
    print(f'2 este singurul numar prim par')
    exit(-1)

for a in range(2,n):
    intermediar = pow(a, n-1) % n
    if (intermediar != 1):
        prim = False
        print(f'{n} nu este prim, pentru ca pentru a={a} => {a}^{n-1} = {intermediar} mod {n}, deci diferit de 1 mod {n}')
        break

if prim:
    print(f'{n} este prim.')
