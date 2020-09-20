python3 opencv-custom.py --input imgs/lenna.png --output output/lenna-usredniaj-cv.png --kernel matrices/usredniaj.txt
python3 opencv-custom.py --input imgs/lenna.png --output output/lenna-gauss-cv.png --kernel matrices/gauss.txt
python3 opencv-custom.py --input imgs/lenna.png --output output/lenna-sobel-cv.png --kernel matrices/sobel.txt
python3 opencv-custom.py --input imgs/lenna.png --output output/lenna-mean_removal-cv.png --kernel matrices/mean_removal.txt
python3 opencv-custom.py --input imgs/lenna.png --output output/lenna-laplace-cv.png --kernel matrices/laplace.txt
