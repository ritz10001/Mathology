from Mathology.ElementaryMath.arithmetic_operations import ArithmeticOperations

class Matrix(ArithmeticOperations):
    
    def __init__(self):
        pass
    
    def addition(self,*matrices):
        """_summary_
        Please enter your input matrices separated by a comma and not as a list of matrices, i.e.,
        do not include the opening and closing []
        
        Correct:    [[1,2],[3,4]],
                    [[5,6],[7,8]],
                    [[9,10],[11,12]]

        Wrong:      [[[1,2],[3,4]],
                     [[5,6],[7,8]],
                     [[9,10],[11,12]]]

        Correct:    [[1,2]],
                    [[3,4]],
                    [[2,3]]
        
        Wrong:      [[[1,2]],
                     [[3,4]],
                     [[2,3]]]
        Returns:
            _type_: _description_
        """
        orders=[]
        for matrix in matrices:
            m = len(matrix)
            n = len(matrix[0])
            orders.append((m,n))
        first = orders[0]
        for i in range(1,len(orders)):
            if orders[i]!=first:
                print("Error: Expected matrices of same order but received matrices of different orders!")
                return "\033[F"
        if len(matrices)>1:
            s = []
            #Calculating the sum
            for i in range(len(matrices[0])):
                for j in range(len(matrices[0][0])):
                    cell_sum = 0
                    for k in range(len(matrices)):
                        cell_sum += matrices[k][i][j]
                    s.append(cell_sum)
            result = []
            counter = 0
            #Converting s to an mxn matrix of desired result dimensions
            for i in range(len(matrices[0])):
                result.append([])
            for i in range(len(matrices[0])):
                for j in range(len(matrices[0][0])):
                    result[i].append(s[counter])
                    counter += 1
            return result
        else:
            return matrices[0]
    
    def subtraction(self,*matrices):
        """_summary_
        Please enter your input matrices separated by a comma and not as a list of matrices, i.e.,
        do not include the opening and closing []
        
        Correct:    [[1,2],[3,4]],
                    [[5,6],[7,8]],
                    [[9,10],[11,12]]

        Wrong:      [[[1,2],[3,4]],
                     [[5,6],[7,8]],
                     [[9,10],[11,12]]]

        Correct:    [[1,2]],
                    [[3,4]],
                    [[2,3]]
        
        Wrong:      [[[1,2]],
                     [[3,4]],
                     [[2,3]]]
        Returns:
            _type_: _description_
        """
        orders = []
        for matrix in matrices:
            m = len(matrix)
            n = len(matrix[0])
            orders.append((m,n))
        first = orders[0]
        for i in range(1,len(orders)):
            if orders[i]!=first:
                print("Error: Expected matrices of same order but received matrices of different orders!")
                return "\033[F"
        if len(matrices)>1:
            s = []
            #Calculating the sum
            for i in range(len(matrices[0])):
                for j in range(len(matrices[0][0])):
                    cell_sum = 0
                    for k in range(len(matrices)):
                        if k==0:
                            cell_sum += matrices[k][i][j]
                        else:
                            cell_sum -= matrices[k][i][j]
                    s.append(cell_sum)
            result = []
            counter = 0
            #Converting s to an mxn matrix of desired result dimensions
            for i in range(len(matrices[0])):
                result.append([])
            for i in range(len(matrices[0])):
                for j in range(len(matrices[0][0])):
                    result[i].append(s[counter])
                    counter += 1
            return result
        else:
            return matrices[0]
    
    def multiplication(self,*matrices):
        """_summary_
        Please enter your input matrices separated by a comma and not as a list of matrices, i.e.,
        do not include the opening and closing []
        
        Correct:    [[1,2],[3,4]],
                    [[5,6],[7,8]],
                    [[9,10],[11,12]]

        Wrong:      [[[1,2],[3,4]],
                     [[5,6],[7,8]],
                     [[9,10],[11,12]]]

        Correct:    [[1,2]],
                    [[3,4]],
                    [[2,3]]
        
        Wrong:      [[[1,2]],
                     [[3,4]],
                     [[2,3]]]
        Returns:
            _type_: _description_
        """
        matrices = list(matrices)
        if len(matrices)>1:
            x = 1
            while x<len(matrices)+1: #[P,Q,R,S]
                A = matrices[x-1]
                if x==1:
                    B = matrices[x]
                    x += 2
                else:
                    x += 1
                    K = A
                    A = B
                    B = K
                a_rows = len(A)
                a_cols = len(A[0])
                b_rows = len(B)
                b_cols = len(B[0])
                C = []
                """
                For matrix multiplication to be possible for matrices A and B with orders m1xn1 and m2xn2 respectively,
                n1=m2
                The resultant product matrix has order m1xn2
                Here,
                m1=a_rows
                n1=a_cols
                m2=b_rows
                m3=b_cols
                """
                if a_cols==b_rows:
                    for i in range(a_rows):
                        for j in range(b_cols):
                            res = 0
                            for k in range(a_cols):
                                res += A[i][k] * B[k][j]
                            C.append(res)
                    result = []
                    counter = 0
                    for i in range(a_rows):
                        result.append([])
                    for i in range(a_rows):
                        for j in range(b_cols):
                            result[i].append(C[counter])
                            counter+=1
                    B=result
                    return result
                else:
                    print("Error: Multiplication not possible as input matrices have incompatible orders!")
                    return "\033[F"
        else:
            return matrices[0]
    
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
        
            det += (-1)**i * matrix[0][i] * det(submatrix)
        
        return det
    
    def transpose(self,matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        result = []
        copy = []
        counter = 0
        for col in range(cols):
            for row in range(rows):
                r = matrix[row][col]
                copy.append(r)
        for col in range(cols):
            result.append([])
        for col in range(cols):
            for row in range(rows):
                result[col].append(copy[counter])
                counter += 1
        return result
    
    def inverse(self):
        pass
    # def cofactor(self,matrix):
    #     """
    #     [[1,2,3],
    #      [4,5,6],
    #      [7,8,9]]

    #     [[a11 a12 . . . a1j. . . a1n],
    #      [a21 a22 . . . a2j. . . a2n],
    #      [. . . . . . . . . . . . . .],
    #      [ai1 ai2 . . . aij . . . ain],
    #      [. . . . . . . . . . . . . .]
    #      [an1 an2 . . . anj . . . ann]]

    #     [[1,2,3,4],
    #      [5,6,7,8],
    #      [9,10,11,12],
    #      [13,14,15,16]]
    #     """
    #     rows = len(matrix)
    #     cols = len(matrix[0])
    #     result = []
    #     if (rows,cols)==(2,2):
    #         minor = self.determinant2x2(matrix)
    #     else:
    #         for row in range(rows):
    #             result.append([])
    #         for row in range(rows):
    #             for col in range(cols):
    #                 result[row].append([])
    #         for row in range(1,rows+1):
    #             for col in range(1,cols+1):
    #                 # result[row][col] =
    #                 pass 
    #     print(result)
    
    def cofactor(self,matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        result = []
        for row in range(rows):
            result.append([])
            for col in range(cols):
                result[row].append(0)
        for row in range(1,rows+1):
            for col in range(1,cols+1):
                result[row-1][col-1] = self.exponentiation(-1,row+col) * self.determinant(self.minor(matrix,row,col))
        print(result)
    
    def minor(self,matrix,row,col):
        # rows = len(matrix)
        # cols = len(matrix[0])
        # result = []
        # for row in range(rows):
        #     result.append([])
        #     for col in range(cols):
        #         result[row].append(0)
        # for i in range(1,rows+1):
        #     for j in range(1,cols+1):
        #         if i!=row and j!=col:
        #             result[i-1][j-1] = matrix[i-1][j-1]
        # return result
        m = []
        counter = 0
        result = []
        for i in range(row,len(matrix)):
            for j in range(col,len(matrix[0])):
                m.append(matrix[i][j])
        for i in range(row+1):
            result.append([])
            for j in range(col+1):
                result[i].append(m[counter])
                counter+=1
                
                
        print(result)
    def determinant2x2(self,matrix):
        """
        [[1,2,4],
         [3,4,2],
         [5,6,7]]
        """
        determinant = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
        return determinant

    def adjoint(self):
        pass
    def eigenvalues(self):
        pass
    def exponent(self):
        pass