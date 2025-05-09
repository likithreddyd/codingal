num=int(input("Enter single input: "))
print("----Tabel of",num,'----')
for i in range(1,11):
    print(num,"x",i,"=",num*i)

num=int(input("Enter single input: "))
print("----Power Tabel of",num,'----')
for i in range(1,11):
    print(num,"is",i,"square is",num**i)

for i in range(1,31):
    square = i**2
    print(f"{i} ---->{i**2}")

for i in range(1,31):
    cube = i**3
    print(f"{i} ---->{cube}")

print("...power of four....")

for i in range(50,101):
    print(f"power of four {i} is {i**4} ")

#Practice

print("......power of five......")

for i in range(200,300):
    print(f"power of five {i} is {i**5}")

print("......power of six......")

for i in range(100,200):
    print(f"power of six {i} is {i**6} ")


#Nested Loop

for i in range(20):
    for j in range(30):
        print("i: ",i, "j: ",j)




