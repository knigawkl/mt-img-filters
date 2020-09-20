import sys
import cv2
import numpy as np
import argparse


def load_args():
    p = argparse.ArgumentParser()
    p.add_argument('-i', '--input', required = True, help = 'Input image path')
    p.add_argument('-o', '--output', required = True, help = 'Output image path')
    p.add_argument('-k', '--kernel', required = True, help = 'Kernel path')
    return p.parse_args()


def load_matrix(path: str):
    return np.loadtxt(path, int)


def load_img(path: str):
    # return cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB) 
    return cv2.imread(path)


def save_img(path: str, img):
    cv2.imwrite(path, img)


def filter_img(img: np.array, kernel: np.array):
    print(f"Shape pf the image to be filtered: {img.shape}")
    print(img.shape)
    img_h, img_w = img.shape[0], img.shape[1]
    kernel_h, kernel_w = kernel.shape[0], kernel.shape[1]
    border_h = kernel_h // 2
    border_w = kernel_w // 2
    
    image_pad = np.pad(img, pad_width=((kernel_h // 2, kernel_h // 2),
                                       (kernel_w // 2, kernel_w // 2)), 
                                       mode='constant', 
                                       constant_values=0).astype(np.float32)
    out = np.zeros(image_pad.shape)

    for i in range(border_h, image_pad.shape[0]-border_h):
        for j in range(border_w, image_pad.shape[1]-border_w):
            x = image_pad[i-border_h:i-border_h+kernel_h, j-border_w:j-border_w+kernel_w]
            x = x.flatten()*kernel.flatten()
            out[i][j] = x.sum()

    return out[border_h:-border_h,border_w:-border_w]


if __name__ == "__main__":
    args = load_args()
    img = load_img(args.input)
    print(f"Input image shape is {img.shape}")
    kernel = load_matrix(args.kernel)
    print(f"Kernel shape is {kernel.shape}")
    out = np.zeros_like(img, dtype=np.float32)
    for c in range(3):
        out[:, :, c] = filter_img(img[:, :, c], kernel) 
    print("wynikowa macierz")
    print(out.shape)
    save_img(args.output, out)

