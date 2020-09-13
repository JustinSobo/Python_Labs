x = input("Enter an odd length string: ")

a = (x[(len(x)-1)//2:(len(x)+2)//2])
b = (x[:len(x)//2])
c = (x[(len(x)+1)//2:])

print("Middle character: " + a)
print("First half: " + b)
print("Second half: " + c)
