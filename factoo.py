def fact(sam):
	if sam == 0:
		return 1
	else:
		return sam * fact(sam-1)
sam=int(input(""))	
print(fact(sam))
