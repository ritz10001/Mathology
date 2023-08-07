class ArithmeticOperations:
    def __init__(self):
        pass
    def addition(self,*args):
        if len(args)>1:
            sum = 0
            for i in args:
                if type(i)==int or type(i)==float:
                    sum += i
                else:
                    print("Cannot perform arithmetic operations on non-numeric value(s)!")
                    return "\033[F"
            return sum
        else:
            return args[0]
    def subtraction(self,*args):
        if len(args)>1:
            difference = args[0]
            for i in range(1,len(args)):
                if type(args[i])==int or type(args[i])==float:
                    difference -= i
                else:
                    print("Cannot perform arithmetic operations on non-numeric value(s)!")
                    return "\033[F"
            return difference
        else:
            return args[0]
    def multiplication(self,*args):
        if len(args)>1:
            product = 1
            for i in args:
                if type(i)==int or type(i)==float:
                    product *= i
                else:
                    print("Cannot perform arithmetic operations on non-numeric value(s)!")
                    return "\033[F"
            return product
        else:
            return args[0]
    def division(self,*args):
        if len(args)>1:
            quotient = args[0]
            for i in range(1,len(args)):
                if type(args[i])==int or type(args[i])==float:
                    try:
                        quotient /= args[i]
                    except ZeroDivisionError:
                        print("Cannot divide by zero!")
                else:
                    print("Cannot perform arithmetic operations on non-numeric value(s)!")
                    return "\033[F"
            return quotient
        else:
            return args[0]
    def exponentiation(self,*args):
        if len(args)>1:
            power = args[0]
            for i in range(1,len(args)):
                if type(args[i])==int or type(args[i])==float:
                    power **= args[i]
                else:
                    print("Cannot perform arithmetic operations on non-numeric value(s)!")
                    return "\033[F"
                   
            return power
        else:
            return args[0]