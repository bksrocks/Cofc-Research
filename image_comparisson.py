from lsat_imgread import import_image
from dji_imgread import read_image
import matplotlib.pyplot as plt
import earthpy.plot as ep
from PIL import Image
from PIL.ExifTags import TAGS
# from libxmp import XMPFiles, consts


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

    print(float(dji_lat), float(dji_lon))

    # lat_start = 33.176999 - float(dji_lat)
    # lon_start = -80.106913 - float(dji_lon)

    lat_pix = (34.123 - 33.825) / landsat_image.shape[0]
    lon_pix = (80.913 - 78.861) / landsat_image.shape[0]

    lat_pix_v = (34.123 - 32.518) / landsat_image.shape[1]
    lon_pix_v = (81.336 - 80.913) / landsat_image.shape[1]

    print(lat_pix, lon_pix)
    print(lat_pix_v, lon_pix_v)

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

