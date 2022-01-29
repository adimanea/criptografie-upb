n = int(input("Introduceți modulul: "))

# afișez pătratele din Zn

listaPatrate = []
for i in range(1, n):
	if (i*i % n) not in listaPatrate:
		listaPatrate.append(i*i % n)

listaPatrate.sort()

print(f"Pătratele din Z{n}: {listaPatrate}")