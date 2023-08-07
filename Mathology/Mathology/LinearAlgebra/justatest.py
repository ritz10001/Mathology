def determinant(matrix):
        if len(matrix)!=len(matrix[0]):
            print("Error: Expected square matrix but input type was of unequal rows and columns!")
            return "\033[F"
        #If it is 2x2 order
        if (len(matrix),len(matrix[0])) == (2,2):
            return matrix[0][0] * matrix [1][1] - matrix[0][1] * matrix[1][0]

        # if it is of higher order
        det = 0
        for i in range(len(matrix)):
            submatrix = []
            for row in range(1,len(matrix)):
                r = []
                for col in range(len(matrix)):
                    if col != i:
                        r.append(matrix[row][col])
                submatrix.append(r)
        
            det += (-1)**i * matrix[0][i] * determinant(submatrix)
        
        return det
    


def cofactor(matrix):
    print(len(matrix))
    print(len(matrix[0]))
    if len(matrix)!=len(matrix[0]):
            print("Error: Expected square matrix but input type was of unequal rows and columns!")
            return "\033[F"
    print("hello")
    # if it is of higher order
    result=[]   
    m=len(matrix)
    n=len(matrix[0])
    for i in range(m):
        result.append([])
    print(result)
    for a in range(len(matrix)):
        for i in range(len(matrix)):
            submatrix = []
            for row in range(1,len(matrix)):
                if row!=a:
                    r = []
                    for col in range(len(matrix)):
                        if col != i:
                            r.append(matrix[row][col])
                    submatrix.append(r)
                    print(submatrix)

            co = (-1)**i * determinant(submatrix)
            result[i].append(co)

    return result
cofactor([[1,2,3],[4,0,6],[7,8,9]])
    