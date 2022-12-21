import cv2
import os
import pathlib
def relative_path(fullpath):
    start = pathlib.Path().absolute()
    return os.path.relpath(fullpath, start)

    
img = cv2.imread(relative_path(r"C:\Users\tenno\OneDrive\Máy tính\Project\logohunter\data\test\test_brands\test_nike.png"))
print(img.shape)


#python logohunter.py  --image --input_brands ..\data\test\test_brands\test_lexus.png --input_images ..\data\test\lexus\ --output ..\data\test\test_lexus --outtxt
#python logohunter.py  --image --input_brands ..\data\test\Test\Logo --input_images ..\data\test\Test\Image\ --output ..\data\test\Test\Result --outtxt

