print("Enter Your List, Enter Done To Finish!")
ls=[]
while True:
	temp=input()
	if temp!="Done":
		if temp.isnumeric()==True:
			ls.append(int(temp))
		else:
			print("Number Pucha Be Hamne, Tumhari Crush Ka Nam Nahi!")
			break
	else:
		break
def rev1():
	ls1=ls.copy()
	ls1.reverse()
	print(ls1)
def rev2():
	ls2=ls.copy()

	print(ls2[::-1])
def rev3():
	l=len(ls)
	ls3=ls.copy()

	if l%2==0:
		for i in range(l//2+1):
			a=ls[i]
			b=ls[l-i-1]
			a , b = b , a
			ls3[i]=a
			ls3[l-i-1]=b
			print(ls3)
	else:
		for i in range(l+1//2):
			a=ls[i]
			b=ls[l-i-1]
			a , b = b , a
			ls3[i]=a
			ls3[l-i-1]=b
	print(ls3)
rev2()
rev3()
rev1()
print("Ho Gaya Bro!! ")