class Matrix:
    def __init__(self, arg):
        self.value = arg

        self.row = len(arg)
        self.col = len(arg[0])

    def __mul__(self, other):

        result = [[0 for r in range(other.col)] for c in range(self.row)]
        for i in range(self.row):
            for j in range(other.col):
                for k in range(other.row):
                    result[i][j] += self.value[i][k] * other.value[k][j]
        return Matrix(result)

    def __iter__(self):
        return self.value.__iter__()

    def __getitem__(self, item):
        return self.value[item]


if __name__ == '__main__':
    pass
