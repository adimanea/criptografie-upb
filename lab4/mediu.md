# Exerciții medii

M4P1. Implementați cifrul Caesar pe blocuri, fără padding. Cheile de bloc se citesc de la tastatură.

M4P2. Implementați cifrul Caesar pe blocuri, fără padding, iar cheile de bloc să fie obținute din răspunsurile la întrebări aleatorii. Exemplu:
```
intrebari = ["Culoarea preferată: ", "Orașul nașterii: ", "Numele mamei: ", 
			  "Numele tatălui: ", "Mîncarea preferată: "]
mesaj = criptografie
lungime_bloc = 5
```

Rezultă că avem nevoie de 3 chei de bloc (blocurile fiind `cript`, `ograf` și `ie`).
Aleg aleatoriu 3 întrebări din `intrebari`, iar din răspunsuri, fac cheile,
să zicem luînd ultima literă:

```
Culoarea preferată: albastru // => cheia pentru primul bloc = u = 20
Mîncarea preferată: burger	//  => cheia pentru blocul 2 = r = 17
Orașul nașterii: Iași		//	=> cheia pentru blocul 3 = i = 8
```

M4P3. Implementați cifrul afin pe blocuri. Prima pereche de chei de bloc `(b1k1, b1k2)` se citește
de la tastatură, a doua cheie de bloc se obține din pătratele cheilor anterioare, adică
`(b2k1 = b1k1 * b1k1, b2k2 = b1k2 * b1k2)` etc.

M4P4. Implementați cifrul Vernam, cu keystream-ul generat aleatoriu.

M4P5. Refaceți oricare dintre programele de mai sus, cu spații libere și majuscule introduse *credibil*, adică:
- niciodată să nu apară mai mult de un spațiu liber;
- niciodată să nu apară spațiu liber la începutul sau la finalul mesajului;
- majusculele apar fie la începutul cuvîntului, fie în întregimea cuvîntului.