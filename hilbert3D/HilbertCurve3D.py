from .Vector import Vector
from .Point import Point


class HilbertCurve3D:

    def __init__(self, n):
        self.n = n

        self.points_list = [Point(-(2**(n-1)) + 1/2, -(2**(n-1)) + 1/2, -(2**(n-1)) + 1/2)]

        self.generate_points_list(self.n, Vector(0, 1, 0), Vector(0, 0, 1), Vector(1, 0, 0))

    def generate_points_list(self, n, v1, v2, v3):

        if n <= 0:
            return

        # Draw vertex 0
        self.generate_points_list(n - 1, v2, v3, v1)

        # Draw edge 0
        self.points_list.append(self.points_list[-1] + v1)

        # Draw vertex 1
        self.generate_points_list(n - 1, v3, v1, v2)

        # Draw edge 1
        self.points_list.append(self.points_list[-1] + v2)

        # Draw vertex 2
        self.generate_points_list(n - 1, v3, v1, v2)

        # Draw edge 2
        self.points_list.append(self.points_list[-1] - v1)

        # Draw vertex 3
        self.generate_points_list(n-1, -v1, -v2, v3)

        # Draw edge 3
        self.points_list.append(self.points_list[-1] + v3)

        # Draw vertex 4
        self.generate_points_list(n - 1, -v1, -v2, v3)

        # Draw edge 4
        self.points_list.append(self.points_list[-1] + v1)

        # Draw vertex 5
        self.generate_points_list(n - 1, -v3, v1, -v2)

        # Draw edge 5
        self.points_list.append(self.points_list[-1] - v2)

        # Draw vertex 6
        self.generate_points_list(n - 1, -v3, v1, -v2)

        # Draw edge 6
        self.points_list.append(self.points_list[-1] - v1)

        # Draw vertex 7
        self.generate_points_list(n - 1, v2, -v3, -v1)

    def get_points_list(self):

        for point in self.points_list:
            print(("{0} {1} {2}".format(*point)).replace('.', ','))


if __name__ == '__main__':
    pass
