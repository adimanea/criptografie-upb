# calculează baza ^ exponent modulo modul

baza = int(input("Introduceți baza: "))
exponent = int(input("Introduceți exponentul (puterea): "))
modul = int(input("Introduceți modulul: "))

rez = 1
for t in range(1, exponent + 1):
	rez = (rez * baza) % modul 		# iau modul la fiecare pas!

print(f"{baza}^{exponent} = {rez} mod {modul}")