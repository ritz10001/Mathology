from math import factorial
import collections

class Permutations:
    def __init__(self):
        pass

    def permutationWithoutRepetition(self,n,r):
        return factorial(n)/factorial(n-r)

    def allPermutationWithRepetition(self,n,r):
        return n**r

    def permutationWithRepetition(self,n,*r):
        if str(type(r[0]))=="<class 'dict_values'>":
            denominator = 1
            for i in r[0]:
                denominator *= factorial(i)
            return int(factorial(n)/denominator)
        else:
            denominator = 1
            for i in r:
                denominator *= factorial(i)
            return int(factorial(n)/denominator)

    def wordPermutation(self,word):
        frequency_dict = collections.Counter(word)
        return self.permutationWithRepetition(len(word),frequency_dict.values())
    
    def circularArrangements(self,n):
        return factorial(n-1)

x = Permutations()
print(x.wordPermutation("MISSISSIPPI"))