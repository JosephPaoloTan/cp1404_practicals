price_of_items = 0

number_of_items = int(input("Number of items: "))

while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

for i in range(number_of_items):
    price_of_items += float(input("Price of item: "))

if price_of_items > 100:
    total_price = price_of_items * (9/10)
    print(f"Total price of {number_of_items} items is ${total_price:.2f}")
else:
    print(f"Total price of {number_of_items} items is ${price_of_items:.2f}")
