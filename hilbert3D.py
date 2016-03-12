from hilbert3D.HilbertCurve3D import HilbertCurve3D
import numpy as np
import math

if __name__ == '__main__':

    hilbert = HilbertCurve3D(2)

    ox = np.matrix([[1, 0, 0, 0],
                   [0, math.cos(math.radians(32.5)), -math.sin(math.radians(32.5)), 0],
                   [0, math.sin(math.radians(32.5)), math.cos(math.radians(32.5)), 0],
                   [0, 0, 0, 1]])

    oy = np.matrix([[math.cos(math.radians(-38)), 0, math.sin(math.radians(-38)), 0],
                   [0, 1, 0, 0],
                   [-math.sin(math.radians(-38)), 0, math.cos(math.radians(-38)), 0],
                   [0, 0, 0, 1]])

    # print(ox)
    # print(oy)

    for point in hilbert:

        p = np.matrix([[point[0]],
                       [point[1]],
                       [point[2]],
                       [1]])

        pp = (ox * oy) * p
        pp = pp.tolist()
        print(("{0} {1} {2}".format(pp[0][0], pp[1][0], pp[2][0])).replace('.', ','))
