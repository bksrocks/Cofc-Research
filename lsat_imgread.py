import matplotlib.pyplot as plt
import rasterio as rio
import earthpy.plot as ep
import numpy.ma as ma
import numpy as np
import cv2
import imutils


def rotateSeed(img, math, band):
    rotated = ma.masked_less_equal(img, 0)
    # (h, w) = img.shape[:2]
    # center = (w // 2, h // 2)
    # M = cv2.getRotationMatrix2D(center, 12.5, 1.0)
    # rotated = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_AREA, borderMode=cv2.BORDER_TRANSPARENT)

    # rotated = imutils.rotate(rotated, angle=12.5)
    if not math:
        for row in range(rotated.shape[0]):
            for col in range(rotated.shape[1]):
                if rotated[row, col] == -9999:
                    rotated[row, col] = rotated[0, 0]
                    print(row, col, "blank")
    else:
        if band == 10:
            rotated = (1321.0789 / np.log((774.8853/(3.3420E-04 * rotated + 0.10000)) + 1)) - 273.15
        elif band == 11:
            rotated = (1201.1442 / np.log((480.8883/(3.3420E-04 * rotated + 0.10000)) + 1))
    # for row in range(rotated.shape[0]):
    #     for col in range(rotated.shape[1]):
    #         if not math and rotated[row, col] == -9999:
    #             rotated[row, col] = rotated[0, 0]
    #             print(row, col, "blank")
    #         elif math:
    #             if rotated[row, col] == 0:
    #                 print(row, col, "blank")
    #                 pass
    #             else:
    #                 l_lambda = (3.3420E-04 * rotated[row, col] + 0.10000)
    #                 if band == 10:
    #                     rotated[row, col] = 1321.0789 / np.log((774.8853/l_lambda) + 1)
    #                 elif band == 11:
    #                     rotated[row, col] = 1201.1442 / np.log((480.8883/l_lambda) + 1)
    #                 print(row, col, rotated[row, col])
    return rotated


# # opening landsat image
# with rio.open('img/LC08_L2SP_016037_20211214_20211223_02_T1_ST_TRAD.TIF') as src:
#     dem = src.read(1)
#     # rotating image
#     dem = rotateSeed(dem, False, 0)
#     fig, ax = plt.subplots(figsize=(10, 8))
#
# # masking image to remove null numbers
# dem2 = ma.masked_less_equal(dem, 0)
#
# # plotting image
# im = ax.imshow(dem2)
# ep.colorbar(im)
# ax.set(title="12/14 - dem2")
# ax.set_axis_off()
# plt.show()

# # open lsat b10
# with rio.open('img/LC08_L1TP_016037_20211214_20211223_02_T1_B10.TIF') as b10:
#     b10 = b10.read(1)
#     # rotating image
#     b10 = rotateSeed(b10, True, 10)
#     fig, ax = plt.subplots(figsize=(10, 8))
#
# # masking image to remove null numbers
# b102 = ma.masked_less_equal(b10, 0)
#
# # plotting image
# im = ax.imshow(b10)
# ep.colorbar(im)
# ax.set(title="12/14 - b10")
# ax.set_axis_off()
# plt.show()
#
# open lsat b11
with rio.open('img/LC08_L1TP_016037_20211214_20211223_02_T1_B11.TIF') as b11:
    b11 = b11.read(1)
    # rotating image
    b11 = rotateSeed(b11, True, 11)
    fig, ax = plt.subplots(figsize=(10, 8))

# masking image to remove null numbers
b112 = ma.masked_less_equal(b11, 0)

# plotting image
im = ax.imshow(b11)
ep.colorbar(im)
ax.set(title="12/14 - b11")
ax.set_axis_off()
plt.show()

# open lsat ard st
# with rio.open('img/LC08_CU_027014_20211214_20211225_C01_V01_ST.tif') as ard:
#     ard = ard.read(1)
#     # rotating image
#     # b11 = rotateSeed(b11, True, 11)
#     fig, ax = plt.subplots(figsize=(10, 8))
#
# # masking image to remove null numbers
# # b112 = ma.masked_less_equal(b11, 0)
#
# # plotting image
# im = ax.imshow(ard)
# ep.colorbar(im)
# ax.set(title="12/14 - b11")
# ax.set_axis_off()
# plt.show()
