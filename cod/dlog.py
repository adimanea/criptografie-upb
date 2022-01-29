def putereModulara(baza, exponent, modul):
	x = 1
	for i in range(1, exponent + 1): # 1 <= i < exponent + 1
		x = x * baza % modul
	return x

# logaritmul discret log_baza(arg) = rezultat (modulo modul)
baza = int(input("Introduceți baza logaritmului: baza = "))
arg = int(input("Introduceți argumentul logaritmului: arg = "))
modul = int(input("Introduceți modulul logaritmului: modul = "))

# calculez toate puterile bazei pînă la modul - 1
for i in range(1, modul):
	if putereModulara(baza, i, modul) == arg:
		print(f"log_{baza}({arg}) = {i} modulo {modul}")
		exit()

print(f"log_{baza}({arg}) modulo {modul} nu există")