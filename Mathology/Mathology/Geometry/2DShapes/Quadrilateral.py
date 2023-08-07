from Mathology.Geometry.geometry_2d import Geometry2D

class Quadrilateral:

    def squareArea(self,side):
        return eval(side) ** 2
    
    def squarePerimeter(self,side):
        return self.rhombusPerimeter(side)
    
    def rectanglePerimeter(self,length,breadth):
        return self.parallelogramPerimeter(length,breadth)
    
    def rectangleArea(self,length,breadth):
        return self.parallelogramArea(length,breadth)
    
    def rhombusArea(self,diagonal1,diagonal2):
        return self.kiteArea(diagonal1,diagonal2)
    
    def rhombusPerimeter(self,side):
        return eval(side) * 4
    
    def parallelogramArea(self,base,height):
        return eval(base) * eval(height)
    
    def parallelogramPerimeter(self,base,side):
        return 2 * (eval(base) + eval(side))

    def trapeziumPerimeter(self,side1,side2,side3,side4):
        return eval(side1) + eval(side2) + eval(side3) + eval(side4)

    def trapeziumArea(self,shortBase,longBase,height):
        return 0.5 * eval(height) * (eval(shortBase) + eval(longBase))
    
    def kiteArea(self,diagonal1,diagonal2):
        return eval(diagonal1) * eval(diagonal2) * 0.5
    
    def kitePerimeter(self,shortSide,longSide):
        return self.parallelogramPerimeter(shortSide,longSide)