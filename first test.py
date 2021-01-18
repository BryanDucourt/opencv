import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('./image/3.png')
# cv.imshow('test', img)
# k = cv.waitKey(0)

# cv.imshow('test', img)
# k = cv.waitKey(0)  # wait for keyboard
# if k == 27:  # esc
#     cv.destroyAllWindows()
# elif k == ord('s'):
#     cv.imwrite('messigray.png', img)
#
#     cv.destroyAllWindows()


# opencv follows BGR order, and matplotlib follows RGB order, so if
# you want to display a colored picture with matplotlib, you'll need to convert it to
# RGB mode.

b, g, r = cv.split(img)
img2 = cv.merge([r, g, b])

plt.imshow(img2, interpolation='bicubic')
plt.xticks([]), plt.yticks([])
plt.show()

# cv.namedWindow('image', cv.WINDOW_NORMAL)
# cv.imshow('image', img)
# cv.waitKey(0)
# cv.destroyAllWindows()
