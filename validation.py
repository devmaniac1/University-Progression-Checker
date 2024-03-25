def validate(X):
    try:
        X = int(X)
        if X==int(X):
            if X in range(0,120+1,20):
                return True
            else:
                print("Out of Range")
                print("Entry Value Should be 0,20,40,60,80,100 or 120")
                return False
        else:
            return False
    except ValueError:
        print("Enter Only Integers")
        return False


def validateUow(UoW_Num):
    if UoW_Num[:1] == "w" and len(UoW_Num[1:]) == 7 and (UoW_Num[1:].isdigit()):
        return True
    else:
        print("UoW Number Should Contain 'w' followed by 7 digits (eg. w1999414)")
        return False
