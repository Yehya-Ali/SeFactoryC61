age = int(input("Enter your age: "))

if age <= 8:
    print("The ticket price is $5")
elif age > 8 and age <= 15:
    print("The ticket price is $10")
else:
    print("The ticket price is $15")