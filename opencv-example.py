import cv2
import argparse

p = argparse.ArgumentParser()
p.add_argument('-i', '--input', required = True, help = 'Input image path')
p.add_argument('-o', '--output', required = True, help = 'Output image path')
p.add_argument('-k', '--ksize', required = True, help = 'Filter kernel size', type=int)

args = p.parse_args()

img = cv2.imread(args.input)
out_img = cv2.medianBlur(img, args.ksize)
cv2.imwrite(args.output, out_img)

