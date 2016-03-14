class PostscriptGenerator:

    def __init__(self, points_generator, image_size):
        self.points_generator = points_generator
        self.image_size = image_size

    def generate_postscript(self):
        print("%!PS-Adobe-2.0 EPSF-2.0")
        print("%%BoundingBox: {0} {0} {1} {1}".format(-self.image_size / 2, self.image_size))
        print("newpath")

        first_point = next(self.points_generator)
        print("{0:.4f} {1:.4f} moveto".format(*first_point))

        for point in self.points_generator:
            print("{0:.4f} {1:.4f} lineto".format(*point))

        print(".4 setlinewidth")
        print("stroke")
        print("showpage")
        print("%%Trailer")
        print("%EOF")
