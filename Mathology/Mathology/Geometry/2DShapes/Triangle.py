from Mathology.Geometry.geometry_2d import Geometry2D

class Triangle(Geometry2D):
    def __init__(self) -> None:
        pass

    """Calculate area and perimeter using input side length"""

    def perimeter(self,side1,side2,side3):
        if None in (side1,side2,side3):
            print("Error: expected 3 sides of a triangle, received incorrect number of sides instead!")
            return "\033[F"
        return eval(side1) + eval(side2) + eval(side3)

    def equilateralArea(self,side):
        return ((3**0.5)/4)*(eval(side)**2)
    
    def isocelesArea(self,altitude,base):
        if None in (altitude, base):
            print("Error: expected both, altitude and base of a triangle, received incorrect number of sides instead!")
            return "\033[F"
        return 0.5 * eval(altitude) * eval(base)

    def heronArea(self,side1,side2,side3):
        if None in (side1,side2,side3):
            print("Error: expected 3 sides of a triangle, received incorrect number of sides instead!")
            return "\033[F"
        semiperimeter = self.perimeter(side1,side2,side3)/2
        return (semiperimeter * (semiperimeter - side1) * (semiperimeter - side2) * (semiperimeter - side3))**0.5

    def median(self,x1=0,y1=0,x2=0,y2=0):
        return self.InternalDivision(1,1,x1,y1,x2,y2)
    
    def centroid(self,x1=0,y1=0,x2=0,y2=0,x3=0,y3=0):
        return (((x1+x2+x3)/3),((y1+y2+y3)/3))

    