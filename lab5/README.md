# Algoritmii Diffie-Hellman, El Gamal și RSA

Algoritmii criptografici se bazează pe probleme de aritmetică dificile,
în primul rînd din punct de vedere computațional. Cu alte cuvinte, se lucrează
cu numere mari sau sînt foarte multe cazuri de analizat sau pur și simplu
procedurile în sine au o complexitate foarte mare din punctul de vedere al
calculelor implicate.

Algoritmii pe care îi prezentăm astăzi, Diffie-Hellman, El Gamal și RSA se bazează,
respectiv, pe *problema logaritmului discret* și pe *problema factorizării*.
Vom explica, pe scurt, aceste probleme și vom justifica de ce sînt ele dificile,
apoi vom vedea cum se implementează la nivel elementar algoritmii respectivi.

## Problema logaritmului discret
Prin definiție, logaritmul unui număr `a` într-o anume bază `b` este exponentul
la care trebuie ridicată baza `b` pentru a obține `a`. Cu alte cuvinte,
logaritmul tratează *probleme de exponețiere*, de ridicare la putere, ceea ce
face ca numerele implicate să fie, de cele mai multe ori, foarte mari.
În plus, dacă ar fi să lucrăm cu funcția logaritmică *reală*, am ajunge la
numere de tip `float`, extrem de greu de gestionat.

De aceea, problema logaritmului discret se formulează într-un context modular,
adică în inele de forma `Zn`. Definiția se păstrează și putem scrie:

```
log_b(a) = c <=> b^c = a în Zn
```

Altfel spus, `log_b(a) = c` dacă și numai dacă, după ce ridicăm `b` la puterea
`c` și luăm restul împărțirii la `n`, obținem exact `a`.

Însă problema logaritmului discret este dificilă pentru faptul că sînt destule
cazuri cînd aceasta nu are soluție. Ca punct de pornire, ne putem gîndi la
pătratele perfecte din `Zn`. De pildă, pentru `n = 5`, pătratele din `Z5`
sînt `{0, 1, 4}`, deci niciun număr la pătrat nu poate da `2` sau `3`.
Acest lucru face imposibil calculul `sqrt(2)` sau `sqrt(3)` în `Z5`.

Din fericire, un caz particular al **teoremei lui Lagrange** ușurează 
căutările logaritmilor:

> Într-un grup finit cu `n` elemente, orice element al grupului ridicat
> la puterea `n` dă elementul neutru.

În `Zn`, acest lucru se scrie `a^n = a`, pentru orice `a` din `Zn`.

Rezultă de aici că, dacă vrem să aflăm, de exemplu, `log_3(5)` în `Z7`,
deci ne interesează la ce putere trebuie ridicat `3` pentru a obține `5 mod 7`,
este suficient să calculăm `3^1, 3^2, 3^3, ..., 3^7 = 1`. Dacă niciuna
dintre valori nu este 5, am terminat, problema nu are soluție.

Vă puteți ajuta de [acest calculator](https://www.alpertron.com.ar/DILOG.HTM) pentru logaritmul discret.

Acum să vedem cum se foloseste acest concept în algoritmul Diffie-Hellman.

## Diffie-Hellman
Algoritmul lui Whitfield Diffie și Martin Hellman se folosește, de obicei,
pentru [schimbul de chei](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange) la inițierea unei comunicări. De pildă, în cazul
autentificării reciproce cînd se accesează un server.

Procedura este următoarea. Presupunem că Alice și Bob vor să stabilească
un canal de comunicare.

1. Alice alege o cheie privată, `a`;
2. Bob alege o cheie privată `b`;
3. Se alege un număr prim mare, `p` și un întreg aleatoriu `alpha`, care se pot face publice;
4. Alice calculează cheia sa publică `A`, după formula `A = alpha^a mod p`, pe care o transmite lui Bob;
5. Bob calculează cheia sa publică `B`, după formula `B = alpha^b mod p`, pe care o transmite lui Alice;
6. Se poate obține o cheie comună (*shared key*) `K`, pe care Alice o calculează prin `K = B^a mod p`, iar Bob o calculează prin `K = A^b mod p`. Rezultate matematice ne asigură că cele două valori coincid;
7. Cheia `K` astfel obținută poate fi folosită pentru a comunica prin orice metodă doresc. De exemplu, se poate folosi pentru criptare Caesar, i.e. translație cu `K` elemente a literelor dintr-un mesaj.

Mai multe detalii [aici](https://medium.com/loopring-protocol/learning-cryptography-diffie-hellman-key-exchange-discrete-log-problem-cyclic-groups-28703f3d5a48), de exemplu. Dar pentru scopul acestui laborator,
procedura de mai sus este suficientă.

## Generatori și grupuri ciclice
În pregătire pentru algoritmul El Gamal, avem nevoie, pe lîngă logaritmul 
discret, și de noțiunile de grupuri ciclice și generatori. Ideea de bază
este aceasta:

> Dacă din puterile unui singur element `g` al unui grup `G` putem obține
> toate elementele grupului, atunci `g` se numește **generator** al grupului
> `G`. Grupul se va numi **ciclic** și acest lucru se notează cu `G = <g>`.

Dar în unele cazuri, nu obținem chiar toate elementele grupului pornind de la
unul singur. Astfel că are sens și noțiunea mai generală de *subgrup ciclic*
generat de un anume element. Iată două exemple:

```
Fie grupul G = Z5. Calculăm puterile tuturor elementelor sale, să vedem
dacă găsim generatori. Conform teoremei lui Lagrange, ne vom opri la puterea
a patra pentru fiecare element (nu uitați, lucrăm cu înmulțirea, deci cu Z5 - {0}, 
care are 4 elemente). Avem:

1 nu se schimbă, la orice putere
2, 2^2 = 4, 2^3 = 3, 2^4 = 1
3, 3^2 = 4, 3^3 = 2, 3^4 = 1
4, 4^2 = 1, 4^3 = 4, 4^4 = 1

Conform calculelor, am găsit că 2 poate genera toate elementele din Z5 - {0}.
Deci Z5 - {0} = <2>.

Dar și 3 poate, deci Z5 - {0} = <3>, la fel de bine.

Aceste rezultate fac ca Z5 - {0} să fie grup ciclic.

Pe de altă parte, <4> = {1, 4}, deci el generează doar un subgrup ciclic
cu două elemente.
```

Există diverse teoreme și scurtături care să ne asigure dacă un element este
sau nu generator. Dar cel mai simplu este să facem calculul direct și să vedem
dacă obținem toate elementele grupului.

În Python, de exemplu, putem avea:

```python
def putereModulara(a, b, n):
	"""Funcția calculează a^b mod n"""
	x = 1
	for i in range(n):
		x = x * a % n
	return x

def esteGenerator(g, n):
	"""Funcția verifică dacă g este generator pentru Zn"""
	listaPuteri = []
	for i in range(1, n):
		if putereModulara(g, i, n) not in listaPuteri:
			listaPuteri.append(putereModulara(g, i, n))
	if len(listaPuteri) == n - 1:
		return 1
	else:
		return 0
```

### Algoritmul El Gamal
Acest algoritm are 3 etape:

1. Generarea cheii;
2. Algoritmul de criptare;
3. Algoritmul de decriptare.

Presupunem că Alice vrea să comunice cu Bob. Se alege un număr prim mare, `p`,
iar toate calculele se vor face modulo `q`, deci în `Zq - {0}`.

**Generarea cheii**:
- Alice alege un _grup ciclic_ `G`, de ordin `q - 1`, cu un generator `g`. Fie `e` elementul
  neutru al acestui grup.
- Alice alege un întreg aleatoriu `x` din `{1, 2, ..., q - 1}`;
- Alice calculează `h = g^x mod q`;
- *Cheia publică* este `PuK = (G, q, g, h)`, iar *cheia privată* este `PrK = x`.

**Criptarea**:
- Bob alege un mesaj `M`, pe care îl transformă într-un element `m` al lui `G`, folosind o *transformare reversibilă*;
- Se alege un întreg aleatoriu `y` din `{1, 2, ..., q - 1}`;
- Bob calculează `s = h^y mod q`, numit *secretul public*;
- Bob calculează `c1 = g^y mod q` și `c2 = m * s`;
- *Cifrul* transmis de Bob este perechea `(c1, c2)`.

**Decriptarea**:
- Alice calculează `s = c1^x mod q = h^y mod q`;
- Alice calculează inversul lui `s` în `G`;
- Alice calculează `m = c2 * s^{-1}`, apoi îl transformă în `M`, folosind inversa transformării folosite de Bob.

## Problema factorizării
Această problemă este, pe cît de simplu de formulat, pe atît de complicat de
rezolvat. În forma elementară, se dă un număr `N` și se cere descompunerea sa
în factori primi. Dacă `N` este foarte mare, procedura este extrem de dificilă
computațional. În cazul algoritmului RSA, de exemplu, care este considerat
suficient de sigur, se folosesc numere de cel puțin 600 de cifre. Mai mult, 
în cazul RSA este suficient să se folosească numere de forma `N = p * q`, unde
`p` și `q` sînt prime foarte mari. Chiar și în acest caz, descompunerea este
foarte dificilă.

## Indicatorul lui Euler
Pentru un număr natural `n`, se definește *indicatorul lui Euler*, `phi(n)`
(numit, în engleză, *Euler's totient function*) ca fiind numărul de numere
mai mici decît `n` și coprime cu `n`. În simboluri:

```
phi(n) = #{0 < x < n | (x, n) = 1}
```

Am folosit notația `#{...}` pentru cardinalul unei mulțimi și `(x, n) = cmmdc(x, n)`.

De exemplu, `phi(10) = 4`, pentru că numerele `{1, 3, 7, 9}` sînt coprime cu `10`.

Ca o scurtătură importantă, dacă `p` este prim, atunci `phi(p) = p - 1`, pentru
că toate numerele mai mici decît `p` vor fi coprime cu el. 

Așadar, de exemplu, `phi(13) = 12`, `phi(5) = 4` etc.

În plus, *funcția `phi` este multiplicativă*, deci `phi(x * y) = phi(x) * phi(y)`.

## RSA
Procedura urmează pașii:

**Alegerea cheilor de criptare:**:
- Alice și Bob aleg două numere prime mari, `p` și `q`;
- Se calculează *modulul de criptare*, `n = p * q`;
- Se calculează `phi(n) = (p - 1) * (q - 1)` (vezi detalii în secțiunea anterioară);
- Se alege un *exponent de criptare* `e`, cu valori în `{3, 4, ..., phi(n) - 1}`,
  dar astfel încît `cmmdc(e, phi(n)) = 1`;
- Se alege un *exponent de decriptare* `d`, astfel încît `d * e = 1 mod phi(n)`;
- *Cheia publică de criptare* este `PuK = (e, n)`;
- *Cheia privată de decriptare* este `PrK = (d, n)`.

**Criptarea mesajelor** Bob -> Alice:
- Bob primește cheia publică de criptare de la Alice, `PuK = (e, n)`;
- Bob alege un mesaj `m` din `{0, 1, ..., n - 1}` pe care vrea să-l trimită;
- Bob calculează `c = m^e mod n`;
- Bon trimite `c` lui Alice.

**Decriptarea mesajelor** de către Alice:
- Alice primește `c`;
- Alice calculează `m' = c^d mod n`, deoarece cunoaște cheia de decriptare `PrK = (d, n)`;
- Se poate demonstra că `m' = m`, deci Alice a realizat decriptarea.