import random
print("Enter No. Of Names!")
n = int(input())
ls=[None]*n
for u in range(n):
	ls[u]=u
for i in range(n):
	print(f"Enter {i+1} Name:")
	temp=input()
	ls[i]=temp
fn=[None]*n
ln=[None]*n
for j in range(n):
	l=ls[j].find(" ")
	t=ls[j]
	fn[j]=t[:l:]
	ln[j]=t[l::]
print("And The New Names Are!")
for a in range(n):
	temp1=random.choice(fn)
	temp2=random.choice(ln)
	temp3=temp1+temp2
	print(temp3)