import cv2
import numpy as np
import argparse


p = argparse.ArgumentParser()
p.add_argument('-i', '--input', required = True, help = 'Input image path')
p.add_argument('-o', '--output', required = True, help = 'Output image path')
p.add_argument('-k', '--kernel', required = True, help = 'Kernel path')
args = p.parse_args()

img = cv2.imread(args.input)
kernel = np.loadtxt(args.kernel, int)

out_img = cv2.filter2D(img, -1, kernel)
cv2.imwrite(args.output, out_img)

