import time
with open("Contact.txt","a") as f:
	def AddCont():
		print("Enter Contact Name")
		name=input()
		print("Enter Contact No.")
		num=input()
		if Check(name,num) != "0"
		f.write(name,"/n")
		f.write(num,"/n")
	def Check(a,b):
		while f.readline()!="":
			if f.readline()==a:
			  		if f.readline()==b:
			  			print("The Contact Already Exists")
			  			return 0
			  			break
	def FindCont():
		#This Part Needs Some Debugging!
		print("Enter The Name To Search")
		name=input()
		count=0
		while f.readline()!="":
			if f.readline()==name:
			  		print("The Number Is ",f.readline())
			  		return 1
			  		break
		   else:
			  	return 0
	print("Hello! Welcome To Contacts 2.0")
	time.sleep(1)
	print("So What's Your Name")
	time.sleep(1)
	name=input()
	print(f"So {name} How May I Help You?")
	time.sleep(1)
	print("If You Want To Add A Contact Type 1 \n and if you want to See Details of a contact Type 2")
	time.sleep(2)
	print("Enter Your Choice")
	choice=int(input())
	if choice == 1:
		AddCont()
	else :
		if FindCont() == 0:
			"Sorry The Contact Doesn't Exist"