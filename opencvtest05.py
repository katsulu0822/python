import os
import cv2



def get_filenames(directory_path):
    if not os.path.exists(directory_path):
        print("不存在")
    filenames = os.listdir(directory_path)
    return filenames


target_directory = '\k\images\set01\source'
files = get_filenames(target_directory)

for file in files:
    print(f'{target_directory}/{file}')
    img = cv2.imread(f'{target_directory}/{file}',cv2.IMREAD_GRAYSCALE)
    parts = file.split('.')
    print(f'{target_directory}/{parts[0]}-grayscale.{parts[1]}') 
    cv2.imwrite(f'{target_directory}/{parts[0]}-garyscale.{parts[1]}',img)

