# Exerciții medii

M3P1. Se citește de la tastatură un număr natural `n`. Să se afișeze numerele prime consecutive `p` și `q`, din intervalul `[2,n]`, care se află la distanța maximă (adică `|p - q|` are valoarea maximă).

M3P2. Implementați ciurul lui Eratostene, dar fiecare pas să se realizeze cu un delay și să se afișeze treptat. În C++, puteți folosi funcția `sleep()` (dacă folosiți Windows, funcția `Sleep(t)` se găsește în `windows.h`, iar `t` este dat în milisecunde), iar în Python, funcția `sleep(t)` așteaptă `t` secunde.

M3P3. Implementați ciurul lui Eratostene pentru numerele prime pînă la `n`, unde `n` este pătrat perfect și afișați rezultatul într-un tablou, astfel:

```
Introduceți marginea superioară pentru numere prime: 100
2	3	5	7		11      
	13		17	19                      
	23			29	31      
			37		41      
	43		47                                      
	53			59	61      
			67		71      
	73			79                      
	83			89                      
			97
```

Indicație: dacă numărul este prim, se afișează. Altfel, se afișează `\t`, adică `tab` (un alineat).

M3P4. Implementați testul Fermat exact. 
Dacă numărul nu este prim, să se afișeze primul `a` pentru care `a^{n-1} != 1 mod n`.

M3P5. Implementați testul Solovay-Strassen exact.

M3P6. Implementați testul Solovay-Strassen probabilist, lăsînd utilizatorul să aleagă numărul de teste aleatorii.