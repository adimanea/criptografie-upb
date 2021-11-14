# Cifruri flux și pe blocuri

Prin definiție, un algoritm criptografic *flux* (eng. *stream cypher*)
este un algoritm care lucrează cu textul clar caracter cu caracter.

Un algoritm criptografic *pe blocuri* (eng. *block cypher*) este unul care împarte
textul clar în blocuri de lungime fixată și tratează fiecare bloc diferit.

În unele cazuri, se poate aplica și *padding*, adică se adaugă caractere aleatorii
sau unele fixate (e.g. zerouri) dacă lungimea textului clar nu se împarte exact
la lungimea blocurilor.

De exemplu, dacă avem cuvîntul clar `CRIPTOGRAFIE` și vrem să-l cifrăm prin metoda flux,
se aplică algoritmul de criptare ales pe fiecare dintre caractere, pe rînd.

Dacă același cuvînt vrem să-l criptăm pe blocuri, să spunem cu lungimea blocului `b = 3`,
atunci se împarte cuvîntul în blocuri de lungime 3, `CRI, PTO, GRA, FIE` și se aplică
algoritmul sau algoritmii pe fiecare dintre blocuri. Se pot aplica chiar și algoritmi 
diferiți pentru fiecare bloc.

Dacă lungimea blocului ar fi fost `b = 5` și presupunem că folosim padding cu caractere
aleatorii, am avea blocurile `CRIPT, OGRAF, IE`, dar ultimul bloc trebuie mărit,
deci avem `CRIPT, OGRAF, IEXAT`, de exemplu (am aplicat 3 caractere aleatorii).

## Convenții generale
Pentru simplitate, vom folosi următoarele convenții generale:

1. Vom presupune că lucrăm doar cu mesaje alcătuite din caractere din alfabetul englezesc. Așadar, nu vom cripta (vom ignora) diacriticele sau semnele de punctuație. Dacă un cuvînt conține spații, puteți alege dacă le respectați sau le ignorați, adică dacă apar și în mesajul cifrat sau nu.
2. Vom lucra, *preferabil* cu pozițiile în alfabet (zero-indexate!) ale literelor unui mesaj, pentru a le transforma în numere. De exemplu, cuvîntul `MAMA` devine lista de numere `[12, 0, 12, 0]`. Matematic, vom lucra în `Z26`.

Pentru referință, puteți folosi tabelul:
```
A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W	X	Y	Z
0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25
```

**Observație:** Dacă preferați, puteți lucra și cu punctuație și cu coduri ASCII în loc de pozițiile din alfabet. Dar, în general, problemele vor fi mai grele în acest caz.

## Cifrul Caesar
Unul dintre primele exemple de cifruri a fost un *cifru de substituție*, în care literele
din mesajul clar sînt înlocuite 1-1 cu altele, obținute după o anumită procedură.
Matematic, modelăm acest cifru astfel:

**Varianta flux**:
- se citește de la tastatură un cuvînt sau un mesaj, să zicem în variabila `clar` (de tip `string`);
- se citește de la tastatură o cheie de criptare, să zicem în variabila `k`;
- pentru fiecare caracter din `clar`, se asociază poziția în alfabet și se obține un vector de `int`, să zicem în variabila `pozitii_clar`, care are lungimea egală cu `strlen(clar)` și elementele sale vor fi de la 0 la 25;
- pentru fiecare `0 <= i <= strlen(clar)`, se modifică elementele vectorului astfel `pozitii_clar[i] = (pozitii_clar[i] + k) % 26`;
- se recuperează caracterele, astfel că fiecare număr din `pozitii_clar` va reprezenta o poziție din alfabet;
- se alcătuiește textul cifrat folosind aceste caractere, `cod`, care se afișează.

Exemplu:
```
clar = laborator
k = 3
pozitii_clar = [11, 0, 1, 14, 17, 0, 19, 14, 17]
pozitii_clar = [14, 3, 4, 17, 20, 3, 22, 17, 20]
cod = oderudwru
```

**Varianta pe blocuri, fără padding**:
- se citește de la tastatură `clar`;
- se citește lungimea blocurilor `b`;
- se citește *vectorul de chei*, de lungime `b`, `chei[]`;
- se împarte `clar` în blocuri de lungime `b`, de exemplu în `bloc[]`, care este un vector de `string`;
- fiecare `bloc[i]` se cifrează folosind `chei[i]`;
- se recompune mesajul final și se afișează.

Exemplu:
```
clar = laborator
b = 5
chei[] = [5, 11]
bloc[] = [labor, ator]
pozitii_clar = [[11, 0, 1, 14, 17], [0, 19, 14, 17]]
pozitii_clar = [[16, 5, 6, 19, 22], [11, 4, 25, 2]]
cod = [[q, f, g, t, w], [l, e, z, c]]
cod = qfgtwlezc
```

## Cifrul afin
Această metodă funcționează similar cu cifrul Caesar, doar că în loc să se facă criptarea
folosind o singură cheie, prin translație, `clar = clar + k`, acum se folosesc 2 chei
și se aplică o omotetie, adică o funcție de gradul 1: `clar = k1 * clar + k2`.

Exemplu:
```
clar = joi
k1 = 5
k2 = 7
pozitii_clar = [9, 14, 8]
pozitii_clar = [0, 25, 21]
cod = azv
```

Ca și în cazul cifrului Caesar, și cifrul afin se poate aplica în metoda flux sau pe blocuri.
În varianta pe blocuri, avem nevoie de atîtea perechi de chei `(k1, k2)` cîte blocuri folosim.


## Cifrul Hill (matrice de criptare)
În această metodă, vectorul `pozitii_clar` din contextul de mai sus este gîndit ca o matrice-coloană.
Se generează aleatoriu (sau se dă) o matrice pătratică de lungime `strlen(pozitii_clar)`, cu care
se înmulțește la stînga vectorul `pozitii_clar`, pentru a obține vectorul criptat.

Similar, se poate aplica și varianta pe blocuri, în care se generează cîte o matrice pentru fiecare bloc.

Exemple: vezi în [PDF-ul de la laborator](https://1drv.ms/b/s!AqqJNzpXrVNEjPQwwgOCGqhG1c6yFA?e=SXl5il).

## Cifrul Hill afin
În loc de o matrice, se pot folosi două, astfel că procedura de criptare nu mai înseamnă
doar înmulțirea vectorului `pozitii_clar` cu o matrice pătratică `A`, ci o transformare
liniară (afină), de forma `A * pozitii_clar + B`, unde `A` și `B` sînt matrice de dimensiuni potrivite.

Din nou, se poate aplica fie în varianta flux, fie pe blocuri.

Exemple: vezi în [PDF-ul de la laborator](https://1drv.ms/b/s!AqqJNzpXrVNEjPQwwgOCGqhG1c6yFA?e=SXl5il).

## Cifrul Vernam (`XOR`)
În acest cifru, se convertește fiecare poziție a caracterelor din `mesaj` în binar,
se generează un flux de chei (*keystream*) și se aplică `XOR` (adunarea din `Z2`, practic)
între codurile în binar ale literelor și cheia din flux potrivită.

Concret:
1. Se iau pozițiile din alfabet ale fiecărui caracter din mesaj;
2. Se transformă în binar fiecare dintre aceste coduri;
3. Se generează aleatoriu un keystream în binar, de lungimea mesajului;
4. Se calculează `XOR` între cele două stream-uri;
5. Rezultatul se trece din binar în zecimal și se recuperează caracterele.

Exemplu:
```
Mesajul de criptat: criptografie
Caracterele de criptat:
['c', 'r', 'i', 'p', 't', 'o', 'g', 'r', 'a', 'f', 'i', 'e']
Indicii lor în alfabet:
[2, 17, 8, 15, 19, 14, 6, 17, 0, 5, 8, 4]
Codurile binare ale indicilor:
['0b10', '0b10001', '0b1000', '0b1111', '0b10011', '0b1110', '0b110', '0b10001', '0b0', '0b101', '0b1000', '0b100']
Cheile de criptare (zecimale):
[0, 7, 22, 10, 1, 0, 12, 22, 15, 18, 14, 23]
Cheile de criptare (binare):
['0b0', '0b111', '0b10110', '0b1010', '0b1', '0b0', '0b1100', '0b10110', '0b1111', '0b10010', '0b1110', '0b10111']
Pozițiile criptate:
[2, 22, 4, 5, 18, 14, 10, 7, 15, 23, 6, 19]
Mesajul criptat:
cwefsokhpxgt
```

**Observație:** Dat fiind că lucrăm cu un keystream generat aleatoriu,
este irelevant în acest caz să luăm în considerare varianta pe blocuri.

## Idei generale de îmbunătățire a codurilor
Evident, în practică, algoritmii pe care i-am folosit sînt foarte slabi. Totuși, 
pentru exercițiile de laborator, puteți ține cont de următoarele idei ca să faceți
criptarea și mai „sigură“:
- puteți concatena mesajul de intrare, apoi puteți adăuga un număr aleatoriu de spații libere în mesajul rezultat, pe poziții aleatorii, pentru a da impresia că și mesajul inițial era împărțit în cuvinte. Astfel, dacă avem mesajul `laborator de criptografie`, puteți prelua `laboratordecriptografie`, apoi să presupunem că ați cifrat și rezultă `kshgkczorqdacorujdgfdaa`. Puteți afișa `ksh gkc zorqda corujd gf daa`;
- puteți introduce un număr aleatoriu de majuscule, plasate în poziții aleatorii;
- pentru a face mesajul și mai realist, puteți restricționa ca majusculele să nu apară decît la începutul cuvintelor (ca în numele proprii) sau să aveți întregi cuvinte cu majuscule. De exemplu, ar fi credibil un mesaj ca `AGGAG sdsd Cast asdd gggsa Xasd`, dar nu un mesaj ca `SSGsd MMSqxg asdgSDdsd CCsdLdqD`.

## Generarea cheilor
În practică, se folosesc chei care sînt determinate din proceduri matematice complicate.
Foarte rar se folosesc chei aleatorii. Din nou, pentru simplitate, am omis acest detaliu.
O idee de îmbunătățire pe care o puteți aplica este ca, atunci cînd folosiți
criptarea pe blocuri, să generați aleatoriu doar prima cheie de bloc, apoi celelalte
să fie generate recurent, folosind-o pe anterioara sau pe anterioarele.

De exemplu, dacă cheia pentru blocul 1 este `cb1`, puteți genera cheia pentru
blocul 2 ca fiind `cb2 = cb1 * cb1`, apoi cheia pentru blocul 3 ca fiind `cb3 = cb1 * cb1 + cb2 * cb2` etc.

Pentru acest laborator, cel puțin, aveți libertate totală de a jongla cu asemenea proceduri.
Evident, în viața reală, lucrurile trebuie să se bazeze cît mai puțin pe aleatoriu
și cît mai mult pe rezultate eficiente și demonstrabile.

## Exerciții
- ușoare [aici](./usor.md)
- medii [aici](./mediu.md)