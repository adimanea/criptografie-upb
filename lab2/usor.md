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

--------------

## Exerciții

U2P1. **Tabla înmulțirii în `Zn`**: Citiți de la tastatură `n`, întreg pozitiv,
și afișați tabla înmulțirii inelului `Zn`.

U2P2. **Inverse modulare**: Citiți de la tastatură `a, n` și aflați inversul
lui `a` modulo `n`. Indicație: Dacă `b` este inversul lui `a mod n`,
atunci `b` are proprietatea că `a * b % n = 1`.

U2P3. **Divizori ai lui zero**: Citiți de la tastatură `a, n` și aflați dacă
`a` este divizor al lui zero în `Zn`. Indicație: Pentru a fi divizor al lui zero,
`a` trebuie să fie nenul și să existe `b` nenul în `Zn`, astfel încît `a * b % n = 0`.

U2P4. **Ecuații de gradul întîi în `Zn`**: Citiți de la tastatură `a, b, c, n`
și rezolvați ecuația `a*x + b = c` în `Zn`. **Atenție!** Există condiții
de validare, i.e. cazuri cînd ecuația nu poate fi rezolvată.

U2P5. **Fracții ireductibile**: Se citesc de la tastatură `numarator` și `numitor`,
care sînt numărătorul, respectiv numitorul unei fracții de numere întregi.
Aduceți fracția la forma ireductibilă, adică simplificați-o cît se poate.

U2P6. **Suma fracțiilor**: Se citește de la tastatură `n`, apoi `n` fracții
(adică `2*n` numere întregi, în perechi `(numarator, numitor)`). Aduceți fracțiile
la același numitor, calculați suma fracțiilor, afișați rezultatul, apoi simplificați
rezultatul într-o fracție ireductibilă, pe care să o afișați.

U2P7. **`cmmdc` pentru `n` numere** Se citește de la tastatură `n`, apoi `n` numere
întregi pozitive. Calculați `cmmdc` pentru toate aceste numere.

U2P8. **Factorizare**: Se citește de la tastatură `n`, un număr întreg și pozitiv
(preferabil, cu cel puțin 3 cifre). Să se afișeze descompunerea în factori primi
a lui `n`. Exemplu: `n = 100`, se afișează `(2, 2) * (5, 2)`, pentru că
`100 = 2^2 * 5^2`. Puteți alege formatul afișării cum doriți, dar trebuie să fie
clară baza și exponentul pentru fiecare factor prim.

U2P9. **Conjectura lui Collatz (aka 3n+1)**: Se citește de la tastatură un număr
întreg pozitiv `n` și se prelucrează astfel:
- dacă numărul este par, se înjumătățește;
- dacă numărul este impar, se înmulțește cu 3 și se adună 1.
[Conjectura lui Collatz](https://en.wikipedia.org/wiki/Collatz_conjecture) (1937)
afirmă că, indiferent de numărul cu care pornim, se va ajunge la 1 într-un număr
finit de pași.

Testați conjectura pentru cîteva numere introduse de la tastatură. Opțional,
puteți lăsa utilizatorul să continue și să mai introducă numere, pînă alege
să iasă din program.

U2P10. **Indicatorul lui Euler** (eng. *Euler's totient function*):
Fie `n` un număr întreg pozitiv. Se definește `phi(n)` ca fiind
numărul de numere strict mai mici decît `n`, coprime cu `n`.
Mai precis, `phi(n) = card({0 < x < n | cmmdc(x, n) = 1})`.
În particular, dacă `n` este prim, `phi(n) = n-1`.

Calculați indicatorul lui Euler pentru un număr introdus de la tastatură.
Cu alte cuvinte, utilizatorul introduce `n`, iar programul afișează `phi(n)`.