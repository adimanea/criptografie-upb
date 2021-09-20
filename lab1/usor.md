# Exerciții ușoare

## Criptografie

U1C1. Cu ce se ocupă criptografia și care sînt domeniile conexe?

U1C2. Ce exemple de apariții ale criptografiei ați întîlnit, în cărți, filme, jocuri etc.?

U1C3. Dați exemple de servicii pe care le folosiți zilnic și care \(afirmă\) că vă criptează comunicarea și datele.

U1C4. Ce este procesul de _autentificare_? Dar procesul de _autorizare_? Dați un exemplu în care cele două procese diferă \(i.e. un utilizator s-a autentificat, dar nu este autorizat și invers\).

U1C5. Putem spune că utilizarea unui lacăt cu cifru la o valiză este o măsură criptografică? Argumentați.

U1C6. Anonimizarea pe Internet este o măsură criptografică? Argumentați.

U1C7. Descrieți, în cuvintele voastre, termenii:

* atacul cu forță brută \(eng. _brute force attack_\);
* atacul _man in the middle_ \(MiTM\);
* atacul dicționar \(eng. _dictionary attack_\);
* inginerie socială \(eng. _social engineering_\);
* certificat digital;
* semnătură digitală.

U1C8. Cum vedeți viitorul criptografiei?

U1C9. Puteți concepe criptografia în afara mediului digital \(criptarea altor date decît a celor din computere sau dispozitive inteligente\)? Dați un exemplu.

U1C10. De ce credeți că numerele prime sînt foarte importante în criptografie?

## Matematică

U1M1. Calculați:

* 15 mod 3; 
* 12 mod 8; 
* -2 mod 5;
* 999 mod 2;
* 999 mod 3.

U1M2. Calculați:

* inversul lui 3 mod 7;
* inversul lui 3 mod 8;
* inversul lui 3 mod 9;
* inversul lui -5 mod 7;
* inversul lui 20 mod 2000;
* inversul lui -5 mod 9.

U1M3. Rezolvați în Z5 ecuația 3x + 1 = 2.

U1M4. Scrieți în baza 2 numerele: 11, 31, 32, 51, 88, 100.

U1M5. Scrieți în baza 10 numerele în binar: 111, 10101, 11111, 10000, 1001001, 11001100.

## Programare

U1P1. Ce calculează și ce afișează următoarea bucată de cod?

```cpp
// C++
int v[100], int m;
m = -9999;
for (int i = 0; i < n; i++)
    if (v[i] > m)
        m = v[i];

std::cout<<m<<std::endl;
```

```python
# Python
m = -999
for i in range(len(v)):
    if v[i] > m:
        m = v[i]

print(m)
```

U1P2. Ce calculează și ce afișează următoarea bucată de cod?

```cpp
// C++
int d = 0, i = 0, v[100];

while (i < n) {
    if (v[i] % 3 == 0) {
        d++;
    }
    i++;
}

std::cout<<d<<std::endl;
```

```python
# Python
d = 0
for elt in v:
    if elt % 3 == 0:
        d += 1
print(d)
```

U1P3. Ce calculează și ce afișează următoarea bucată de cod?

```cpp
// C++
int func(int x, int m) {
    for (int i = 0; i < m; i++) {
        if ((x * i) % m == 1) {
            return i;
        }
    }
    return 0;
}

int main() {
    int nr = 5, mod = 11;

    if func(nr,mod) {
        std::cout<<func(nr,mod)<<std::endl;
    }
    else {
        std::cout<<"Nu se poate."<<std::endl;
    }

    return 42;
}
```

```python
# Python
def func(x, m):
    for i in range(m):
        if (x * i) % m == 1:
            return i
    return 0

nr = 5
mod = 11
if func(nr, mod):
    print(func(nr, mod))
else:
    print("Nu se poate")
```

U1P5. \(De\)Scrieți un program/algoritm care numără multiplii de 3 sau de 5 mai mici decît 1000.

U1P6. \(De\)Scrieți un program/algoritm care citește `n` de la tastatură și afișează dacă `n` este pătrat perfect.

U1P7. \(De\)Scrieți un program/algoritm care citește `n` de la tastatură și afișează al `n`-lea număr prim.

U1P8. \(De\)Scrieți un program/algoritm care citește `n` de la tastatură și afișează cel mai mic număr prim strict mai mare decît `n`.

