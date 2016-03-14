import math


def sin(x):
    return math.sin(math.radians(x))


def cos(x):
    return math.cos(math.radians(x))


class Point:

    def __init__(self, *args):
        self.values = args

    def __str__(self):
        return str(self.values)

    def __len__(self):
        return len(self.values)

    def __iter__(self):
        return self.values.__iter__()

    def __getitem__(self, item):
        return self.values[item]

    def __add__(self, other):

        if isinstance(other, Vector):
            values = []

            for i in range(len(self)):
                values.append(self[i] + other[i])

            return Point(*values)

    def __sub__(self, other):

        return self + (-other)


class Vector:

    def __init__(self, *args):

        if isinstance(args[0], Point):
            self.values = tuple(args[0])
        else:
            self.values = args

    def __neg__(self):
        values = tuple(-1 * value for value in self)
        return Vector(*values)

    def __add__(self, other):
        result = tuple(a + b for a, b in zip(self, other))
        return Vector(*result)

    def __sub__(self, other):
        return self + (-other)

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
