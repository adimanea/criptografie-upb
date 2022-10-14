# Supliment matematic: Operații cu clase de resturi

## Teorie
Se va discuta la întîlnire și se va găsi în PDF-ul de notițe (**TBA**).

## Exerciții
### Ecuații algebrice
Rezolvați următoarele ecuații în $\mathbb{Z}_n$, cu $n$ indicat:

1. $3x - 1 = 7$ în $\mathbb{Z}_{11}$.
2. $5x + 2 = 1$ în $\mathbb{Z}_{13}$.
3. $2x + 11 = 3$ în $\mathbb{Z}_{20}$.
4. $5x^2 + 3x + 7 = 1$ în $\mathbb{Z}_{11}$.
5. $x^2 - 2x + 3 = 2$ în $\mathbb{Z}_7$.
6. $4x^2 + 3x - 1 = 5$ în $\mathbb{Z}_{13}$.

### Ecuații logaritmice
Calculați $\log_a(b)$ în $\mathbb{Z}_n$, cu $a, b, n$ indicate:

1. $a = 3, b = 5, n = 7$.
2. $a = 2, b = 5, n = 11$.
3. $a = 6, b = 3, n = 5$.
4. $a = 11, b = 2, n = 17$.
5. $a = 13, b = 5, n = 19$.

### Sisteme liniare
Rezolvați sistemele de ecuații în $\mathbb{Z}_n$, cu $n$ indicat:

1. $3x + 2y = 1$ și $5x - 3y = 2$, cu $n = 7$.
2. $2x - y = 3$ și $-3x + 7y = 1$, cu $n = 11$.
3. $5x - 11y = 2$ și $2x - 7y = 11$, cu $n = 23$.

### Inverse matriceale
Determinați inversele matricelor date (dacă există), cu elemente din $\mathbb{Z}_n$, 
cu $n$ indicat:

$$A = \left( \matrix{1 & -2 & 3 \cr 1 & 1 & 5 \cr 2 & 4 & 0} \right), n = 7$$

$$B = \left( \matrix{1 & 3 & -1 \cr 5 & -2 & 3 \cr -3 & 1 & 0} \right), n = 11$$

$$C = \left( \matrix{-3 & -2 & 0 \cr -5 & 1 & 2 \cr 0 & 2 & 1} \right), n = 10$$

---

## Supliment de programare
Implementați pe computer oricare dintre exercițiile de mai sus.
Unde este cazul, puteți folosi funcții ajutătoare, cum ar fi:
- `inv(a,n) : int`: determină dacă `a` este inversabil modulo `n`;
- `pp(a, n) : bool`: afișează dacă `a` este pătrat perfect modulo `n`;
- `sqrt(a, n) : bool`: calculează radicalul numărului `a` modulo `n` (atenție la precondiții!);
