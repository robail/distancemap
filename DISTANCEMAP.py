from __future__ import print_function
from skimage.feature import peak_local_max
from skimage.morphology import watershed
from scipy import ndimage
import argparse
import imutils
import cv2
image = cv2.imread('w.png')
print(image)

shifted = cv2.pyrMeanShiftFiltering(image, 21, 51)
cv2.imshow("Input", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray = cv2.cvtColor(shifted, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
cv2.imshow("Thresh", thresh)


cv2.waitKey(0)
cv2.destroyAllWindows()
print(thresh)

map = ndimage.distance_transform_edt(thresh)
cv2.imshow("Thresh", map)
cv2.waitKey(0)
cv2.destroyAllWindows()

