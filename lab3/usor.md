# Exerciții ușoare

U3P1. Citiți de la tastatură `n`, număr natural cel puțin egal cu 1000. Afișați divizorii primi ai lui `n`.

U3P2. Citiți de la tastatură `n`, număr natural cel puțin egal cu 1000. Afișați cel mai mare număr prim care divide `n`.

U3P3. Citiți de la tastatură `n`, număr natural cel puțin egal cu 50. Aplicați ciurul lui Eratostene pentru lista de numere naturale de la 1 la `n`.

U3P4. Implementați testul Fermat exact:
- citiți de la tastatură `n` (nu mai mare decît 1000, pentru eficiență);
- pentru fiecare `1 <= a <= n`:
	+ calculați `t = a^{n-1}`;
	+ calculați `t mod n`:
		* dacă la un anumit pas `t != 1`, afișați `n NU este număr prim, conform testului Fermat.`;
		* `break`;
- dacă nu s-a ieșit din bucla de mai sus, afișați `n este număr prim, conform testului Fermat`.

U3P5. Implementați testul Fermat probabilist, adică aceeași procedură de mai sus, dar utilizatorul alege cîte teste aleatorii se fac:
- citiți `n`;
- utilizatorul alege numărul de teste, `teste`;
- generați o listă de `teste` numere `1 <= a <= n`;
- procedați ca mai sus pentru aceste valori `a`;
- afișați rezultatul pentru fiecare `a` încercat;
- dacă toate testele sînt pozitive, afișați `numărul este PROBABIL prim`;
- dacă există un test negativ, vă opriți și afișați `numărul NU este prim`.

U3P6. Scrieți un program care să citească de la tastatură `b` și `n` și să afișeze simbolul Jacobi `(b/n)`.

U3P7. Scrieți un program care să citească de la tastatură `b` și `n` și să afișeze simbolul Jacobi `(b/n)`,
cu tot cu justificare:
- dacă `n | b`, se afișează cîtul împărțirii lui `b` la `n`;
- dacă `b mod n` este pătrat perfect în `Zn`, se afișează și `sqrt(b)` în `Zn`.