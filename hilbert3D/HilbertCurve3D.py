from .Vector import Vector
from .Point import Point


class HilbertCurve3D:

    def __init__(self, n, size):
        self.n = n
        self.size = size

        length = 2**n - 1
        length_curve = size / length

        self.start_point = Point(-1/2 * length * length_curve,
                                 1/2 * length * length_curve,
                                 -1/2 * length * length_curve)

        self.points_generator = self.generate_points(self.n,
                                                     Vector(0, -length_curve, 0),
                                                     Vector(0, 0, length_curve),
                                                     Vector(length_curve, 0, 0),
                                                     self.start_point)

    def __iter__(self):
        return self.points_generator

    def generate_points(self, n, v1, v2, v3, start_point):

        if n <= 0:
            yield start_point
        else:
            yield from self.generate_points(n - 1, v2, v3, v1, start_point)

            start_point += v1

            yield from self.generate_points(n - 1, v3, v1, v2, start_point)

            start_point += v2

            yield from self.generate_points(n - 1, v3, v1, v2, start_point)

            start_point -= v1

            yield from self.generate_points(n - 1, -v1, -v2, v3, start_point)

            start_point += v3

            yield from self.generate_points(n - 1, -v1, -v2, v3, start_point)

            start_point += v1

            yield from self.generate_points(n - 1, -v3, v1, -v2, start_point)

            start_point -= v2

            yield from self.generate_points(n - 1, -v3, v1, -v2, start_point)

            start_point -= v1

            yield from self.generate_points(n - 1, v2, -v3, -v1, start_point)


if __name__ == '__main__':
    pass
