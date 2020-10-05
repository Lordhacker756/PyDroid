import time
print("Hello! I'm Utk And You?")
name=input()
if name.isnumeric()!=True:
	name=name+" "
bol=name.isalnum()
def calc(a):
	hyear=int(a)+100
	print(f"You'll Be A 100 Year Old Guy In The Year {hyear}")
	print("Would You Like To Know Any Particular Year When You'll Be Of \n A Specific Age?")
	time.sleep(2)
	print("Enter \"Y\" To Proceed!")
	choice=input()
	if choice=="Y":
		print("Enter The Age You'll Like To Get The Year Of !")
		age=input()
		if len(age)>2 or len(age)<1 or age.isalnum()== True:
			print("I Think I Asked You Age And It's Not A God Damn Age!!!!")
		else:
			ya=int(a)+int(age)
			print(f"You'll Be {age} Year Old In The Year {ya}")
	else:
		time.sleep(1)
		print("I Asked You Yes or No, Adios!")
if bol == True:
	print("Did Elon Musk Name You?")
	time.sleep(1)
	print("Now Restart The Code XD!")
else:
	print(f"Hello {name} Please Enter Your Age Or Year Of Birth")
	temp=input()
	if len(temp)==4:
		if 2020-int(temp)>90:
			print("C'mon Grandpas Don't Use Python!")
		elif 2020-int(temp)<0:
			print("First Go And Be Born Properly!")
		else:
			calc(temp)
	
	elif len(temp)==2 or len(temp)==1:
		if int(temp)<9:
			print("Really Chigga Pigga?")
		elif int(temp)>90:
			print("Really GrandPa?")
		else:
			byear=2020-int(temp)
			print(byear)
			calc(byear)
	else:
		print("Bhang Khai Ho Ka Chacha?")