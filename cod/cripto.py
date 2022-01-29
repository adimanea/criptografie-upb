alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
			'i', 'j', 'k', 'l', 'm', 'n', 'o',
			'p', 'q', 'r', 's', 't', 'u', 'v',
			'w', 'x', 'y', 'z']

plain = input("Introduceți un cuvînt: ")
pozitii = [alfabet.index(x) for x in plain]

k1 = int(input("Prima cheie pentru cifrul afin: "))
k2 = int(input("A doua cheie pentru cifrul afin: "))

pozitiiCod = [(p * k1 + k2) % 26 for p in pozitii]
for p in pozitiiCod:
	print(alfabet[p])