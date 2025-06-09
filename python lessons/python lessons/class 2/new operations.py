#operations = == , != , < , > , <= , >= 

print(20 == 20)
print(20==25)

print(20!=25)
print(20!= 20)

print(10<20)
print(20<10)

print(20>23)
print(20>50)

print(20<=20)
print(20<=10)

print(20<=10)
print(15<=20)

x=20
 
x += 20
print(x)

x -= 30
print(x)

x *= 10
print(x)

x /= 5
print(x)

if True:
    print("Akash")
else:
    print("Likith")

if False:
    print("Akash")
else:
    print("Likith")



#Home Work

age =int(input("Enter your age"))

if age >= 18:
    print("you are alegeble to vote")
else:
    print("you are not elegebe to vote")

number=int(input("Enter the number"))
remainder=number%2
print("Remainder:" ,remainder)

if remainder == 0:
    print("the number is even")
else:
    print("the number is odd")

#write a program where we need to check the number is divisiblle by 343 or not

number=int(input("Enter the number"))
remainder=number%343

if remainder == 0:
    print("The num is divisible by 343")
else:
    print("The num is not divisible by 343")

number = int(input("Enter the number"))

remainderby2 = number % 2
remainderby3 = number % 3

if remainderby2 == 0 and remainderby3 == 0:
    print("The number is divisible by 2 and 3")
else:
    print("The number is not divisible by 2 and 3")

number = int(input("Enter the number"))

remainderby2 = number % 2
remainderby3 = number % 3
remainderby10= number % 10

if remainderby2 == 0 and remainderby3 == 0 and remainderby10:
    print("The number is divisible by 2,3 and 10")
else:
    print("The number is not divisible by 2,3 and 10")

y = input("Enter single input: ")

asctiiValue = ord(y)
print(asctiiValue)
