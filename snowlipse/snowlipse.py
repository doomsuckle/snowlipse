import numpy as np
import PIL.Image as Image

from .EllipseContainer import EllipseContainer


def get_snow(psnow=0.1, height=400, width=640):
    """
    generate an image with random background snow
    :param psnow: rate of snow in image
    :param height: image height
    :param width: image width
    :return:
    """
    ret = np.random.rand(height, width)
    ret[ret > psnow] = 1
    return np.uint8(255 * ret)


def get_evil_snow(psnow=0.1, height=400, width=640):
    """
    generate an image with non-standard background snow
    :param psnow: rate of snow in image
    :param height: image height
    :param width: image width
    :return:
    """
    ret = np.random.rand(height, width)
    ret1 = np.random.rand(height, width)
    ret[ret > psnow] = 1
    ret1[ret1 > 3. * psnow] = 1

    for row in range(height):
        for col in range(width):
            if row < col:
                ret[row, col] = ret1[row, col]

    return np.uint8(255 * ret)


def toy():
    """
    toy raw script to generate an image
    :return:
    """
    height = 400

    # create ellipse container
    econ = EllipseContainer(300, 200, 80, 200, 57)

    # number of points to generate
    num_gen = 1000

    # get points to draw
    r, xx, yy = econ.get_points(num_gen)

    # apply smearing
    xx = xx + 1. * np.random.normal(0, 1., num_gen)
    yy = yy + np.random.normal(0, 1., num_gen)

    # get base image
    xr = get_snow(0.10)
    # get rows and columns to flip with snow
    rows = height - yy.astype(np.uint) - 1
    cols = xx.astype(np.uint)
    # set to 0
    xr[rows, cols] = 0
    img = Image.fromarray(xr)
    img.save('img-toy.png')  # econ = EllipseContainer(300, 200, 80, 200, 57) num_gen = 1000 xr = get_snow(0.00)


if __name__ == '__main__':
    toy()