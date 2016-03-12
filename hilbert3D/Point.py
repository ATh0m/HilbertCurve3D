from .Vector import Vector


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


if __name__ == '__main__':
    pass
