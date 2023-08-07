from math import pi
from Mathology.Trigonometry.trigonometry import Trig

class Circle(Trig):

    def __init__(self):
        pass

    def area(self,radius):
        return pi * radius**2
    
    def circumference(self,radius):
        return radius * pi * 2
    
    def sectorArea(self, theta, radius):
        """Theta in degrees"""
        return theta/360 * self.area(radius)
    
    def segmentArea(self,theta, radius):
        """Theta in degrees is the area of the segment of the sector making angle theta"""
        return radius**2 * (((pi * theta)/360) - (self.sin(theta)/2))
    
    def arcLength(self,theta,radius):
        """Theta in degrees"""
        return self.degreesToRadians(theta) * radius
    