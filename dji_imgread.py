from thermal_base import ThermalImage
from matplotlib import pyplot as plt
import earthpy.plot as ep
import numpy as np

# https://github.com/detecttechnologies/thermal_base

dji_img_sample = "img/DJI_0354.JPG"

# dji_img_sample =

image = ThermalImage(image_path=dji_img_sample, camera_manufacturer="dji")
thermal_np = image.thermal_np           # The temperature matrix as a np array
raw_sensor_np = image.raw_sensor_np     # The raw thermal sensor excitation values as a np array
meta = image.meta

print(raw_sensor_np.shape)

fig, ax = plt.subplots(figsize=(10, 8))
im = plt.imshow(thermal_np, interpolation='nearest')
# plt.imshow(raw_sensor_np, interpolation='nearest')
ep.colorbar(im)
ax.set(title="12/14 - dji")
ax.set_axis_off()
plt.show()

# np.savetxt("thermap.txt", thermal_np)
