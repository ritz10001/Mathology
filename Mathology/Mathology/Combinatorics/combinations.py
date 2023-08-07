from math import factorial

class Combinations:
    def __init__(self):
        pass

    def combination(self,n,r):
        return factorial(n)/(factorial(r)*factorial(n-r))

    def combinationWithRepetition(self,n,r):
        return factorial(n+r-1)/(factorial(r)*factorial(n-1))