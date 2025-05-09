maths = int(input("Enter your maths marks: "))

science = int(input("Enter your science marks: "))

english = int(input("Enter your english marks: "))

social = int(input("Enter your social marks: "))

hindi = int(input("Enter your hindi marks: "))

#Total 
Total = maths + science + english + social + hindi
print("Total marks:" , Total)

# average

average = Total/3

print(" average marks: ",average)

#percentage
percentage = Total /500 * 100

print(" percentage of marks :",percentage)