def gcd(first, second) :
	small = min(first, second)
	for i in range(1, small + 1) :
		if first % i == 0 and y % i == 0 :
			gcd = i
	print(gcd)
	return gcd

x = int(input("Enter first"))
y = int(input("Enter second"))

gcd(x, y)