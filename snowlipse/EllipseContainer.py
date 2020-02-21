import numpy as np

class EllipseContainer(object):
    """
    class to contain an ellipse based on the
    projection with 5 parameters: cx, cy, a, b, angle
    """

    def __init__(self, cx, cy, a, b, angle):
        """
        :param cx: x-center of the ellipse
        :param cy: y-center of the ellipse
        :param a: major axis
        :param b: minor axis
        :param angle: angle of the ellipse (in degrees)
        """

        self.cx = cx
        self.cy = cy
        self.a = a
        self.b = b
        self.angle_deg = angle
        self.angle_rad = np.radians(angle)  # convert to radians

    def get_points(self, npoints: int):
        """
        get structure with points in degrees, x, and y
        :param npoints: number of points to sample
        :return:
        """

        R = sorted(np.random.rand(npoints) * 2. * np.pi)

        xx = self.cx + self.a * np.cos(R) * np.cos(self.angle_rad) - self.b * np.sin(R) * np.sin(
            self.angle_rad)

        yy = self.cy + self.a * np.cos(R) * np.sin(self.angle_rad) + self.b * np.sin(R) * np.cos(
            self.angle_rad)

        return R, xx, yy
