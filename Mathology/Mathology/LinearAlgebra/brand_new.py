def determinant(matrix):

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
    
        det += (-1)**i * matrix[0][i] * det(submatrix)
    
    return det


print(determinant([[1,2,3],
            [4,5,6],
            [7,8,9]]))