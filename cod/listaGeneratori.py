# afișează lista de generatori pentru Zn (dacă există)

def putereModulara(baza, exponent, modul):
	x = 1
	for i in range(1, exponent + 1): # 1 <= i < exponent + 1
		x = x * baza % modul
	return x

def esteGenerator(g, n):
	listaPuteri = []
	for i in range(n):
		if putereModulara(g, i, n) not in listaPuteri:
			listaPuteri.append(putereModulara(g, i, n))
	if len(listaPuteri) == n - 1:
		return True
	else:
		return False

n = int(input("Introduceți modulul, n = "))
listaGeneratori = []
for i in range(1, n):
	if esteGenerator(i, n):
		listaGeneratori.append(i)

if len(listaGeneratori) == 0:
	print(f"Z{n} nu este ciclic, deci nu are generatori")
else:
	print(f"Z{n} este ciclic, generatorii săi sînt {listaGeneratori}")