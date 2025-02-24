class matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])
    
    # def print_matrix(self):
    #     for row in self.data:
    #         print(' '.join(map(str, row)))

    def transpose(self):
        # tmatrix = [[0 for _ in range(self.rows)] for _ in range(self.cols)]
        tmatrix = [0] * [self.cols, self.rows]
        for i in range(self.cols):
            for j in range(self.rows):
                tmatrix[i][j] = 0
        # tmatrix = [[0 for _ in range(self.rows)] for _ in range(self.cols)]
        # print(tmatrix)
        
        for i in range(self.rows):
            for j in range(self.cols):
                tmatrix[j][i] = self.data[i][j]
        self.rows, self.cols = self.cols, self.rows
        self.data = tmatrix
        
if __name__ == "__main__":
    m = matrix(3, 3)

    m.data = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(m)
    m.transpose()
    print(m)

    m = matrix(2, 3)
    m.data = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    print(m)
    m.transpose()
    print(m)




