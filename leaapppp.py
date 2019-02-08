while True:
	try:
		sam=int(input())
		break
	except:
		print("invalid input")
		break
if sam%400==0 or sam%4==0 and sam%100 !=0:
	print("yes")
else:
	print("no")
