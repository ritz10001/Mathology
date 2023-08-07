class Cuboid:

    def __init__(self) -> None:
        pass

    def totalSurfaceArea(self,length,breadth,height):
        return 2 * (eval(length) * eval(breadth) + eval(length) * eval(height) + eval(breadth) * eval(height))

    def lateralSurfaceArea(self,length,breadth,height):
        return 2 * eval(height) * (eval(length) + eval(breadth))

    def volume(self,length,breadth,height):
        return eval(length) * eval(breadth) * eval(height)