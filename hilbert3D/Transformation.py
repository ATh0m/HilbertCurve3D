from .Point import Point
from .Vector import Vector
from .Math import sin, cos


class Transformation:

    def __init__(self, points_generator, image_size, spectator, x, y, z, x_angle, y_angle):
        self.points_generator = points_generator

        self.image_size = image_size
        self.spectator = spectator

        self.start_point = Point(x, y, z)

        self.x_angle = x_angle
        self.y_angle = y_angle

        x, y, z = self.start_point

        self.vector = Vector(1/2 * self.image_size + x,
                             1/2 * self.image_size + y,
                             z)

        self.vector -= Vector(*points_generator.start_point)

        self.transformed_points_generator = self.generate_transformed_points(self.points_generator,
                                                                             self.spectator,
                                                                             self.vector,
                                                                             self.x_angle,
                                                                             self.y_angle)

    def generate_transformed_points(self, points_generator, spectator, vector, x_angle, y_angle):

        for new_point in points_generator:

            new_point = self.rotate_around_y_axis(y_angle, new_point)
            new_point = self.rotate_around_x_axis(x_angle, new_point)

            new_point = self.perspective_view(new_point, spectator)

            new_point = self.translation(new_point, vector)

            yield new_point

    def __iter__(self):
        return self.transformed_points_generator

    def __next__(self):
        return next(self.transformed_points_generator)

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
