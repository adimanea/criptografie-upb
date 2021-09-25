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
- Pentru studenții avansați, care vor să rezolve inclusiv "complicațiile grafice"
și pe cele statistice, recomand notițele mele de aici: [1](https://github.com/adimanea/fsa-softmat/blob/main/python/6-stat.md), [2](https://github.com/adimanea/fsa-softmat/blob/main/python/3-grafice-discrete.md),
[3](https://github.com/adimanea/fsa-softmat/blob/main/python/3-grafice-discrete.ipynb).

-------------

## Exerciții

G2P1. **Logaritm în `Zn` (aka logaritmul discret)**: Fie `a, b, c, n`
numere naturale. Spunem că `log_a(b) = c` în `Zn` dacă `a^c % n = b`.
Nu orice logaritm se poate calcula în `Zn`, iar procedura este, în general,
foarte dificilă. De aceea, ea stă la baza sistemului criptografic
Diffie-Hellman, utilizat pentru schimbul inițial de chei (vom reveni).

Citiți de la tastatură `a, b, n` și calculați `log_a(b)` în `Zn`, dacă se poate.
Dacă nu se poate, afișați un mesaj corespunzător.

G2P2. **Conjectura lui Collatz (aka 3n+1)** Pentru detalii, vezi mai întîi
problema U2P9 de [aici](usor.md), problema M2P5 de [aici](mediu.md) și 
[pagina Wiki](https://en.wikipedia.org/wiki/Collatz_conjecture).
Cerința este: citiți de la tastatură sau dintr-un fișier o listă de numere
(cel puțin 10) și afișați-l pe acela care necesită cei mai mulți pași
în conjectura lui Collatz, precum și pe cel care necesită cei mai puțini.

*Complicație 1:* Puteți genera numerele de intrare aleatoriu, precum și numărul lor.

*Complicație 2:* Afișați statistici pe baza numerelor de intrare, precum:
- numărul mediu de pași;
- mediana numărului de pași;
- reprezentare grafică (e.g. bar chart/histogram) număr de intrare vs număr de pași.

G2P3. **Numere triunghiulare:** Un număr se numește *triunghiular* dacă se obține
ca o sumă a lui Gauss, adică dacă este egal cu suma tuturor numerelor naturale
de la 1 la un anumit prag. De exemplu, 10 este triunghiular, pentru că
`10 = 1 + 2 + 3 + 4`.

Vom numi *al n-lea număr triungiular* și-l vom nota (neconvențional)
cu `t(n)` numărul `t(n) = 1 + 2 + 3 + ... + n`.

Verificați dacă un număr `n`, introdus de la tastatură, este triungiular.
În caz afirmativ, afișați și al cîtelea număr triunghiular este, adică
`m`, pentru care `t(m) = n`.

G2P4. **[Constanta lui Kaprekar](https://en.wikipedia.org/wiki/Kaprekar%27s_routine)**: Pornim cu un număr de 4 cifre și-l
prelucrăm astfel:
- i se ordonează cifrele crescător, apoi descrescător;
- se scade numărul mai mic din numărul mai mare;
- dacă prima cifră a unuia dintre numere ajunge să fie 0, se acceptă
(e.g. 2450 se transformă în 5420 și în 245, deci scădem 5420 - 245);
- se repetă procedura pentru rezultatul obținut;
- după maximum 8 pași, se ajunge la 6174, după care algoritmul intră în buclă infinită.

Rulați "rutina lui Kaprekar" pentru un număr introdus de la tastatură.

*Complicații*:
- rulați rutina pe un număr aleatoriu de numere aleatorii, citite dintr-un fișier;
- afișați toți pașii intermediari;
- afișați statistici;
- reprezentați grafic aceste statistici;


Rutina funcționează și pentru numere de 3 cifre, caz în care se finalizează cu 495.
Rezolvați exercițiul și pentru acest caz.

G2P5. **Formula lui Euler:** Fie `a` un număr natural și `phi(n)` indicatorul lui Euler
(vezi problema U2P10 de [aici](usor.md)). Formula lui Euler afirmă că `a^phi(n) % n = 1`.
Verificați formula pentru cîteva perechi de numere `(a, n)`, i.e. calculați `phi(n)`
și asigurați-vă că `a^phi(n) % n = 1`.

**Atenție:** Va trebui să faceți calculele modular! Altfel, ridicarea la putere
va ajunge foarte rapid la numere foarte mari!


