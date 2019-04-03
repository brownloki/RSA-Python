'''
def modMulInv(inverse, mod) :
	for i in range(mod) :
		remainder = (inverse * i) % mod
		if remainder == 1 :
			return i
	return 0

inv = int(input("Enter number to find inverse of: "))
modulo = int(input("Enter mudulo: "))

out = modMulInv(inv, modulo)

print(out)

'''

