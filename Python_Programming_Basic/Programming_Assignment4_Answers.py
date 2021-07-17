1.Write a Python Program to Find the Factorial of a Number?
Answer1:
def factorial_value(num):
    """
    This function calculates the factorial of the number passed and returns the factorial value
    :param num: Any positive number or 0
    :return: result = calculated factorial value
    :rtype: int
    """
    try:
        if num == 0 or num == 1:
            return 1
        else:
            result = 1
            for i in range(1, num+1):
                result = result * i
            return result
    except Exception as e:
        return e


number= int(input("Enter the number for which you want to find the factorial : "))
answer = factorial_value(number)
print("{}! is {}".format(number, answer))


2.Write a Python Program to Display the multiplication Table?
Answer2:
number = int(input("Enter the number for which you want to display the multiplication table : "))
try:
    print("Multiplication table of {} is below".format(number))
    for i in range(1, 11):
        result = number * i
        print("{} * {} = {}".format(number, i, result))
except Exception as e:
    print(e)


3.Write a Python Program to Print the Fibonacci sequence?
Answer3:
def fib_sequence(n):
    """
    This function takes a positive integer 'n' and returns the first n number of fibonacci numbers
    :param n: A positive integer
    :return: returns a fibonacci sequence
    """
    fib1 = 0
    fib2 = 1
    try:
        if n <= 0:
            print("Enter a number greater than 0")

        elif n == 1:
            return 0

        else:
            fibseq = [fib1, fib2]
            for i in range(1, n-1):
                fib = fib2 + fib1
                fib1 = fib2
                fib2 = fib
                fibseq.append(fib)
            return fibseq
    except Exception as e:
        return e


num = int(input("Enter the number : "))
fib_seq = fib_sequence(num)
print("The first {} fibonacci series numbers are {}".format(num, fib_seq))


4.Write a Python Program to Check Armstrong Number?
Answer4:
def arm_number(n):
    """
    This function take a number n and returns the sum of cube of the digits in the number.
    e.g if the number is 123, the return value is 36(1 ** 3 + 2 ** 3+ 3 **3).
    :param n: any integer
    :return: sum of cube of the digits in the number
    """
    try:
        if n == 0 or n ==1:
            return n
        else:
            total = 0
            for i in str(n):
                total = total + int(i) ** 3
            return total
    except Exception as e:
        return e


armstrong = int(input("Enter the number to check : "))
result = arm_number(armstrong)
if result == armstrong:
    print("{} is an armstrong number".format(armstrong))
else:
    print("{} is not an armstrong number".format(armstrong))



5.Write a Python Program to Find Armstrong Number in an Interval?
Answer5:
def arm_number(n):
    """
    This function take a number n and returns the sum of cube of the digits in the number.
    e.g if the number is 123, the return value is 36(1 ** 3 + 2 ** 3+ 3 **3).
    :param n: any integer
    :return: sum of cube of the digits in the number
    """
    try:
        if n == 0 or n ==1:
            return n
        else:
            total = 0
            for i in str(n):
                total = total + int(i) ** 3
            return total
    except Exception as e:
        return e


lower_limit = int(input("Enter the lower limit of the interval : "))
higher_limit = int(input("Enter the higher limit of the interval : "))
armstrong_list = []
for j in range(lower_limit, higher_limit+1):
    result = arm_number(j)
    if result == j:
        armstrong_list.append(result)
if len(armstrong_list) != 0:
    print("The armstrong numbers between {} and {} are {}".format(lower_limit, higher_limit, armstrong_list))
else:
    print("There are no armstrong numbers between {} and {}".format(lower_limit, higher_limit))


6.Write a Python Program to Find the Sum of Natural Numbers?
Answer6:
numbers = input("Enter the numbers to add separated bu comma(,) : ")
total = 0
try:
    for i in numbers:
        if i == ",":
            continue
        else:
            total = total + int(i)
    print("the sum of {} is {}".format(numbers, total))
except Exception as e:
    print(e)