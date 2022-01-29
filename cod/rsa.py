# algoritmul RSA
import random

def cmmdc(x, y):
	while x != y:
		if x > y:
			x = x - y
		else:
			y = y - x
	return x

def inversModular(x, n):
	for i in range(1, n):
		if (x * i % n == 1):
			return i
	return -1

def estePrim(p):
	for i in range(2, p // 2 + 1):
		if p % i == 0:
			return False
	return True

def putereModulara(baza, exponent, modul):
	x = 1
	for i in range(1, exponent + 1): # 1 <= i < exponent + 1
		x = x * baza % modul
	return x

print("RSA: Alegerea cheilor...")
p = int(input("Introduceți un număr prim, p = "))
while not estePrim(p):
	print("Numărul introdus nu este prim, reîncercați.")
	p = int(input("Introduceți un număr prim, p = "))
q = int(input("Introduceți un număr prim, q = "))
while not estePrim(q):
	print("Numărul introdus nu este prim, reîncercați.")
	q = int(input("Introduceți un număr prim, q = "))

# modulul de criptare
n = p * q
phi = (p - 1) * (q - 1)

# exponentul de criptare
e = random.randint(3, phi - 1)
while cmmdc(e, phi) != 1:
	e = random.randint(3, phi - 1)

# exponentul de decriptare
d = inversModular(e, phi)

# afișez cheile
print(f"Cheia publică de criptare este PuK = ({e}, {n})")
print(f"Cheia privată de decriptare este PrK = ({d}, {n})")

print()
print("Algoritmul RSA. Criptarea mesajului...")

m = int(input(f"Introduceți mesajul de criptat între 0 și {n-1}, m = "))

# codul
c = putereModulara(m, e, n)
print(f"Codul este {c}")

print()
print("Algoritmul RSA. Decriptarea mesajului...")

mPrim = putereModulara(c, d, n)
if (mPrim == m):
	print(f"Decriptarea este corectă, mesajul este {mPrim}")
else:
	print(f"Eroare!")