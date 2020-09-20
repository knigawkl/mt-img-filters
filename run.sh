python3 filter.py --input imgs/hotel.jpg --output output/hotel-gauss.png --kernel matrices/gauss.txt
python3 filter.py --input imgs/hotel.jpg --output output/hotel-laplace.png --kernel matrices/laplace.txt
python3 filter.py --input imgs/hotel.jpg --output output/hotel-mean_removal.png --kernel matrices/mean_removal.txt
python3 filter.py --input imgs/hotel.jpg --output output/hotel-sobel.png --kernel matrices/sobel.txt
python3 filter.py --input imgs/hotel.jpg --output output/hotel-usredniaj.png --kernel matrices/usredniaj.txt
python3 filter.py --input imgs/grzyby.jpg --output output/grzyby-gauss.png --kernel matrices/gauss.txt
python3 filter.py --input imgs/grzyby.jpg --output output/grzyby-laplace.png --kernel matrices/laplace.txt
python3 filter.py --input imgs/grzyby.jpg --output output/grzyby-mean_removal.png --kernel matrices/mean_removal.txt
python3 filter.py --input imgs/grzyby.jpg --output output/grzyby-sobel.png --kernel matrices/sobel.txt
python3 filter.py --input imgs/grzyby.jpg --output output/grzyby-usredniaj.png --kernel matrices/usredniaj.txt

