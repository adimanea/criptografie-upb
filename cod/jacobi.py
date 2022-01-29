# calculează simbolul Jacobi (b/n)

print("Programul calculează simbolul Jacobi (b/n), cu n impar")
b = int(input("Introduceți b = "))
n = int(input("Introduceți n = "))
while (n % 2 == 0):
	print("Programul lucrează doar cu n număr impar. Reîncercați.")
	n = int(input("Introduceți n = "))

# dacă n | b => (b/n) = 0
if (b % n == 0):
	print(f"({b}/{n}) = 0, pentru că {n} divide {b}")
	exit()

patratePerfecteModN = []
for x in range(1, n):
	if ((x * x) % n) not in patratePerfecteModN:
		patratePerfecteModN.append(x * x % n)
if (b % n in patratePerfecteModN):
	for x in range(1, n):
		if (x * x % n == b):
			print(f"({b}/{n}) = 1, pentru că {b % n} este pătratul lui {x} modulo {n}")
			exit()

print(f"({b}/{n}) = -1, pentru că avem cazul al treilea")