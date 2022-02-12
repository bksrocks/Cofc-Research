import matplotlib.pyplot as plt
import rasterio as rio
import earthpy.plot as ep
import numpy.ma as ma
import numpy as np
import imutils


def rotate_image(img):
    # rotates image
    return imutils.rotate(img, angle=12.5)


def normalize_data(data):
    # normalizes the data
    return (data - np.min(data)) / (np.max(data) - np.min(data))


def import_image(image_path, band):
    with rio.open(image_path) as img:
        image = img.read(1)
        # image_array = np.array(image, dtype="float64")
        # rotating image
        image_array = rotate_image(image)

    # converting temperatures from Kelvin to Celcius
    # if band == 10:
    #     image_array = (1321.0789 / np.log((774.8853 / (3.3420E-04 * image_array + 0.10000)) + 1)) - 273.15
    # elif band == 11:
    #     image_array = (1201.1442 / np.log((480.8883 / (3.3420E-04 * image_array + 0.10000)) + 1))

    image_array = normalize_data(image_array)

    return ma.masked_less_equal(image_array, 0)


def main():

    # open landsat band 10 image
    b10 = import_image('img/LC08_L1TP_016037_20211214_20211223_02_T1_B10.TIF', 10)

    # plotting image
    fig, ax = plt.subplots(figsize=(10, 8))
    im = ax.imshow(b10)
    ep.colorbar(im)
    ax.set(title="12/14 - b10")
    ax.set_axis_off()
    plt.show()


# main()
