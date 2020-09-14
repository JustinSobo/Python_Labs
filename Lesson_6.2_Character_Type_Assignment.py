# j is a lower case letter.
# 7 is a digit.
# ^ is a non-alphanumeric character.
# C is an upper case letter.

# Assigning list values
lower_Case = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
upper_Case = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
digit = ["0", "1", "2", "3", "4" ,"5" ,"6" ,"7", "8", "9"]

# Setting lengths of list
lower_Len = len(lower_Case)
upper_Len = len(upper_Case)
digit_Len = len(digit)

# Gathering character from user
i = input("Enter a character: ")

# Checking all lists against gathered character from user
if i in lower_Case:
        print(i+" is a lower case letter.")
elif i in upper_Case:
    print(i+" is an upper case letter.")
elif i in digit:
    print(i+" is a digit.")
else:
    print(i+" is a non-alphanumeric character.")
