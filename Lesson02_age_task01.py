age = float(input("What's your age?"))
if age <= 6:
    print("You study at kindergarden")
elif age <= 18:
    print("You study at school")
elif age <= 22:
    print("You study at University")
elif age >= 23:
    print("You already work")
print("Your are " + str(age) + " years old")