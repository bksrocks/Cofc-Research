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
import cv2


def compare_images(landsat, drone):
    # image comparison utilizing https://www.pyimagesearch.com/2014/07/14/3-ways-compare-histograms-using-opencv-python/

    # initialize the index dictionary to store the image name
    # and corresponding histograms and the images dictionary
    # to store the images themselves
    index = {}
    images = {}

    # extract a 3D RGB color histogram from the image,
    # using 8 bins per channel, normalize, and update
    # the index
    # print(type(landsat), landsat.depth(), type(drone), drone.depth())
    hist1 = cv2.calcHist(landsat, [0], None, [256], [0, 256])
    # hist1 = cv2.normalize(hist1, hist1).flatten()

    hist2 = cv2.calcHist(drone, [0], None, [256], [0, 256])
    # hist2 = cv2.normalize(hist2, hist2).flatten()

    index[landsat] = hist1
    index[drone] = hist2

    OPENCV_METHODS = (("Correlation", cv2.HISTCMP_CORREL),
                      ("Chi-Squared", cv2.HISTCMP_CHISQR),
                      ("Intersection", cv2.HISTCMP_INTERSECT),
                      ("Hellinger", cv2.HISTCMP_BHATTACHARYYA))

    # loop over the comparison methods
    for (methodName, method) in OPENCV_METHODS:
        # initialize the results dictionary and the sort
        # direction
        results = {}
        reverse = False

        # if we are using the correlation or intersection
        # method, then sort the results in reverse order
        if methodName in ("Correlation", "Intersection"):
            reverse = True

        # loop over the index
        for (k, hist) in index.items():
            # compute the distance between the two histograms
            # using the method and update the results dictionary
            d = cv2.compareHist(index["doge.png"], hist, method)
            results[k] = d

        # sort the results
        results = sorted([(v, k) for (k, v) in results.items()], reverse=reverse)

        # show the query image
        fig = plt.figure("Query")
        ax = fig.add_subplot(1, 1, 1)
        ax.imshow(images["doge.png"])
        plt.axis("off")

        # initialize the results figure
        fig = plt.figure("Results: %s" % (methodName))
        fig.suptitle(methodName, fontsize=20)

        # loop over the results
        for (i, (v, k)) in enumerate(results):
            # show the result
            ax = fig.add_subplot(1, len(images), i + 1)
            plt.imshow(images[k])
            plt.axis("off")

        # show the OpenCV methods
        plt.show()


def main():
    # Reading both images
    landsat_image = import_image("img/LC08_L1TP_016037_20211214_20211223_02_T1_B10.TIF", 10)
    dji_image, dji_meta = read_image("img/DJI_0354.JPG")

    # Getting GPS coordinates for dji drone image
    imagepath = "img/DJI_0354.JPG"

    with open(imagepath, "rb") as fin:
        img = fin.read()
        xmp_lat = str(img).find("GpsLatitude=")
        xmp_lon = str(img).find("GpsLongitude=")
        dji_lat = str(img)[xmp_lat+13:xmp_lat+24]
        dji_lon = str(img)[xmp_lon+14:xmp_lon+25]

    compare_images("img/LC08_L1TP_016037_20211214_20211223_02_T1_B10.TIF", "img/DJI_0354.JPG")


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

