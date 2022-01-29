x = int(input("Introduceți numărul de aflat ordin, x = "))
y = int(input("Introduceți modulul față de care se calculează ordinul, n = "))

def putereModulara(baza, exponent, modul):
	"""Returnează baza ^ exponent % modul"""
	rez = 1
	for t in range(1, exponent + 1):
		rez = (rez * baza) % modul 		# iau modul la fiecare pas!
	return rez

for i in range(1, y):
	if putereModulara(x, i, y) == 1:
		print(f"ord({x}) = {i} în Z{y}")
		exit()

print(f"ord({x}) = inf în Z{y}")