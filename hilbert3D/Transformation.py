from .Point import Point
from .Math import sin, cos


class Transformation:

    @classmethod
    def rotate_around_x_axis(cls, x, point):

        point_x, point_y, point_z = point

        new_point = Point(point_x * 1 + point_y * 0 + point_z * 0,
                          point_x * 0 + point_y * cos(x) - point_z * sin(x),
                          point_x * 0 + point_y * sin(x) + point_z * cos(x))

        return new_point

    @classmethod
    def rotate_around_y_axis(cls, x, point):

        point_x, point_y, point_z = point

        new_point = Point(point_x * cos(x) + point_y * 0 + point_z * sin(x),
                          point_x * 0 + point_y * 1 + point_z * 0,
                          -point_x * sin(x) + point_y * 0 + point_z * cos(x))

        return new_point

    @classmethod
    def translation(cls, point, vec):
        return point + vec

    @classmethod
    def perspective_view(cls, point, d):
        point_x, point_y, point_z = point

        temp = d / (point_z + d)

        new_point = Point(point_x * temp, point_y * temp, 0)

        return new_point


if __name__ == '__main__':
    pass
