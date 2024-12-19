name = input('Your name: ')
print(f"{name.strip()} is Gay")

age = input("How old are you? ")

if age.isdigit() and age >= 18:
    print("Gay")
elif age.isdigit() and age < 18:
    print("Gay is not gay")
else:
    print("Not a number")