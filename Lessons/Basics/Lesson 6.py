#If else statements


a = 5
b = 44
lis = ["Just", "as", "an", "example"]
dic = {
	"This" : "Is",
	"A" : "Dictionary",
	"You" : "Can",
	"Check" : "For",
	"Entries" : "Aswell"
}

if a == 10: #If a is equal to 10 (= is used to assign variables, == is used to compare)
	 print("a is equal to ten") #If true do this code
elif a == 5: #If not true check if a equals 5
	print("a is equal to five")
else: #If none are true
	print("a is not equal to ten or five") #Excecute this code
	
if b > a:
	print("b is bigger than a")
	if b > 20:
		print("it is also bigger than 20")
else:
	print("b is less than a and 20")

if "an" in lis: #If the string an is in the list lis
	print(lis[2])
else: #You dont have to put an else if you dont need to but i needed to teach quickly what pass does
	pass #Tells python to move on 

if "Can" in dic: #TODO work on a better example
	print("An example of using if statements with dictionaries")
else:
	print("No")
