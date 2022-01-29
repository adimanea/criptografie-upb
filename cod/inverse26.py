x = int(input("Introduceți numărul de inversat: "))
inversabile = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

if x not in inversabile:
	print(f"{x} nu este inversabil")
	exit()

for i in range(1, 26):
	if x * i % 26 == 1:
		print(f"Inversul lui {x} este {i} în Z26")
		exit()