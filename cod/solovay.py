# testul Solovay-Strassen

def putereModulara(baza, exponent, modul):
	"""Returnează baza ^ exponent % modul"""
	rez = 1
	for t in range(1, exponent + 1):
		rez = (rez * baza) % modul 		# iau modul la fiecare pas!
	return rez

def jacobi(b, n):
	"""Returnează simbolul Jacobi (b/n)"""
	if (b % n == 0):
		return 0

	patratePerfecteModN = []
	for x in range(1, n):
		if ((x * x) % n) not in patratePerfecteModN:
			patratePerfecteModN.append(x * x % n)
	if (b % n in patratePerfecteModN):
		return 1

	return n - 1

n = int(input("Introduceți numărul de testat, n = "))
while (n % 2 == 0):
	print("Programul lucrează doar cu n număr impar. Reîncercați.")
	n = int(input("Introduceți n = "))

for b in range(1, n):
	if (putereModulara(b, (n-1)//2, n) != jacobi(b, n)):
		print(f"{n} nu este prim, conform Solovay-Strassen")
		print(f"{b} este un martor")
		exit()

print(f"{n} este prim, conform Solovay-Strassen")