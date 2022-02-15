from lsat_imgread import import_image
from dji_imgread import read_image
import matplotlib.pyplot as plt
import numpy.ma as ma
import numpy as np
import earthpy.plot as ep
from PIL import Image
from PIL.ExifTags import TAGS
# from libxmp import XMPFiles, consts
from skimage.metrics import structural_similarity as ssim


def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    imageA = ma.resize(imageA, (imageB.shape[0], imageB.shape[1]))
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err


def compare_images(imageA, imageB, title):
    # compute the mean squared error and structural similarity
    # index for the images
    m = mse(imageA, imageB)
    s = ssim(ma.resize(imageA, (imageB.shape[0], imageB.shape[1])), imageB)

    # setup the figure
    fig = plt.figure(title)
    plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))

    # show first image
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(imageA, cmap = plt.cm.gray)
    plt.axis("off")

    # show the second image
    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(imageB, cmap = plt.cm.gray)
    plt.axis("off")

    # show the images
    plt.show()


def main():
    landsat_image = import_image("img/LC08_L1TP_016037_20211214_20211223_02_T1_B10.TIF", 10)
    dji_image, dji_meta = read_image("img/DJI_0354.JPG")

    # path to the image or video
    imagename = "img/DJI_0354.JPG"

    with open(imagename, "rb") as fin:
        img = fin.read()
        xmp_lat = str(img).find("GpsLatitude=")
        xmp_lon = str(img).find("GpsLongitude=")
        dji_lat = str(img)[xmp_lat+13:xmp_lat+24]
        dji_lon = str(img)[xmp_lon+14:xmp_lon+25]

    # print(float(dji_lat), float(dji_lon))
    #
    # # lat_start = 33.176999 - float(dji_lat)
    # # lon_start = -80.106913 - float(dji_lon)
    #
    # lat_pix_h = abs(34.123 - 33.825) / landsat_image.shape[0]
    # lon_pix_h = abs(80.913 - 78.861) / landsat_image.shape[0]
    #
    # lat_pix_v = abs(34.123 - 32.518) / landsat_image.shape[1]
    # lon_pix_v = abs(81.336 - 80.913) / landsat_image.shape[1]
    #
    # print(lat_pix_h, lon_pix_h)
    # print(lat_pix_v, lon_pix_v)

    # landsat_image_cut = landsat_image[lat_start:dji_image.shape[0]+lat_start, lon_start:dji_image.shape[1]+lon_start]

    # print(lat_start)
    # print(dji_image.shape[0]+lat_start)
    # print(lon_start)
    # print(dji_image.shape[1]+lon_start)

    # plot the image
    # fig, ax = plt.subplots(figsize=(10, 8))
    # im = plt.imshow(landsat_image_cut, interpolation='nearest')
    # ep.colorbar(im)
    # ax.set(title="12/14")
    # ax.set_axis_off()
    # plt.show()

    compare_images(landsat_image, dji_image, "12-14")


main()

''' 
Path: 16
Row: 37
Ctr Lat: 33.176999
Ctr Lon: -80.106913
Ul Lat: 34.123
Ul Lon: -80.913
Ur Lat: 33.825	
Ur Lon: -78.861
Ll Lat: 32.518	
Ll Lon: -81.336
Lr Lat: 32.225	
Lr Lon: -79.319
'''

