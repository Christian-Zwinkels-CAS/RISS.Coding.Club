#While loops


i = 1
while i < 8: #While x is less than 8 loop through this code
	if i == 6:
		break #Tells python to stop the loop
	print(i)
	i += 1

x = 0
while x < 12:
	x += 2
	if x == 8:
		print("Skips 8")
		continue #Skips when x is 8
	print("X: " + str(x))
else: #When the loop is done do this code
	print("x is now not less than 12")
