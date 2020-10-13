date=input()
dict ={
	"January":"1",
	"February":"2",
	"March":"3",
	"April":"4",
	"May":"5",
	"June":"6",
	"July":"7",
	"August":"8",
	"September":"9",
	"October":"10",
	"November":"11",
	"December":"2"
}
if date.find("/")>0:
	ls=date.split("/")
	ls2=ls[1]+"/"+ls[0]+"/"+ls[2]
	print(ls2)
elif date.find(",")>0:
	ls1=date.split(" ")
	temp=ls1[0]
	tempn=dict[temp]
	
	daten=date.replace(",","/")
	
	daten1=daten.replace(" ","/")


	daten2=daten1.replace(temp,dict[temp])

	lseu=daten2.split("/")
	
	datef=lseu[1]+"/"+lseu[0]+"/"+lseu[2]
	print(datef)
	
