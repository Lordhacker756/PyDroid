import time
print("Hello! There!!")
time.sleep(1)
print("Welcome To My Health Management System!")
time.sleep(1)
x=1
print("What's Your Name?")
name=input()
print("Hello ",  name," Is This Your First Time Here ")
print("Or Have You Been Here Before?")
time.sleep(1)
print("Enter N If You're Here For The First Time ")
print("And Enter E If You've Been Here Before!")
user=input()
print("So! ", name, "Would You Like To Jave A Look At Your Diet Or Exercise Plan?")
time.sleep(1)
print("Or You'd Like To Add The Things You Have Eaten Or Exrcises You Have Done!")
time.sleep(1)
print("Enter L To Have A Look And Enter U To Update Your Plans")
query=input()
if(query== "L" and user == "E" ):
	print("Would You Like To Have A Look At Your Diet Log Or Exercise Log?")
	print("Enter D For Diet And E For Exercise")
	choice=input()
	if(choice=="D"):
		with open("RyaanD.txt") as l:
			l.readlines()
	else:
		with open("RyaanE.txt") as m:
			m.readlines()
elif(query=="U"):
	print("What Would You Like To Log?")
	print("Enter D To Log Diet And Ex To Log Exercise!")
	cho= input()
	if cho == "D":
	   print("Would You Like To Add Multiple Items Or Single Item?")
	   print("Enter M For Multiple S For Single")
	   ec=input()
	   a= open("RyaanD.txt","a")
	   if ec=="S":
	     print("Enter What Have You Eaten")
	     ate=input()
	     a.write(ate)
	   else:
	          while x==1:
	               print("Enter What Have You Eaten")
	               atem=input()
	               a.write(atem)
	               print("Enter y to Enter More Items and e To Exit!")
	               mi=input()
	               if mi == "e":
	               	x=x+1
	else:
	   print("Would You Like To Add Multiple Items Or Single Item?")
	   print("Enter M For Multiple S For Single")
	   ec=input()
	   ae= open("RyaanD.txt","a")
	   if ec=="S":
	     print("Enter What Have You Eaten")
	     exe=input()
	     ae.write(exe)
	   else:
	          while x==1:
	               print("Enter What Have You Done")
	               atem=input()
	               a.write(atem)
	               print("Enter y to Enter More Items and e To Exit!")
	               mie=input()
	               if mie == "e":
	               	x=x+1
	  	
else:
	print("You Don't Have A Previous Record As You're A New User!")
