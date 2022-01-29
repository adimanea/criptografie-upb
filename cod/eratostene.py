# Ciurul lui Eratostene

# citesc maximul
n = int(input("Introduceți capătul: "))

# generez o listă de numere de la 2 la n
lista = []
for i in range(2, n+1):
	lista.append(i)

# index =  0, 1, 2, 3, ..., n-2
# lista = [2, 3, 4, 5, ..., n  ]

# iau toți multiplii din listă și-i fac 0
for elt in lista:
	if elt != 0:
		for x in range(elt * 2, n + 1, elt):
			lista[x - 2] = 0

for elt in lista:
	if elt == 0:
		print("x ", end="")
	else:
		print(elt, end=" ")

prime = [t for t in lista if t != 0]
procentPrime = len(prime)/len(lista)

print()
print(f"{round(procentPrime * 100,2)}% sînt numere prime din {len(lista)}")