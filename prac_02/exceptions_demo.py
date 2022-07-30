
numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))


while True:
    if denominator != 0:
        fraction = numerator / denominator
        print(fraction)
        break
    else:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))

print("Finished.")

# 1. ValueError occurs when a non integer value is inputted

# 2. ZeroDivisionError occurs when denominator input is 0

# 3. It is possible

