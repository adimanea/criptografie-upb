def cmmdc(x, y):
	while x != y:
		if x > y:
			x = x - y
		else:
			y = y - x
	return x

def phi(x):
	nr = 0
	for i in range(1, n):
		if cmmdc(i, x) == 1:
			nr = nr + 1
	return nr

def inversModular(x, n):
	for i in range(1, n):
		if (x * i % n == 1):
			return i

def zeroDivizor(x, n):
	for i in range(1, n):
		if (x * i % n == 0):
			return i

n = int(input("Introduceți modulul, n = "))
while (n <= 0):
	print("Eroare. Introduceți un număr pozitiv!")
	n = int(input("Introduceți modulul, n = "))

x = int(input("Introduceți un număr, x = "))
while (x <= 0):
	print("Eroare. Introduceți un număr pozitiv!")
	x = int(input("Introduceți un număr, x = "))

x = x % n

# dacă x este inversabil
if cmmdc(x, n) == 1:
	print(f"{x} este inversabil în Z{n}")
	print(f"Inversul lui {x} este {inversModular(x, n)}")
else:
# dacă este zero-divizor
	print(f"{x} este zero-divizor în Z{n}")
	print(f"{x} * {zeroDivizor(x, n)} = 0 în Z{n}")

print()
procentInversabile = round(phi(n)/n, 3)
print(f"{procentInversabile * 100} % elemente inversabile în Z{n}")