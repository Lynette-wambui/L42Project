#Main way of checking
number = int(input("Enter a number to be checked: "))
if number <= 0:
    print("Please enter a number to check if it armstrong.")

if number%2==0:
        print(number, "is an Armstrong number")
else:
        print(number, "is not an Armstrong number")


num = int(input("Enter number to be checked :"))

flag = False 

if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
if flag:
    print(num, "Is not a prime number")
else:
    print(num, "Is a prime number")




num = 34
print("Table of 34")
for i in range(1,11):
    mul = num*i
    print("34 * %d = %d" % (i,mul))


    num = 1
sum = 0
while(num<=25):
    sum = sum+num
    num = num+1

    print("Sum of the first 25 natural numbers :", sum)

