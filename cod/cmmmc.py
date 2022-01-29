def cmmdc(a, b):
	while a != b:
		if a > b:
			a -= b
		else:
			b -= a
	return a

a = int(input("Introduceți primul număr: "))
b = int(input("Introduceți cel de-al doilea număr: "))

cmmmc = a * b // cmmdc(a, b)
print(f"cmmmc({a}, {b}) = {cmmmc}")