class Vector:

    def __init__(self, *args):
        self.values = args

    def __neg__(self):
        values = tuple(-1 * value for value in self)
        return Vector(*values)

    def __str__(self):
        return "[" + str(self.values)[1:-1] + "]"

    def __len__(self):
        return len(self.values)

    def __iter__(self):
        return self.values.__iter__()

    def __getitem__(self, item):
        return self.values[item]


if __name__ == '__main__':
    pass

