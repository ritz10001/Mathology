class Geometry3D:
    
    def __init__(self):
        pass
    
    def distance(self,A=(0,0,0),B=(0,0,0)):
        """
        A=(x1,y1,z1)
        B=(x2,y2,z2)
        """
        if len(A)>3 or len(B)>3:
            print("Error: Expected 3-dimensional coordinates but received higher dimensional coordinates instead!")
            return "\033[F"
        if type(A)==int:
            M=A
            A=(M,0,0)
        if type(B)==int:
            M=B
            B=(M,0,0)
        A=list(A)
        B=list(B)
        if len(A)<3:
            x=3-len(A)
            for i in range(x):
                A.append(0)
        if len(B)<3:
            y=3-len(B)
            for j in range(y):
                B.append(0)
        result = ((B[0]-A[0])**2 + (B[1]-A[1])**2 + (B[2]-A[2])**2)**0.5
        return result

    def InternalDivision(self,m=1,n=1,x1=0,y1=0,z1=0,x2=0,y2=0,z2=0):
        x = (m*x2 + n*x1)/(m+n)
        y = (m*y2 + n*y1)/(m+n)
        z = (m*z2 + n*z1)/(m+n)
        if x==-0.0:
            x=0.0
        if y==-0.0:
            y=0.0
        if z == -0.0:
            z = 0.0
        return (x,y,z)
    
    def ExternalDivision(self,m=1,n=1,x1=0,y1=0,z1=0,x2=0,y2=0,z2=0):
        x = (m*x2 - n*x1)/(m-n)
        y = (m*y2 - n*y1)/(m-n)
        z = (m*z2 - n*z1)/(m-n)
        if x==-0.0:
            x=0.0
        if y==-0.0:
            y=0.0
        if z == -0.0:
            z = 0.0
        return (x,y,z)