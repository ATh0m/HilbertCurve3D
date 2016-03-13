from hilbert3D.HilbertCurve3D import HilbertCurve3D
from hilbert3D.Transformation import Transformation
from hilbert3D.Vector import Vector

if __name__ == '__main__':

    hilbert = HilbertCurve3D(1, 2)

    # print("%!PS-Adobe-2.0 EPSF-2.0")
    # print("%%BoundingBox: 0 0 1000 1000")
    # print("newpath")
    # print("500 500 moveto")

    for point in hilbert:

        new_point = Transformation.rotate_around_y_axis(-38, point)
        new_point2 = Transformation.rotate_around_x_axis(32.5, new_point)

        # new_point3 = Transformation.translation(new_point2, Vector(500, 500, 0))
        #
        # new_point4 = Transformation.perspective_view(new_point3, 500)

        print(("{0:.2f} {1:.2f} {2:.2f}".format(*new_point2)).replace(".", ","))

    # print(".4 setlinewidth")
    # print("stroke")
    # print("showpage")
    # print("%%Trailer")
    # print("%EOF")

