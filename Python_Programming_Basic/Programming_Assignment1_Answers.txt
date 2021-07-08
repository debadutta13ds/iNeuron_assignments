1. Write a Python program to print "Hello Python"?
Answer1:
	print('"Hello Python"')

2. Write a Python program to do arithmetical operations addition and division.?
Answer2:
	a=10
	b=2
	print(a+b)
	print(a/b)

3. Write a Python program to find the area of a triangle?
Answer3:
	base = float(input("Please enter the length of the base in numeric or float value: "))
	height = float(input("Please enter the length of the height in numeric or float value: "))

	if isinstance(base, float) and isinstance(base, float):
		area = (base * height) / 2
		print(area)
	else:
		print("Please enter both base and height as numeric values")


4. Write a Python program to swap two variables?
Answer4:
	var1 = input("Enter First Variable: ")
	var2 = input("Enter Second Variable: ")
	var3 = ''
	var3 = var2
	var2 = var1
	var1 = var3
	print("After swapping First Variable is " + var1 + " and Second Variable is " + var2)


5. Write a Python program to generate a random number?
Answer5:
	Below program will print a random number between 1 and 100
	
	import random
	print(random.randint(1,100))