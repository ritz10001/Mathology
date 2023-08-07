from math import pi, factorial

class Trig:
    """
    To use pi, please import python's in built math.pi
    """
    def __init__(self):
        pass
    def radiansToDegrees(self,angle):
        return angle*180/pi

    def degreesToRadians(self,angle):
        return angle*pi/180

    def sin(self,angle): #Angle in radians
        if angle % pi == 0: #if angle=n*pi
            return 0
        sine = 0
        for n in range(10):
            sine += (((-1)**n)*(angle**((2*n)+1)))/factorial((2*n)+1)
        return sine

    def cos(self,angle):
        if len(str(angle/pi))==3:
            if str(angle/(pi))[-1] != '0': #if angle=(n+1/2)*pi -> angle/pi - 1/2 = n
                return 0
            else:
                cosine = 0
                for n in range(25):
                    cosine += (((-1)**n)*(angle**(2*n)))/factorial(2*n)
                return cosine
        else:
            cosine = 0
            for n in range(25):
                cosine += (((-1)**n)*(angle**(2*n)))/factorial(2*n)
            return cosine

    def tan(self,angle):
        if self.cos(angle)==0:
            return "f(x) = tan x is not defined for x = {}, which is a multiple of pi/2".format(angle)
        tan = self.sin(angle)/self.cos(angle)
        if str(tan) in ("-0.0","0.0"):
            return 0
        return tan

    def cot(self,angle):
        if self.sin(angle)==0:
            return "f(x) = cot x is not defined for x = {}, which is a multiple of pi".format(angle)
        cot = self.cos(angle)/self.sin(angle)
        if str(cot) in ("-0.0","0.0"):
            return 0
        return cot

    def sec(self,angle):
        if self.cos(angle)==0:
            return "f(x) = sec x is not defined for x = {}, which is a multiple of pi/2".format(angle)
        return 1/self.cos(angle)

    def cosec(self,angle):
        if self.sin(angle)==0:
            return "f(x) = cosec x is not defined for x = {}, which is a multiple of pi".format(angle)
        return 1/self.sin(angle)
    
    def arcsin(self,value):
        if value<-1 or value>1:
            print("Error: Input value is outside the domain [-1,1] of arcsin!")
            return "\033[F"
        epsilon = 0.00001
        low = -pi / 2
        high = pi / 2
        mid = (low + high) / 2
        while abs(self.sin(mid) - value) > epsilon:
            if self.sin(mid) > value:
                high = mid
            else:
                low = mid
            mid = (low + high) / 2
        return mid

    def arccos(self,value):
        arcsin = 0

        for n in range(10):
            arcsin += factorial(2*n)*(value**((2*n)+1))/((2**(2*n))*((factorial(n))**2)*((2*n)+1))
        
        return pi/2 - arcsin

    def arctan(self,value):
        arctan = self.arccos(1/(1+value**2)**0.5)
        if value<0:
            return -arctan
        return arctan

    def arccot(self,value):
        if value==0:
            return pi/2
        return self.arctan(1/value)
    
    def arcsec(self,value):
        if value>-1 and value<1:
            print("Error: Input value is outside the domain (-∞,-1] ∪ [1,∞) of arcsec!")
            return "\033[F" 
        return self.arccos(1/value)

    def arccosec(self,value):
        if value>-1 and value<1:
            print("Error: Input value is outside the domain (-∞,-1] ∪ [1,∞) of arccosec!")
            return "\033[F" 
        return self.arcsin(1/value)