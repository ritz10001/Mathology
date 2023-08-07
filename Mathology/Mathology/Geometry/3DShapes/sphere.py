from math import pi

class Sphere:

    def __init__(self) -> None:
        pass

    def surfaceArea(self,radius):
        return 4 * pi * radius**2

    def volume(self,radius):
        return 4/3 * pi * radius**3