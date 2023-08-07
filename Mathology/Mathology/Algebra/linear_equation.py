from Mathology.ElementaryMath.arithmetic_operations import ArithmeticOperations
import re
class LinearEquation(ArithmeticOperations):
    def __init__(self):
        pass
    def solve_one_variable(self,equation):
        equation = str(equation) 
        equation = equation.replace(" ","")
        equation += " "
        final_equation = ""
        for i in equation:
            if i=="+" or i=="-" or i=="=":
                final_equation += " "+i+" "
            else:
                final_equation += i        
        s=re.split(r' ',final_equation)
        equation_list = []
        try:
            ind = s.index("=")
        except ValueError:
            print("Error: Invalid Expression, missing '='")
            return "\033[F"
        i = 1
        while i<len(s)+1:
            if i-1<=ind:
                if s[i-1]=="-":
                    equation_list.append(s[i-1] + s[i])
                    i += 1
                else:
                    equation_list.append(s[i-1])
            else:
                if s[i-1]=="-":
                    equation_list.append(s[i])
                    i += 1
                else:
                    equation_list.append("-" + s[i-1])
            i += 1
        for i in equation_list[:]:
            if i in ("-+","+-","--","++","=","+","-",''):
                equation_list.remove(i)
        var_list = []
        const_list = []
        var_name_list = []
        for i in equation_list:
            if i[-1].isalpha():
                var_name = i[-1]
                var_name_list.append(var_name)
                if len(i)>1 and i[0]!='-':
                    var_list.append(eval(i[:len(i)-1]))
                else:
                    var_list.append(eval('1'))
            else:
                const_list.append(eval(i))
        for i in range(1,len(var_name_list)):
            if (var_name_list[i-1]!=var_name_list[i]):
                print("Error: Expected single variable but received multiple!")
                return "\033[F"
        var_list_sum = sum(var_list)
        const_list_sum = sum(const_list)
        solution = self.division(-(const_list_sum),var_list_sum)
        if solution==-0.0:
            return 0.0
        return solution

print(LinearEquation().solve_one_variable("2x+9=0"))