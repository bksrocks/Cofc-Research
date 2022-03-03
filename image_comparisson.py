from lsat_imgread import import_image
from dji_imgread import read_image
import matplotlib.pyplot as plt
import numpy as np
from mycolorpy import colorlist as mcp


def compare_images(landsat, drone):
    plt.figure()
    plt.title("Histogram Comparisson")
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")
    # bins = np.linspace(0, 1, 10)
    plt.subplot(1, 2, 1)
    plt.hist(landsat, label='landsat', color=mcp.gen_color(cmap="Blues", n=landsat.shape[1]))
    # plt.hist(landsat, bins, label='landsat', color=mcp.gen_color(cmap="Blues", n=landsat.shape[1]))
    # plt.legend(loc='upper right')
    plt.subplot(1, 2, 2)
    plt.hist(drone, label='drone', color=mcp.gen_color(cmap="Greens", n=drone.shape[1]))
    # plt.hist(drone, bins, label='drone', color=mcp.gen_color(cmap="Greens", n=drone.shape[1]))
    # plt.legend(loc='upper right')
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

