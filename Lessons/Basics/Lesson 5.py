#Dictionaries


GTR_R34 = { #Makes a dictionary
	"Make" : "Nissan", #Sets the entry "Make" to the value "Nissans"
	"Series" : "Skyline",
	"Model" : "R34",
	"Horsepower" : 276,
	"Weight" : 1560,
	"Delete" : "Me"
}

hp = GTR_R34["Horsepower"] #Gets the value of the entry called "Horsepower"
wh = GTR_R34["Weight"]
power = str(round(hp / wh, 2)) + "hp/kg" #Round method here rounds the number to 2 decimal places
print(GTR_R34)
print(power)
GTR_R34["Transmision"] = "6 Speed" #Adds a new entry
print(GTR_R34)
GTR_R34.pop("Delete") #Deletes the specified entry
print(GTR_R34)
