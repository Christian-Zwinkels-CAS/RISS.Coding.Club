#Working with strings


x = " Hello-World "

print(x.strip()) #Gets rid of empty space at the begining and end of the string
print(x.lower()) #Makes the whole string lower case
print(x.upper()) #Makes the whole string upper case
print(x.replace("H", "Y")) #Replaces the h with a j
print(x.split("-")) #Splits the string using a hyphen as a separator

name = "Christian"
age = 16
a = "My name is {}, and im {} years old" #The curly brakets are placeholders

print(a.format(name, age)) #Fills the placeholders from left to right with these variables
