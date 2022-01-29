x = int(input("Introduceți numărul de inversat, x = "))
y = int(input("Introduceți modulul față de care se calculează, y = "))

for i in range(1, y):
	if x * i % y == 1:
		print(f"inv({x}) = {i} în Z{y}")
		exit()

print(f"{x} nu e inversabil în Z{y}")