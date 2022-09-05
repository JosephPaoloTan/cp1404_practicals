"""1. Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it."""
user_name = input("Please enter your name: ")
out_file = open('name.txt', 'w')
out_file.write(user_name)
out_file.close()

"""2. Write code that opens "name.txt" and reads the name (as above) then prints,
"Your name is Bob" (or whatever the name is in the file)."""
in_file = open('name.txt', 'r')
name = in_file.read()
print(f"Your name is {name}")
in_file.close()

"""3. Write code that opens "numbers.txt", reads only the first two numbers and adds them together then prints the result."""
in_file = open('numbers.txt', 'r')
first_number = int(in_file.readline())
second_number = int(in_file.readline())
numbers = first_number + second_number
print(numbers)
in_file.close()

"""4. Now write a fourth block of code that prints the total for all lines in numbers.txt or a file with any number of numbers."""
in_file = open('numbers.txt', 'r')
total = 0
for line in in_file:
    number = int(line)
    total += number
print(total)
in_file.close()