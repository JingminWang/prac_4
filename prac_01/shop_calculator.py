total_price = 0
number = int(input("Number of items:"))
while number < 0:
    print("Invalid number of items!")
    number = int(input("Number of items:"))
for i in range(number):
    price = float(input("Price of item:"))
    total_price += price
if total_price > 100:
    print("Total price for {} items is ${:.2f}".format(number, total_price * 0.9))
else:
    print("Total price for {} items is ${:.2f}".format(number, total_price))


