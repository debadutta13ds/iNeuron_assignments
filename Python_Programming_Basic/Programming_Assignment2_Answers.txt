1.Write a Python program to convert kilometers to miles?
Answer1:
	KiloMeters = input("Enter the Distance in Kilometers : ")
	ConversionRatio = 0.621371
	try:

		Miles = float(KiloMeters) * ConversionRatio
		print("Distance in Miles is : " + str(Miles))
	except Exception as e:
		print(e)



2.Write a Python program to convert Celsius to Fahrenheit?
Answer2:
	Celsius = input("Enter the temperature in celsius. Provide value in integer or float : ")
	try:

		Fahrenheit = (float(Celsius) * 9/5) + 32
		print("Temperature in Fahrenheit is : " + str(Fahrenheit))
	except Exception as e:
		print(e)


3.Write a Python program to display calendar?
Answer3:
	import calendar
	try:
		yy = int(input("Enter a valid year (in integer):" ))
		mm = int(input("Enter a valid month in integer) : "))
		print(calendar.month(yy, mm))

	except Exception as e:
		print(e)


4.Write a Python program to solve quadratic equation?
Answer4:
	import cmath
	try:
		a = int(input("Enter value of a in integer : "))
		b = int(input("Enter value of b in integer : "))
		c = int(input("Enter value of c in integer : "))

		d = (b**2) - (4*a*c)

		s1 = (-b + (cmath.sqrt(d)))/(2*a)
		s2 = (-b - (cmath.sqrt(d)))/(2*a)
		print("Solution to the quadratic equation with the provided values of a as {0} b as {1}, "
			  "c as {2} is {3} and {4}".format(a, b, c, s1, s2))
	except Exception as e:
		print(e)


5.Write a Python program to swap two variables without temp variable?
Answer5:
	var1 = input("Enter First Variable: ")
	var2 = input("Enter Second Variable: ")
	var1, var2 = var2, var1
	print("After Swapping, First Variable is " + var1 + " and Second Variable is " + var2)