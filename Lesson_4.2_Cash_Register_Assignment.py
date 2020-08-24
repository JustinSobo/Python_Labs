#Gather variable information
item_1 = float(input("Enter price of the first item: "))
item_2 = float(input("Enter price of the second item: "))
club_card = input("Does customer have a club card? (Y/N): ")
tax_rate = float(input("Enter tax rate, e.g. 5.5 for 5.5% tax: "))

#Calculate base price
base_price = float(item_1 + item_2)

#Identify if customer has second item or not
#If yes, then reduce lower item cost by 50%
#Calculate sum
if (item_2 > 0 and item_2 < item_1):
    item_2 = (item_2 / 2)
    items = item_1 + item_2
elif (item_2 > 0 and item_2 > item_1):
    item_1 = (item_1 / 2)
    items = item_1 + item_2
elif (item_2 > 0 and item_1 == item_2):
    item_2 = (item_2 / 2)
    items = item_1 + item_2
elif (item_2 <= 0):
    items = item_1

#Identify if customer has a Club Card
#If yes, reduce overall cost by 10%
if (club_card == "Y" or "y"):
    items = (items * 0.9)
elif (club_card == "N" or "n"):
    items = items

#Calculating tax rate
tax_rate = float(tax_rate / 100) + 1

#Display base price
print("Base price =", "%.2f" % base_price)

#Display price after discounts
print("Price after discounts =", "%.2f" % items)

#Displaying total price
print("Total price =", "%.2f" % (items * tax_rate))
