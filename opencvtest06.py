import os
import cv2



target_directory = '\k\images\set01\source'
os.chdir(target_directory)
filenames = os.listdir()

image_list = []
for filename in filenames:
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    image_list.append(img)

target_directory = '../output'
os.chdir(target_directory)

for filename, image in zip(filenames, image_list):
    print(filename)
    parts = filename.split('.')
    print(f'{target_directory}/{parts[0]}-grayscale.{parts[1]}') 
    cv2.imwrite(f'{target_directory}/{parts[0]}-garyscale.{parts[1]}',image)

