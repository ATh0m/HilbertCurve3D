from hilbert3D.HilbertCurve3D import HilbertCurve3D
from hilbert3D.Transformation import Transformation
from hilbert3D.PostscriptGenerator import PostscriptGenerator
import sys

if __name__ == '__main__':

    n = int(sys.argv[1])
    s = int(sys.argv[2])
    u = int(sys.argv[3])
    d = int(sys.argv[4])
    x = int(sys.argv[5])
    y = int(sys.argv[6])
    z = int(sys.argv[7])
    x_angle = float(sys.argv[8])
    y_angle = float(sys.argv[9])

    hilbert_curve_3d = HilbertCurve3D(n, u)
    hilbert_curve_3d_transformation = Transformation(hilbert_curve_3d, d, x, y, z, x_angle, y_angle)
    hilbert_curve_3d_transformation_postscript_generator = PostscriptGenerator(hilbert_curve_3d_transformation, s)

    hilbert_curve_3d_transformation_postscript_generator.generate_postscript()
