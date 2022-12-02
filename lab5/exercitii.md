# Exerciții pe caiet

1. Implementați algoritmul **Diffie-Hellman** în următoarele cazuri (păstrăm notația din [teorie](./README.md#diffie-hellman)). Calculați cheia comună `K` și, opțional, folosiți-o pentru o criptare Caesar:
   1. `a = 5, b = 7, p = 13, alpha = 5`;
   2. `a = 6, b = 8, p = 11, alpha = 7`;
   3. `a = 10, b = 3, p = 17, alpha = 10`;
   4. `a = 9, b = 5, p = 19, alpha = 20`;
   5. `a = 11, b = 11, p = 17, alpha = 30`;
2. Implementați algoritmul **El Gamal** în următoarele cazuri (păstrăm notația din [teorie](./README.md/#algoritmul-el-gamal)), *cu validarea datelor*:
   1. Alice: `G = Z7, g = 3, x = 5`. Calculați cheia publică și cheia privată. Bob: Folosiți `M = 3`, transformarea identică, `y = 4` și calculați secretul public și cifrul `(c1, c2)`. Realizați decriptarea, calculînd `s, s^{-1}, m` și `M`.
   2. Alice: `G = Z11, g = 7, x = 5`. Calculați cheia publică și cheia privată. Bob: Folosiți `M = 7` și transformarea `f(x) = x + 3`, `y = 6` și calculați secretul public și cifrul `(c1, c2)`. Realizați decriptarea, calculînd `s, s^{-1}, m` și `M`.
   3. Alice: `G = Z13, g = 8, x = 11`. Calculați cheia publică și cheia privată. Bob: Folosiți `M = 3` și transformarea `f(x) = 2x - 1`, `y = 5` și calculați secretul public și cifrul `(c1, c2)`. Realizați decriptarea, calculînd `s, s^{-1}, m` și `M`.
3. Implementați algoritmul **RSA** în următoarele cazuri (păstrăm notația din [teorie](./README.md/#rsa)). Alegeți voi  exponenții de criptare și de decriptare, *cu validarea datelor* și (de)criptați mesajul `m = 7` în fiecare caz:
   1. `p = 7, q = 11`;
   2. `p = 11, q = 13`;
   3. `p = 5, q = 19`;
   4. `p = 17, q = 11`;
   5. `p = 23, q = 17`.


# Exerciții de programare

L5E1. Scrieți un program care să calculeze toate puterile elementelor dintr-un
grup multiplicativ `Zn`. Cu alte cuvinte, se citește de la tastatură `n`
și se afișează toate puterile tuturor elementelor din `Zn - {0}`.

L5E2. Scrieți un program care să calculeze logaritmul discret în `Zn`.
Se citește de la tastatură `n`, apoi baza `b` și argumentul `a`, iar
programul afișează `log_b(a)` în `Zn`, dacă există, sau mesajul `nu există`,
în caz contrar.

L5E3. Scrieți un program care să implementeze algoritmul Diffie-Hellman.
- se citesc de la tastatură (sau se aleg aleatoriu) cheile private `a` și `b`;
- se citesc de la tastatură (sau se aleg aleatoriu) un număr prim mare `p` și un întreg `alpha`;
	+ puteți include și validarea datelor: numerele citite să fie naturale, iar `p` să fie prim;
- se calculează cheia publică `A = alpha^a mod p`;
- se calculează cheia publică `B = alpha^b mod p`;
- se calculează cheia comună `K = B^a mod p` sau `K = A^b mod p`;
	+ puteți face ambele calcule și să verificați că cele două valori coincid; altfel, aveți erori în program!
- se afișează cheia `K`.

L5E4. Continuați procedura de mai sus, folosind cheia `K` într-un alt algoritm
criptografic. De exemplu, cifrul Caesar de tip flux, cu tot cu decriptare.

L5E5. Scrieți un program care verifică dacă un număr este generator al unui grup de forma `Zn`.
Citiți de la tastatură `g` și verificați dacă `Zn = <g>`.

L5E6. Scrieți un program care afișează toți generatorii grupului `Zn`, dacă acesta este ciclic.
Se citește `n` și se afișează toți `x`, astfel încît `Zn = <x>` sau `grupul nu este ciclic`,
în caz că `x` nu există.

L5E7. Scrieți un program care afișează toate subgrupurile ciclice generate de elementele
lui `Zn`. Citiți de la tastatură `n` și afișați `<1>, <2>, <3>, ..., <n - 1>`.

L5E8. Scrieți un program care implementează pasul de generare a cheii din algoritmul El Gamal:
- alegeți (sau generați aleatoriu) `q` astfel încît `Zq` să fie grup ciclic (**includeți verificarea!**);
- găsiți un generator `g` al lui `G = Zq` de mai sus;
- alegeți aleatoriu un element `x` din `{1, 2, ..., q - 1}`;
- calculați `h = g^x mod q`;
- Afișați cheia publică `PuK = (G, q, g, h)` și cheia privată `PrK = x`.

L5E9. Implementați pasul de criptare din algoritmul El Gamal, în continuarea exercițiului anterior:
- alegeți (de la tastatură sau aleator) un element `m` din `G = Zq`, care va fi mesajul de transmis;
- alegeți (de la tastatură sau aleator) un element `y` din `{1, 2, ..., q - 1}`;
- calculați și afișați *secretul public*: `s = h^y mod q`;
- calculați `c1 = g^y mod q`;
- calculați `c2 = m & s`;
- afișați cifrul, `(c1, c2)`.

L5E10. Implementați pasul de decriptare din algoritmul El Gamal, în continuarea exercițiului anterior:
- calculați `s = c1^x mod q` și `s = h^y mod q`, verificînd că cele două sînt egale (altfel, aveți o eroare în program!);
- calculați inversul elementului `s` în `G = Zq`;
- calculați `m = c2 * s^{-1}`;

L5E11. Scrieți un program care calculează indicatorul lui Euler. Citiți `n` de la tastatură și afișați `phi(n)`.

L5E12-14. Implementați, pe rînd, pașii din algoritmul RSA:
- Alegerea cheilor `p` și `q` (aleatoriu sau citit de la tastatură), apoi ceilalți pași, astfel încît să afișați `PuK = (e, n)` și `PrK = (d, n)`;
- Criptarea mesajelor, astfel încît să afișați `c`;
- Decriptarea mesajelor, astfel încît să calculați `m'` și să vă asigurați că `m' = m`.

Exemplu de rulare:

```
Introduceți un număr prim p = 13
Introduceți un al doilea număr prim q = 17
Calculez modulul de criptare...
Modulul de criptare este n = 221
Alegeți modulul de criptare, de la 3 la 191, coprim cu 192, e = 5
Calculez exponentul de decriptare...
Exponentul de decriptare este d = 77
Cheia publică este PuK = (5, 221)
Cheia privată de decriptare este PrK = (77, 221)
----------------------------------------------------------------------
Introduceți un număr prim p = 10
Numărul introdus nu este prim, reîncercați.
Introduceți un număr prim p = 11
Introduceți un al doilea număr prim q = 19
Calculez modulul de criptare...
Modulul de criptare este n = 209
Alegeți modulul de criptare, de la 3 la 179, coprim cu 180, e = 4
cmmdc(4, 180) = 4 != 1. Reîncercați.
Alegeți modulul de criptare, de la 3 la 179, coprim cu 180, e = 11
Calculez exponentul de decriptare...
Exponentul de decriptare este d = 131
Cheia publică este PuK = (11, 209)
Cheia privată de decriptare este PrK = (131, 209)
```

Mai departe, pentru criptare:

```
Introduceți un număr prim p = 7
Introduceți un al doilea număr prim q = 11
Calculez modulul de criptare...
Modulul de criptare este n = 77
Alegeți modulul de criptare, de la 3 la 59, coprim cu 60, e = 19
Calculez exponentul de decriptare...
Exponentul de decriptare este d = 19
Cheia publică este PuK = (19, 77)
Cheia privată de decriptare este PrK = (19, 77)
Cum trimiteți mesajul: (a) numeric (b) cu maximum 3 litere: a
Introduceți mesajul numeric m = 411
Calculez mesajul criptat...
Mesajul criptat transmis de Bob este c = 67
```

Sau, în varianta cu text:

```
Introduceți un număr prim p = 13
Introduceți un al doilea număr prim q = 17
Calculez modulul de criptare...
Modulul de criptare este n = 221
Alegeți modulul de criptare, de la 3 la 191, coprim cu 192, e = 15
cmmdc(15, 192) = 3 != 1. Reîncercați.
Alegeți modulul de criptare, de la 3 la 191, coprim cu 192, e = 19
Calculez exponentul de decriptare...
Exponentul de decriptare este d = 91
Cheia publică este PuK = (19, 221)
Cheia privată de decriptare este PrK = (91, 221)

Cum trimiteți mesajul: (a) numeric (b) cu maximum 3 litere: b
Introduceți mesajul de maximum 3 litere m = yes
Mesajul transformat numeric este m = 2458
Mesajul criptat transmis de Bob este c = 157
```

Pentru decriptare:

```
Introduceți un număr prim p = 19
Introduceți un al doilea număr prim q = 41
Calculez modulul de criptare...
Modulul de criptare este n = 779
Alegeți modulul de criptare, de la 3 la 719, coprim cu 720, e = 121
Calculez exponentul de decriptare...
Exponentul de decriptare este d = 601
Cheia publică este PuK = (121, 779)
Cheia privată de decriptare este PrK = (601, 779)
Programul poate decripta doar mesaje numerice.
Cum trimiteți mesajul: (a) numeric (b) cu maximum 3 litere: a
Introduceți mesajul numeric m = 4112
Calculez mesajul criptat...
Mesajul criptat transmis de Bob este c = 217

Decriptare, varianta numerică
Alice a primit mesajul c = 217
Decriptează...
Am obținut m' = 217
Mesajul coincide cu m.
```