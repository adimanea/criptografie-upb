# Exerciții recapitulative

## Temă (Caesar, afin, Hill)

T1. Folosind cifrul Caesar, varianta flux, criptați cuvintele:
	
(a) `RECAPITULARE`, cu cheia `k = 17`;

(b) `LAMULTIANI`, cu cheia `k = 23`;

(c) `SARBATOARE`, cu cheia `k = 19`;

(d) `LUMINITEDECRACIUN`, cu cheia `k = 24`.

La fiecare, verificați rezultatul prin decriptare.


T2. Folosind cifrul Caesar, varianta pe blocuri fără padding, criptați cuvintele:

(a) `CORONAVIRUS`, cu lungimea blocurilor `b = 5` și cheile `k1 = 5`, `k2 = 17`, `k3 = 13`;

(b) `VARIANTAOMICRON`, cu lungimea blocurilor `b = 7` și cheile `k1 = 7`, `k2 = 11`, `k3 = 20`;

(c) `POLITEHNICA`, cu lungimea blocurilor `b = 3` si cheile `k1 = 5`, `k2 = 11`, `k3 = 21`, `k4 = 7`.

La fiecare, verificați rezultatul prin decriptare.

T3. Folosind cifrul afin, varianta flux, criptați cuvintele:

(a) `LAMULTIANI`, cu cheile `k1 = 10` și `k2 = 11`;

(b) `RECAPITULARE`, cu cheile `k1 = 5`, `k2 = 11`;

(c) `TEMACRIPTO`, cu cheile `k1 = 7`, `k2 = 17`.

La fiecare, verificați rezultatul prin decriptare, dacă este posibil. Dacă nu, justificați.

T4. Folosind cifrul afin, varianta pe blocuri fără padding, criptați cuvintele:

(a) `POLITEHNICA`, cu lungimea blocurilor `b = 5` și cheile `k1 = 2`, `k2 = 5`, `k3 = 11`, `k4 = 5`, `k5 = 10`, `k6 = 3`.

(b) `VACANTA`, cu lungimea blocurilor `b = 5` și cheile `k1 = 13`, `k2 = 17`, `k3 = 21`, `k4 = 23`.

(c) `TEMACRIPTO`, cu lungimea blocurilor `b = 7` și cheile `k1 = 17`, `k2 = 7`, `k3 = 11`, `k4 = 15`.

La fiecare, verificați rezultatul prin decriptare, dacă este posibil. Dacă nu, justificați.

T5. Folosind cifrul Hill, varianta flux, criptați cuvintele:

(a) `JOI`, cu matricea de criptare `[1, 5, 1, 2, 0, 3, 5, 0, 2]`;

(b) `PIX`, cu matricea de criptare `[1, 2, 3, 2, 1, 3, 3, 2, 1]`;

(c) `TOP`, cu matricea de criptare `[1, 0, 2, -1, 3, -2, 5, 1, 1]`;

(d) `BEC`, cu matricea de criptare `[1, -1, 1, 2, -2, 2, 3, -3, 3]`.

La fiecare, verificați rezultatul prin decriptare, dacă este posibil. Dacă nu, justificați.


## Modele test: 1 exercițiu pe foaie + 1 pe calculator = 30 min

### Exerciții pe foaie
1. Folosind cifrul Caesar, varianta pe blocuri fără padding, criptați cuvîntul `VINERI`, cu cheia `k = 11`. Verificați rezultatul prin decriptare.
2. Calculați ordinul elementului `x = 3` în `Z7`.
3. Calculați `cmmdc(12, 20, 40)`.
4. Aplicați testul Fermat exact pentru a verifica dacă numărul `x = 9` este prim.
5. Calculați inversa matricei cu 3 linii și 3 coloane `[1, -1, 2, 5, 3, 1, 0, 2, 2]` în `Z7`. Dacă aceasta nu există, justificați.
6. Calculați (dacă există) radical de ordin 4 din 5 în `Z7` și radical de ordin 5 din 4 în `Z7`.

### Exerciții pe calculator
1. Calculați ordinul lui 133 în `Z177`, dacă există.
2. Verificați, folosind testul Fermat probabilist, cu 10 încercări, dacă `x = 133` este prim.
3. Calculați, dacă există, radical de ordin 11 din 1741 în `Z7313`.
4. Citiți de la tastatură `n` și afișați cel mai mare număr prim care se află în intervalul `[n^2, (n + 1)^2]`.
5. Citiți de la tastatură `n` și afișați cel mai mare număr prim care divide `n^2`, dar nu divide `(n + 1)^2`.
6. Scrieți un program care să rezolve, pas cu pas, ecuația `11 * x^2 + 17*x + 131 = 0` în `Z199`: afișați `delta`, afișați `sqrt(delta)` (dacă există; dacă nu, afișați un mesaj sugestiv), afișați soluțiile (dacă există; dacă nu, afișați un mesaj sugestiv).