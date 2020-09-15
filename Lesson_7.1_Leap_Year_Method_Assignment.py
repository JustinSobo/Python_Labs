def isleapyear(mybirthyear):
    if (mybirthyear % 4) == 0:
        if (mybirthyear % 100) == 0:
            if (mybirthyear % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

mybirthyear = 1852
if isleapyear(mybirthyear):
    print("Year {0} was a leap year".format(mybirthyear))
