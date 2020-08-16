print("Please enter the number of coins: ")
q = int(input("# of quarters: "))
d = int(input("# of dimes: "))
n = int(input("# of nickels: "))
p = int(input("# of pennies: "))

q_value = int(25)
d_value = int(10)
n_value = int(5)
p_value = int(1)

q_total = int(q*q_value)
d_total = int(d*d_value)
n_total = int(n*n_value)
p_total = int(p*p_value)

total = (int(q_total + d_total + n_total + p_total))

dollars = total // 100

remaining_cents = total % 100

print("the total is", dollars, "dollars and", remaining_cents, "cents")
