class Percentages:
    def __init__(self):
        pass
    def percentOfNumber(self,percent,number):
        return str((percent/100)*number) + "%"
    def percentChange(self,old,new):
        return str(((new-old)/old)*100) + "%"
    def quantityIncrement(self,percent,quantity):
        return str(quantity + (percent/100)*quantity) + "%"
    def quantityDecrement(self,percent,quantity):
        return str(quantity - (percent/100)*quantity) + "%"
    def fractionToPercent(self,fraction):
        return str(fraction*100) + "%"
    def percentToDecimal(self,percent):
        return str(percent/100) + "%"