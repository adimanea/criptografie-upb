# calculează puterile lui g în Zn
# afișează dacă Zn este ciclic

def putereModulara(baza, exponent, modul):
	x = 1
	for i in range(1, exponent + 1): # 1 <= i < exponent + 1
		x = x * baza % modul
	return x

n = int(input("Introduceți modulul, n = "))
g = int(input(f"Introduceți un element din Z{n}, g = "))

listaPuteri = []
for i in range(1, n):
	# listaPuteri = uniq([g, g^2, g^3, ..., g^{n-1}])
	if putereModulara(g, i, n) not in listaPuteri:
		listaPuteri.append(putereModulara(g, i, n))

listaPuteri.sort()

if len(listaPuteri) == n - 1:
	print(f"{g} este generator pentru Z{n}")
	print(f"deci Z{n} este ciclic")
else:
	print(f"{g} nu este generator pentru Z{n}")
	print(f"deci Z{n} NU este ciclic")
	print(f"{g} generează doar {listaPuteri}")