# import libraries
import argparse
import cv2

# Construct the argument parser
ap = argparse.ArgumentParser()

# add arguments
ap.add_argument('-i', '--image', type=str, required=True, help="path to input image")
ap.add_argument('-s', '--scharr', type=int, default=0)

# parse the arguments
args = vars(ap.parse_args())

# load image
image = cv2.imread(args['image'])

# convert BGR to GRAY format
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# show gray image
cv2.imshow("Gray", gray)

# set kernel size
ksize = -1 if args['scharr'] > 0 else 3
# Compute the gradient across x and y axis
gX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=ksize)
gY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=ksize)

# convert the gradient magnitude back to unsigned 8-bit from floating point.
gX = cv2.convertScaleAbs(gX)
gY = cv2.convertScaleAbs(gY)

# combine the gradient into single image
combined = cv2.addWeighted(gX, 0.5, gY, 0.5, 0)

# show the output image
cv2.imshow("Sobel/Scharr X", gX)
cv2.imshow("Sobel/Scharr Y", gY)
cv2.imshow("Sobel/Scharr combined", combined)
cv2.waitKey(0)
