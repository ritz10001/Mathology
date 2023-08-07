from math import pi

class RightCylinder:
    
    def __init__(self) -> None:
        pass

    def curvedSurfaceArea(self,radius,height):
        return 2 * pi * radius * height

    def totalSurfaceArea(self,radius,height):
        return 2 * pi * radius * (radius + height)

    def volume(self,radius,height):
        return pi * radius**2 * height