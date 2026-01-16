import math
class LinearRegression:

    def __init__(self):
        pass
    

    def fit(self, X, y)->None:
        """
        for now this just does simple LinearRegression
        """
        """ y = (xtx)-1 *xty"""
        self.beta = self.solve_least_squares(self.construct_design(X),y) 
    def predict(self, X, y):
        pass


    def _mse(self):
        pass

    def construct_design(self,matrix):
        design = [[1 for _ in range(1)] for _ in range(matrix.dims[0])]  
        i = 0 
        for row in matrix._mat:
            design[i]+=row
            i+=1


        return Matrix(design)
        

    def qr_decomposition(self, matrix):
        """
        Computes X = Q * R using Modified Gram-Schmidt.
        Returns: (Matrix Q, Matrix R)
        """
        rows, cols = matrix.dims
        #create deep copy of sols 
        V = [[matrix._mat[r][c] for r in range(rows)] for c in range(cols)]
    
        Q_cols = [[0.0] * rows for _ in range(cols)]
        R = [[0.0] * cols for _ in range(cols)]

        for i in range(cols):
            norm_v = math.sqrt(sum(V[i][k]**2 for k in range(rows)))
            R[i][i] = norm_v
        
            for k in range(rows):
                Q_cols[i][k] = V[i][k] / norm_v  # q_i = v_i / ||v_i||

            for j in range(i + 1, cols):
            # Calculate projection: R[i][j] = q_i . v_j
                proj = sum(Q_cols[i][k] * V[j][k] for k in range(rows))
                R[i][j] = proj
            
                for k in range(rows):
                    V[j][k] -= proj * Q_cols[i][k]

        # Reconstruct Q matrix from columns
        Q_data = [[Q_cols[c][r] for c in range(cols)] for r in range(rows)]
    
        return Matrix(Q_data), Matrix(R)

    def back_substitution(self, R, target):
        """
        Solves Rx = target for x, where R is upper triangular.
        R: Matrix object
        target: List or Vector (the result of Q.T * y)
        """
        n = R.dims[1] # Number of features/columns
        x = [0.0] * n
    
        # Start from the bottom row and move up
        for i in range(n - 1, -1, -1):
            val = target[i]
        
            # Subtract known terms (x_j) from the right side
            for j in range(i + 1, n):
                val -= R._mat[i][j] * x[j]
            
            # Divide by the diagonal element
            x[i] = val / R._mat[i][i]
        
        return x

    def solve_least_squares(self, X, y):
            # 1. Decompose X
        Q, R = self.qr_decomposition(X)
    
        target = []
        Q_T = Q.T
        for row in Q_T._mat: 
            dot_product = sum(row[k] * y[k][0] for k in range(len(y)))
            target.append(dot_product)
        
        # 3. Solve R * beta = (Q.T * y)
        self.beta = self.back_substitution(R, target)
    
        return self.beta





    def score(self):
        pass


class Matrix:
    def __init__(self, data):
        """ assumes your matrix is consistent"""
        self._mat = data
        
        self.dims = (len(data), len(data[0])) if data else (0,0)

    @property
    def T(self):
        """The T property."""
        return self.transpose()


    def __mul__(self, matrix2):
        """
        this assumes matrix1 * matrix2
        return a new matrix object
        """
        
        ans = Matrix(data =[[0 for _ in range(self.dims[0])] for _ in
            range(matrix2.dims[1])])

        if self.dims[1]!= matrix2.dims[0]:
            print(f"dimension mismatch: {self.dims} and {matrix2.dims}")
        for i in range(self.dims[0]):
            for j in range(matrix2.dims[1]):
                for k in range(self.dims[1]):
                    ans._mat[i][j] += self._mat[i][k] * matrix2._mat[k][j]
        return ans

    def transpose(self):
        """ simple function to retrieve the tran"""
        
        new_data = [[self._mat[j][i] for j in range(self.dims[0])] for i in
            range(self.dims[1])]
        return Matrix(new_data)

    def inverse(self):
        inv = self._mat.copy()
        pass



    def __str__(self):
        for a in self._mat:
            print(f"{a}")

        return ""


if __name__ == "__main__":

    mat1 = Matrix([[1,2],[4,5],[7,8]])
    mat2 = Matrix([[1,3,5],[2,4,6],[3,5,7]])
    print(mat1, mat2)
    ans = mat1 * mat2
    print(ans)
    print(mat1.T)
    print(mat1)
    vector1 = [[1],[2],[3]]
    lr = LinearRegression()
    lr.fit(Matrix([[0],[1],[5.5]]), vector1)
    print(round(lr.beta[0],3), round(lr.beta[1], 3))
