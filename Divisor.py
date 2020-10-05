print("Enter The Number Of Apples You Got!")
apple=input()
if apple.isnumeric()!=True:
	print("I Asked You A Number Damn It!")
else:
	print("Enter Lower Limit")
	mx=input()
	if mx.isnumeric()==False:
		print("Abe Number Likh Apni Crush Ka Nam Nahi!")
	else:
		jx=int(mx)
		print("Enter Upper Limit!")
		nx=input()
		if nx.isnumeric()!=True:
			print("Abe Number Likh Apni Crush Ka Name Nahi!")
		else:
			ox=int(nx)+1
			for i in range(jx,ox):
				if int(apple)%i==0:
					print(f"{i} is a divisor of {apple}")
				else:
					print(f"{i} is not a divisor of {apple}")