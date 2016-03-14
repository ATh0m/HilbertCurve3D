from .Math import Point, Vector, sin, cos


class Transformation:

    def __init__(self, points_generator, spectator, x, y, z, x_angle, y_angle):
        self.points_generator = points_generator

        self.spectator = spectator

        self.start_point = Point(x, y, z)

        self.x_angle = x_angle
        self.y_angle = y_angle

        vector = self.points_generator.center_vector

        self.transformed_points_generator = self.generate_transformed_points(self.points_generator,
                                                                             self.spectator,
                                                                             vector,
                                                                             self.start_point,
                                                                             self.x_angle,
                                                                             self.y_angle)

    def generate_transformed_points(self, points_generator, spectator, vector, start_point, x_angle, y_angle):

        for new_point in points_generator:

            new_point += vector

            new_point = self.rotate_around_y_axis(y_angle, new_point)
            new_point = self.rotate_around_x_axis(-x_angle, new_point)

            new_point += Vector(start_point)

            new_point = self.perspective_view(new_point, spectator)

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
    def perspective_view(cls, point, d):
        point_x, point_y, point_z = point

        temp = d / (point_z + d)

        new_point = Point(point_x * temp, point_y * temp, 0)

        return new_point


if __name__ == '__main__':
    pass
