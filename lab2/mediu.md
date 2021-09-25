# Laborator 2: Aritmetică

## Precizări inițiale
- Dacă nu se specifică separat, toate numerele cu care lucrăm sînt *naturale*,
adică *întregi, pozitive*;
- Toate exercițiile de mai jos necesită cel puțin o condiție
de validare. O puteți pune, pentru puncte bonus, sau o puteți ignora, dar
există posibilitatea de a avea erori neprevăzute.
- Toate exercițiile pot fi rezolvate fie într-un limbaj de programare,
fie în pseudocod, fie cu pixul pe foaie. Nu se depunctează în funcție de
modul în care prezentați soluția, dar se acordă puncte bonus pentru soluții
*complete, corecte, implementate, optimizate, explicate.*

-------------

## Exerciții

M1P1. **Grupul unităților lui `Zn`**: Un element `x` din *inelul* `Zn` se numește
*unitate* dacă este nenul și este inversabil față de înmulțire. Mulțimea
tuturor unităților unui monoid sau unui inel `A` se notează `U(A)`.
Citiți de la tastatură `n` și afișați `U(Zn)`. Exemple:
- `U(Z5) = {1, 2, 3, 4}`;
- `U(Z6) = {1, 5}`.

M2P2. **Pătrate perfecte din `Zn`**: Un număr `t` se numește *pătrat perfect în Zn*
dacă există un element `x` din `Zn`, astfel încît `x * x % n = t`.
Citiți de la tastatură `n` și afișați lista pătratelor perfecte `Zn`. 
Să notăm (informal, neconvențional, pentru simplitate) această mulțime cu `P(Zn)`.
Exemplu: `P(Z5) = {1, 4}`.

M2P3. **Multipli comuni**: Citiți de la tastatură două numere `a, b` și `n`.
Afișați primii `n` multipli comuni ai lui `a` și `b`. Exemplu:
`a = 5, b = 20, n = 3`, se afișează `{20, 40, 60}`.

M2P4. **Factori comuni**: Citiți de la tastatură două numere `a, b`
și afișați factorii lor comuni. Opțional, puteți afișa doar factorii
*primi* comuni. Exemplu: `a = 20, b = 50`, se afișează
`1, 2, 5, 10` sau `2, 5` dacă se aleg doar factorii primi.

M2P5. **Conjectura lui Collatz (aka 3n+1)** Pentru detalii, vezi mai întîi
problema U2P9 de [aici](usor.md) și 
[pagina Wiki](https://en.wikipedia.org/wiki/Collatz_conjecture).
Cerința este: Utilizați conjectura lui Collatz pentru un joc:
- jucătorul 1 alege un număr;
- jucătorul 2 alege alt număr;
- cîștigă jucătorul al cărui număr necesită mai mulți pași în conjectura lui Collatz.

Opțional, puteți oferi posibilitatea jucătorilor să reîncerce.

M2P6. **Număr care se divide cu toate numerele:** Cel mai mic număr care se divide 
cu toate numerele de la 1 la 10 este 2520. Aflați cel mai mic număr care se divide 
cu toate numerele de la 1 la 20.

Opțional, puteți lăsa utilizatorul să introducă marginea superioară (`n` și
afișați cel mai mic număr care se divide cu toate numerele de la `1` la `n`).
Dar atenție că numerele devin (foarte) mari (foarte) repede.

M2P7. **Numere triunghiulare:** Un număr se numește *triunghiular* dacă se obține
ca o sumă a lui Gauss, adică dacă este egal cu suma tuturor numerelor naturale
de la 1 la un anumit prag. De exemplu, 10 este triunghiular, pentru că
`10 = 1 + 2 + 3 + 4`.

Vom numi *al n-lea număr triungiular* și-l vom nota (neconvențional)
cu `t(n)` numărul `t(n) = 1 + 2 + 3 + ... + n`.

Afișați numărul triunghiular care are 100 de divizori (nu neapărat primi,
nu neapărat proprii).