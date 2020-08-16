print("Please enter the amount of money to convert:")
dollars = int(input("# of dollars: "))
remaining_cents = int(input("# of cents: "))

total_cents = dollars * 100 + remaining_cents

q = total_cents // 25
total_cents = total_cents - (q * 25)

d = total_cents // 10
total_cents = total_cents - (d * 10)

n = total_cents // 5
total_cents = total_cents - (n * 5)

p = total_cents // 1
total_cents = total_cents - (p * 1)

print("The coins are", q, "quarters,", d, "dimes,", n, "nickels and", p, "pennies")
