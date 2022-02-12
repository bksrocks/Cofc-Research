from thermal_base import ThermalImage
from matplotlib import pyplot as plt
import earthpy.plot as ep
import numpy as np


def normalize_data(data):
    # normalizes the data
    return (data - np.min(data)) / (np.max(data) - np.min(data))


def read_image(image_path):
    """This function transforms a DJI Mavic 2 Enterprise Due drone image into a numpy array.
    input: JPG thermal image path.
    output: temperature numpy array."""

    # Uses the library thermal_base to process the DJI image.
    # (https://github.com/detecttechnologies/thermal_base)

    image = ThermalImage(image_path=image_path, camera_manufacturer="dji")

    # thermal_np = image.thermal_np           # The temperature matrix as a np array
    raw_sensor_np = image.raw_sensor_np     # The raw thermal sensor excitation values # as a np array
    meta = image.meta                     # Image metadata

    return normalize_data(raw_sensor_np), meta


def main():

    # import and process drone image
    dji_img_sample, meta = read_image("img/DJI_0354.JPG")

    # plot the image
    fig, ax = plt.subplots(figsize=(10, 8))
    im = plt.imshow(dji_img_sample, interpolation='nearest')
    ep.colorbar(im)
    ax.set(title="12/14 - dji")
    ax.set_axis_off()
    plt.show()


# main ()
