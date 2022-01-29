# afișează lista de pătrate perfecte din Zn

n = int(input("Introduceți n = "))

# list comprehension
# patratePerfecteModN = [(x * x) % n for x in range(1, n)]

patratePerfecteModN = []
for x in range(1, n):
	if ((x * x) % n) not in patratePerfecteModN:
		patratePerfecteModN.append(x * x % n)

patratePerfecteModN.sort()
print(patratePerfecteModN)