# Laborator 3: Teste de primalitate

## Introducere și teorie
Testarea primalității unor numere este o procedură dificilă, în general,
tocmai pentru că nu se cunoaște nicio metodă de a găsi sau a genera
*toate* numerele prime.

De aceea, în unele situații, este mai eficient să aplicăm teste *probabilistice*.
Avantajul lor este că pot da ușor un răspuns negativ, adică dacă numărul *nu*
este prim. Dar dacă este prim, oferă doar rezultat probabilistic,
adică faptul că *este posibil* să fie prim, conform cîtorva teste
(la alegerea utilizatorului).

Evident, cea mai simplă este verificarea directă, de forma:

```python
# Python
def estePrim(n):
	for i in range(2, sqrt(n) + 1):
		if n % i == 0:
			return 0
	return 1

numar = int(input("Introduceți un număr: "))
if estePrim(numar):
	print(f"Numărul {numar} este prim.")
else:
	print(f"Numărul {numar} nu este prim.")
```

Dar vom vedea și cîteva metode mai mult sau mai puțin eficiente
care să verifice exact sau probabilistic dacă un număr este prim.

## Verificare exactă: Ciurul lui Eratostene
Acest algoritm datează din antichitate și determină cu exactitate
toate numerele prime dintr-un interval dat. Procedura lucrează astfel:

1. Se determină intervalul în care se dorește să se afle numerele prime. Să
presupunem că acest interval este `[1,n]`;
2. Se ia fiecare număr din interval și se elimină multiplii numărului
corespunzător pasului la care ne aflăm, începînd cu 2:
	- la primul pas, se elimină toate numerele pare (în afară de 2);
	- la al doilea pas, se elimină toți multiplii de 3 (cei rămași, în afară de 3);
	- la al treilea pas, se elimină toți multiplii de 4, dar nu au rămas,
	  pentru că au fost eliminați la primul pas;
	- la al patrulea pas, se elimină toți multiplii de 5 (cei rămași, în afară de 5) etc.
3. La final, numerele neeliminate vor fi doar cele prime.

## Verificare exactă: Testul Fermat
Folosind *mica teoremă a lui Fermat*, anume `a^{p-1} = 1 mod p`,
pentru orice `a`, dacă `p` este prim, putem lucra astfel. Dat un număr
natural `n`, putem lucra în `Zn` și să verificăm toate elementele `a`
din `Zn`. Dacă vreunul dintre acestea *nu* returnează `1 mod n`, cînd
este ridicat la puterea `n-1`, atunci `n` nu este prim.

## Verificare probabilistică
Dacă se lucrează cu numere mari, toate testele de mai sus pot deveni probabilistice.
Astfel, se pot lua doar *cîteva* valori pe care să le testăm, la alegerea utilizatorului.
De exemplu, în cazul testului Fermat, dacă vrem să testăm un număr foarte mare `n`, putem
lua doar cîteva valori pentru `a`:

```
Introduceți numărul de testat: 27409
Cîte teste aleatorii se vor face? 20
--------------------------------------------------
Testăm 9731. Rezultat pozitiv.
Testăm 20195. Rezultat pozitiv.
Testăm 13582. Rezultat pozitiv.
Testăm 12102. Rezultat pozitiv.
Testăm 5150. Rezultat pozitiv.
Testăm 1833. Rezultat pozitiv.
Testăm 15410. Rezultat pozitiv.
Testăm 12782. Rezultat pozitiv.
Testăm 14582. Rezultat pozitiv.
Testăm 8594. Rezultat pozitiv.
Testăm 23535. Rezultat pozitiv.
Testăm 21188. Rezultat pozitiv.
Testăm 19470. Rezultat pozitiv.
Testăm 20443. Rezultat pozitiv.
Testăm 21909. Rezultat pozitiv.
Testăm 13679. Rezultat pozitiv.
Testăm 20477. Rezultat pozitiv.
Testăm 25035. Rezultat pozitiv.
Testăm 13726. Rezultat pozitiv.
Testăm 20741. Rezultat pozitiv.
--------------------------------------------------
27409 este probabil prim (Fermat).
```

O listă de numere prime, dacă vreți să verificați numere mai mari, găsiți, de exemplu,
[aici](http://compoasso.free.fr/primelistweb/page/prime/liste_online_en.php).

## Simbolul Jacobi și testul Solovay-Strassen
O funcție foarte importantă din teoria numerelor este **simbolul Jacobi**.
Fie `n` un număr impar și `b` un număr natural oarecare. Se definește simbolul Jacobi,
notat `(b/n)`, astfel:
- dacă `n` divide `b`, atunci `(b/n) = 0`;
- dacă `b mod n` este pătrat perfect în `Zn`, atunci `(b/n) = 1`;
- -1 în rest.

De exemplu:
- `(10/3) = 1`, pentru că `10 mod 3 = 1`, iar `1` este pătrat perfect în `Z3`;
- `(21/3) = 0`, pentru că `3 | 21`;
- `(14/33) = -1`, pentru că 33 nu divide 14, iar 14 nu e pătrat perfect în `Z33`.

Un tabel cu mai multe valori găsiți [aici](https://en.wikipedia.org/wiki/Jacobi_symbol#Table_of_values).

Testul Solovay-Strassen se bazează pe următoarea teoremă:

> Dacă `n` e număr prim, atunci pentru orice `b` din `Zn`,
> are loc `b^{(n-1)/2} = (b/n) mod n`.

Astfel, pentru implementare, trebuie să:
1. Citim `n`;
2. Pentru toți `b` din `Zn`, calculăm simbolurile Jacobi `(b/n)` și expresia `b^{(n-1)/2}`;
3. Dacă cele două sînt egale în `Zn` pentru un același `b`, rezultă că `n` este prim.

**Observație:** Ca și în cazurile de mai devreme, testul Solovay-Strassen poate fi
implementat exact sau probabilist.

## Exerciții
- ușoare [aici](./usor.md)
- medii [aici](./mediu.md)