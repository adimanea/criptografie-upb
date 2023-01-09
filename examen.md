# Modele de examen (Recapitulare)

**În toate exercițiile de mai jos, se consideră alfabetul cu 26 caractere, plus simbolurile ".", " " și "?", deci calculele pentru cifrurile Caesar, afin și Hill se efectuează în `Z29`.**

## MODEL 1
1. Folosind cifrul Caesar, varianta flux, criptați mesajul `CRIPTOGRAFIE`, cu cheia dată de ultimele 2 cifre din numărul de telefon.
2. Folosind cifrul afin, varianta flux, criptați mesajul `SESIUNE`, cu cheia `k1` dată de ziua de naștere, iar cheia `k2` dată de luna de naștere. Verificați prin decriptare.
3. Folosind cifrul Hill, criptați mesajul `DOI`, cu cheia dată de matricea 

```
[-2 mod 7,      11 mod 5,           -43 mod 5   ]
[-121 mod 7,    152 mod 19,         1737 mod 17 ]
[144 mod 12,    155 mod 3,          -155 mod 3  ]
```

4. Folosind algoritmul Diffie-Hellman, obțineți cheia comună `K` pornind de la `a = 13, b = 6, p = 7, alpha = 10`.
5. Folosind algoritmul RSA, criptați mesajul `m = 4`, pornind cu numerele prime `p = 5, q = 7`.
   

---

## MODEL 2
1. Folosind cifrul Caesar, varianta pe blocuri fără padding, criptați mesajul `INTERNATIONAL`, cu lungimea blocurilor `b = 7` și cheile de bloc `k1 = 141, k2 = 41`.
2. Folosind cifrul afin, varianta pe blocuri fără padding, criptați mesajul `INTERNATIONAL`, cu lungimea blocurilor `b = 5` și cheile de bloc `k1 = 3, k2 = 5, k3 = 1, k4 = 11, k5 = 2, k6 = 31`. Verificați prin decriptare.
3. Folosind algoritmul Diffie-Hellman, obțineți cheia comună `K` pornind de la `a = 10, b = 16, p = 5, alpha = 7`.
4. Folosind algoritmul RSA, criptați mesajul `m = 3`, pornind cu numerele prime `p = 3, q = 11`. Verificați prin decriptare.

---

## MODEL 3
1. Folosind cifrul afin, varianta pe blocuri cu padding, criptați mesajul `EXAMEN`, cu lungimea blocurilor `b = 5` și cheile de bloc `k1 = 3, k2 = 17, k3 = 10, k4 = 11`. Verificați prin decriptare.
2. Folosind cifrul Hill, criptați mesajul `GOL`, cu cheia dată de matricea 

```
[-11 mod 13,    -21 mod 7,      -34 mod 5,] 
[-51 mod 5,     -47 mod 3,      -51 mod 7,]
[-31 mod 7,     -100 mod 10,    -99 mod 2 ]
```

Verificați rezultatul prin decriptare.

3. Folosind algoritmul Diffie-Hellman, obțineți cheia comună `K`, pornind de la `a = 11, b = 10, p = 11, alpha = 6`.
4. Folosind algoritmul RSA, criptați mesajul `m = 5`, pornind cu numerele prime `p = 7, q = 5`.

---

## MODEL 4
1. Folosind cifrul Caesar, varianta pe blocuri cu padding, criptați mesajul `MERDENELE`, cu lungimea blocurilor `b = 7` și cheile de bloc `k1 = 11, k2 = 51`. Verificați prin decriptare.
2. Folosind cifrul Hill, criptați mesajul `YES`, cu cheia dată de matricea 

```
[2^5 mod 3,     5^100 mod 5,    4^20 mod 5,  ] 
[20^20 mod 7,   15^30 mod 3,    17^100 mod 4,]
[7^31 mod 8,    43^73 mod 4,    16^50 mod 63 ]
```

Verificați rezultatul prin decriptare.

3. Folosind algoritmul Diffie-Hellman, obțineți cheia comună `K` pornind de la `a = 10, b = 12, p = 13, alpha = 10`. Folosiți apoi cheia `K` pentru a cripta mesajul `DIFFIEHELLMAN` cu cifrul Caesar, varianta flux și verificați rezultatul prin decriptare.
4. Folosind algoritmul RSA, criptați mesajul `m = 3`, pornind cu numerele prime `p = 3, q = 11`.
5. Folosind algoritmul El Gamal, criptați mesajul `M = 5`, cu `G = Z7`. Alegeți un generator `g` și număr `x`, iar transformarea mesajului `M` este funcția `f(t) = 3t - 1`. Validați datele de intrare și verificați rezultatul prin decriptare.

---

## MODEL 5
1. Folosind cifrul afin, varinta pe blocuri fără padding, criptați mesajul `EXAMEN`, cu lungimea blocurilor `b = 7` și cheile de bloc `k1 = 3, k2 = 61`. Verificați rezultatul prin decriptare.
2. Folosind cifrul Hill, criptați mesajul `NOP`, cu cheia dată de matricea 

```
[-31 mod 5,         14^14 mod 5,        -81 mod 7,  ]
[(-13)^30 mod 17,   13^20 mod 3,        121^7 mod 2,]
[156^13 mod 2       3^100 mod 3,        5^124 mod 6 ]  
```

Verificați rezultatul prin decriptare.

3. Folosind algoritmul Diffie-Hellman, obțineți cheia comună `K` pornind de la `a = 12, b = 16, p = 11, alpha = 7`.
4. Folosind algoritmul El Gamal, criptați mesajul `M = 3` cu `G = Z13`. Alegeți un generator `g` și un număr `x`, iar transformarea mesajului `M` este funcția `f(t) = 5t + 2`. Validați datele de intrare și verificați rezultatul prin decriptare.
5. Folosind algoritmul RSA, criptați mesajul `m = 2`, pornind cu numerele prime `p = q = 5`.