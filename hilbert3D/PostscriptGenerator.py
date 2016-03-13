class PostscriptGenerator:
    def __init__(self, points_generator, image_size):
        self.points_generator = points_generator
        self.image_size = image_size

    def generate_postscript(self):
        print("%!PS-Adobe-2.0 EPSF-2.0")
        print("%%BoundingBox: 0 0 {0} {0}".format(self.image_size))
        print("newpath")

        first_point = next(self.points_generator)
        print("{0:.2f} {0:.2f} moveto".format(*first_point))

        for point in self.points_generator:
            print("{0:.2f} {1:.2f} lineto".format(*point))

        print(".2 setlinewidth")
        print("stroke")
        print("showpage")
        print("%%Trailer")
        print("%EOF")

    def print_points(self):

        for point in self.points_generator:

            print(("{:.2f}\t{:.2f}\t{:.2f}".format(*point).replace('.', ',')))
