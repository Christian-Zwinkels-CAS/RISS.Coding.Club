#Python collections


ls = ["This", "Is", "a"] #Ordered, changable and allows duplicates
tup = ("This", "is", "a", "tuple") #Odered and not changable
st = {"This", "is", "a", "set"} #Unindexed and unordered


print(ls[1]) #Prints the second item (first value is 0)
print(ls[0:2]) #Prints 1st to 3rd(not included) item
ls[1] = "is" #Chamges the second value to is
print(ls)
ls.append("list") #Adds an item to the end of the list
ls.remove("list") #Removes the item list
ls.insert(3, "list") #Adds it to the 3rd index (this will be the 4th entry)
del ls[1] #Removes the 2nd item
ls2 = ls.copy() #Copy the list to a new list
ls2.extend(ls) #Adds ls to the end of ls2

tup1 = ("add", "me")
tup2 = tup + tup1 #Adds tup1 to the end of tup
print(tup2)

#Only for sets
st.add("placeholder") #Adds this to the end of the set
st.update(["1", "2", "3"]) #Adds more than one item
