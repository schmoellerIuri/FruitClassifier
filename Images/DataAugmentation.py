from skimage.io import imread_collection
from skimage.util import montage
import numpy as np
import matplotlib.pyplot as plt
import cv2

def scale_range (a, min:float, max:float):
    amin = np.min(a)
    amax = np.max(a)
    a += -(amin)
    a /= amax / (max - min)
    a += min
    return a

def show_montage (col):
    Montage = montage(col, grid_shape=(4, 5), channel_axis=-1)
    plt.figure(figsize=(10, 10))
    plt.imshow(Montage)
    plt.axis('off')
    plt.show()

def gammaTransform (img, gamma):
    img = img.astype('float')
    img = np.power(img, gamma)
    img = scale_range(img, 0, 255).astype('uint8')
    return img

def logarithmTransform(img, c):
    img = img.astype('float')
    img = c * np.log(1 + img)
    img = scale_range(img, 0, 255).astype('uint8')
    return img

def negative2zero(img):
    img = img.copy()
    img[img < 0] = 0
    return img

def calculate_target_size(img_size, kernel_size):
    num_pixels = 0

    # From 0 up to img size (if img size = 224, then up to 223)
    for i in range(img_size):
        # Add the kernel size (let's say 3) to the current i
        added = i + kernel_size
        # It must be lower than the image size
        if added <= img_size:
            # Increment if so
            num_pixels += 1

    return num_pixels

def convolve(img, kernel):
    # Assuming a rectangular image
    tgt_size = calculate_target_size(
        img_size=img.shape[0],
        kernel_size=kernel.shape[0]
    )
    # To simplify things
    k = kernel.shape[0]

    # 2D array of zeros
    convolved_img = np.zeros(shape=(1000, 1000))

    # Iterate over the rows
    for i in range(tgt_size):
        # Iterate over the columns
        for j in range(tgt_size):
            # img[i, j] = individual pixel value
            # Get the current matrix
            mat = img[i:i+k, j:j+k]

            convolved_img[i, j] = np.mean(mat)

    return convolved_img

def save_image(img, i, img_sequence):
    filePath = fruitName + "/" + fruitId + "-" + str(img_sequence) + "-" + versions[i%4] + "-" + backgrounds[i%2] + ".png"
    plt.imsave(filePath, img)

fruitName = 'Tomato'

#your path 
col_dir = f'{fruitName}/*.png'
#creating a collection with the available images
col = imread_collection(col_dir)

backgrounds = ["B", "W"]

versions = ["V1", "V1", "V2", "V2"]

fruitId = col.files[0].split("-")[0].split("\\")[1]

lastImgSequence = int(col.files[-1].split("-")[1])

images_gamma = np.array(col)

lastImgSequence += 1

j = 0

for i in range(len(images_gamma)):
    images_gamma[i] = gammaTransform(images_gamma[i], 2)
    if(j == 4): 
        lastImgSequence += 1
        j = 0
    save_image(images_gamma[i], i, lastImgSequence)
    j += 1

images_log = np.array(col)
j = 0
lastImgSequence += 1

for i in range(len(images_log)):
    images_log[i] = logarithmTransform(images_log[i], 1)
    if(j == 4): 
        lastImgSequence += 1
        j = 0
    save_image(images_log[i], i, lastImgSequence)
    j += 1

kernel = np.ones((5,5),np.float32)/25

images_conv = np.array(col)
j = 0
lastImgSequence += 1	

for i in range(len(images_conv)):
    images_conv[i] = cv2.filter2D(images_conv[i],-1,kernel)
    if(j == 4): 
        lastImgSequence += 1
        j = 0
    save_image(images_conv[i], i, lastImgSequence)
    j += 1



