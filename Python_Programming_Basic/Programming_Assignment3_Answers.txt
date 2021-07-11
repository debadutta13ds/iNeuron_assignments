1.Write a Python Program to Check if a Number is Positive, Negative or Zero?
Answer1:
	try:
		num = int(input("Enter the number to check : "))

		if num == 0:
			print("{} is zero".format(num))
		elif num/-1 > num:
			print("{} is negative".format(num))
		else:
			print("{} is positive".format(num))

	except Exception as e:
		print(e)

2.Write a Python Program to Check if a Number is Odd or Even?
Answer2:
	try:
		num = int(input("Enter the number to check : "))

		if num % 2 == 0:
			print("{} is Even".format(num))
		else:
			print("{} is Odd".format(num))

	except Exception as e:
		print(e)

3.Write a Python Program to Check Leap Year?
Answer3:
	try:
		year = int(input("Enter the year to check : "))

		if year % 4 == 0:
			print("{} is leap year".format(year))
		else:
			print("{} is not a leap year".format(year))

	except Exception as e:
		print(e)


4.Write a Python Program to Check Prime Number?
Answer4:
	Prime_Flag = 0
	try:
		num = int(input("Enter the number to check : "))
		if num == 0 or num == 1:
			print("{} is not a prime number".format(num))
		elif num == 2:
			print("{} is a prime number".format(num))
		else:
			for i in range(2, num-1):
				if num % i == 0:
					print("{} is not a prime number".format(num))
					Prime_Flag = 1
					break
		if Prime_Flag == 0:
			print("{} is a prime number".format(num))

	except Exception as e:
		print(e)


5.Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
Answer5:

def prime_in_interval(number):
    """
    This function takes a positive number greater than 1 as input and returns a list containing
    the prime numbers till the number entered.

    :rtype: object
    """
    try:
        prime_list = []
        if number == 2:
            return 2
        else:
            for i in range(2, number):
                prime_flag = 0
                for j in range(2, i):
                    if i % j == 0:
                        prime_flag = 1
                        break
                if prime_flag == 0:
                    prime_list.append(i)
            return prime_list
    except Exception as e:
        return e


answer = prime_in_interval(10000)
print("The prime numbers till 10000 are {}".format(answer))
