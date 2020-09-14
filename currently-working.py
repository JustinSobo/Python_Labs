def isleapyear(mybirthyear):
    if (mybirthyear % 4) == 0:
        if (mybirthyear % 100) == 0:
            if (mybirthyear % 400) == 0:
                x = True
            else:
                x = False
        else:
            x = True
    else:
        x = False
    
mybirthyear = int(input("Enter a year: "))


