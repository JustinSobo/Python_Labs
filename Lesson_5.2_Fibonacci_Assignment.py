i = int(input("Please enter a positive integer greater than 1: "))

a, b = 1, 1
count = 0

if i <= 0:
   print("Not valid, please enter a positive integer greater than 1")
elif i == 1:
   print("Fibonacci iterations upto",i,":")
   print(a)
else:
   while count < i:
       print(a)
       nth = a + b
       a = b
       b = nth
       count += 1
