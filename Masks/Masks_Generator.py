import cv2
from skimage.io import imread_collection
import os

def GetImagesMask(images, params, class_name):
  masks = []
  i = 0
  limit = 0
  
  kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (params[0], params[0]))
  operation = cv2.MORPH_CLOSE
  for image in images:
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if (i % 2) == 0:
      limit = params[1]
    else:
      limit = params[2]

    if(class_name == 'Lemon' and i == len(images)-1):
      limit = params[3]
      
    ret, thresh = cv2.threshold(img, limit, 255, cv2.THRESH_BINARY)
    if (i % 2) == 1:
      thresh = cv2.bitwise_not(thresh)

    thresh = cv2.morphologyEx(thresh, operation, kernel)   
    i += 1

    masks.append(thresh)
    
  return masks

fruits = ['Apple', 'Lemon', 'Banana', 'Clementine', 'Tomato']

for fruit in fruits:
  images = imread_collection(f'{fruit}/*.png')

  params = {'Apple':(45,10,85),'Lemon':(43,80,140,220),'Banana':(99,60,90),'Clementine':(45,63,125),'Tomato':(81,20,80)}

  masks = GetImagesMask(images, params[fruit], fruit)

  # Create a folder called {Fruits}_Masks for each fruit
  folder_name = f'{fruit}_Masks'
  if not os.path.exists(folder_name):
    os.makedirs(folder_name)

  # Save each mask image to the folder
  for i, mask in enumerate(masks):
    filename = images.files[i].split('\\')[1].split('.')[0]
    cv2.imwrite(f'{folder_name}/{filename}_MASK.png', mask)
