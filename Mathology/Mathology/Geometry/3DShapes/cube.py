class Cuboid:

    def __init__(self) -> None:
        pass
    
    def totalSurfaceArea(self,side):
        return 6 * side**2
    
    def lateralSurfaceArea(self,side):
        return 4 * side**2
    
    def volume(self,side):
        return side**3