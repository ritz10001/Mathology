class PlaceValue:

    def __init__(self):
        pass

    def FindPlaceValue(self,digit,num):
        num = str(num)
        digit = str(digit)
        if len(digit)>1:
            print("Error: Expected single digit to find place value for, received multiple instead!")
            return "\033[F"
        if digit not in num:
            print("Error: Digit to check place value for is not present in number!")
            return "\033[F"
        l = len(num)
        p = 1
        for i in range(-1,-l-1,-1):
            if num[i]==digit:
                return str(p)+"'s place"
            p *= 10
            
    def FindDigitValue(self,place,num):
        for i in str(place)[1::]:
            if i!='0' or str(place)[0]!="1":
                print("Error: Entered place to check for digit is not valid!")
                return "\033[F"
        num = str(num)
        l = len(num)
        if 10**l<=place:
            print("Error: Entered place value is too large for number!")
            return "\033[F"
        p=1
        c=-1
        for i in range(-1,-l-1,-1):
            if p!=place:
                p *= 10
                c-=1
            else:
                return num[c]