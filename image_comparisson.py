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
    # lsat = np.histogram(landsat, bins=50, range=None, normed=None, weights=None, density=None)
    drone = np.histogram(drone, bins='auto')
    plt.figure()
    plt.title("Grayscale Histogram")
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")
    plt.plot(drone)
    plt.xlim([0, 256])
    # normalize the histogram
    drone /= drone.sum()

    # plot the normalized histogram
    plt.figure()
    plt.title("Grayscale Histogram (Normalized)")
    plt.xlabel("Bins")
    plt.ylabel("% of Pixels")
    plt.plot(drone)
    plt.xlim([0, 256])
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

    compare_images(landsat_image, dji_image)


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

