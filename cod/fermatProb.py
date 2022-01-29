# implementează testul Fermat probabilist

import random

def putereModulara(baza, exponent, modul):
	rez = 1
	for t in range(1, exponent + 1):
		rez = (rez * baza) % modul 		# iau modul la fiecare pas!
	return rez

n = int(input("Introduceți numărul de verificat: n = "))
teste = int(input("Numărul de teste efectuate: teste = "))

nrTestate = []

# varianta exactă
if teste == n - 1:
	nrTestate = [i for i in range(1, n)]

# varianta probabilistă
else:
	while len(nrTestate) < teste:
		x = random.randint(1, n - 1)
		if x not in nrTestate:
			nrTestate.append(x)

	nrTestate.sort()
	print("Vom testa numerele: ")
	print(nrTestate)
	
# teorema Fermat
for t in nrTestate:
	if putereModulara(t, n - 1, n) != 1:
		print(f"{n} nu este prim; {t} este un martor")
		exit()
	else:
		print(f"Testez {t}. Rezultat pozitiv.")

print(f"{n} este PROBABIL prim (Fermat), probabilitatea = {round(len(nrTestate)/(n-1), 5)}")