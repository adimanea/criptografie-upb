# Laborator 1: Introducere și generalități

## Criptografie
M1C1. Dați exemplu de un algoritm criptografic și la ce este folosit (dacă mai este în uz).

M1C2. Ce este un algoritm criptografic *simetric*?

M1C3. Ce este *hashing*-ul?

M1C4. Ce este *salt*-ul?

M1C5. Ce este un *nonce*? Dar un OTP (*one-time-pad*)?

M1C6. Cîte cifre apreciați că trebuie să aibă un număr folosit într-un algoritm criptografic curent (de exemplu, RSA), astfel încît să fie sigur?

M1C7. Ce este securitatea demonstrabilă (*provable security*)?

M1C8. Ce sînt criptomonedele și unde intervine criptarea?

M1C9. Ce este o coliziune, în cazul unui algoritm criptografic?

M1C10. Ce este securitatea fizică?

## Matematică
M1M1. Calculați:
- ordinul lui 3 în Z5;
- ordinul lui 7 în Z9;
- ordinul lui 5 în Z10;
- ordinul lui 7 în Z13.

M1M2. Calculați:
- logaritm în bază 2 din 3 în Z5;
- logaritm în bază 5 din 2 în Z7;
- logaritm în bază 3 din 7 în Z11.

M1M3. Rezolvați ecuațiile:
- 3x + 2 = 1 în Z7;
- 2x - 1 = 2 în Z5;
- 4x + 3 = 1 în Z10;
- 15x + 2 = 7 în Z3;

M1M4. Rezolvați ecuațiile:
- x^2 + 3x - 1 = 0 în Z5;
- 2x^2 + x - 2 = 0 în Z7;
- 3x^2 - 1 = 5 în Z11.

M1M5. De cîți biți avem nevoie pentru a stoca un număr de 5 cifre?

## Programare
M1P1. Ce calculează și ce afișează bucata de cod de mai jos?
```c++
// C++
int func(int a, int b) {
    while (a != b) {
        if (a > b) {
            a -= b;
        }
        else {
            b -= a;
        }
    }
    return a;
}

int main() {
    int modul;

    modul = 153;
    for (int i = 1; i < modul; i++) {
        if (func(i, modul) != 1) {
            std::cout<<i<<std::endl;
        }
    }

    return 192;
}
```

```python
# Python
def func(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

modul = 153
for i in range(1, modul):
    if func(i,modul) != 1:
        print(i)
```

M1P2. Ce calculează și ce afișează bucata de cod de mai jos?
```c++
// C++
void func(int a, int b) {
    for (int i = 1; i < b; i++) {
        if (a * i % b == 0) {
            std::cout<<"DA!"<<std::endl;
        }
        else {
            std::cout<<"NU!"<<std::endl;
        }
    }
}

int main() {
    int x = 15, y = 7, n = 100;

    func(x, n);
    func(y, n);

    return 171;
}
```

```python
# Python
def func(a, b):
    for i in range(1, b):
        if a * i % b == 0:
            print("DA")
        else:
            print("NU")

x = 15
y = 7
n = 100
func(x, n)
func(y, n)
```

M1P3. (De)Scrieți un program/algoritm care calculează radical din `n` modulo `m`, cu `m` și `n` citite de la tastatură (adică radical din `n` în `Zm`).

M1P4. (De)Scrieți un program/algoritm care calculează ordinul lui `m` în `Zn`, cu `n` și `m` citite de la tastatură.

M1P5. (De)Scrieți un program/algoritm care calculează de cîți biți este nevoie pentru a stoca numărul `n`, citit de la tastatură.