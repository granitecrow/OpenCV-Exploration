import cv2 as cv
import os

imageFolder = 'images'
folders = os.listdir(imageFolder)
print(folders)

for folder in folders:
    path = imageFolder + '/' + folder
    images = []
    myList = os.listdir(path)
    print(f'total number of images detected: {len(myList)}')
    for image in myList:
        current = cv.imread(f'{path}/{image}')
        images.append(current)
    
    stitcher = cv.Stitcher.create()
    (status, result) = stitcher.stitch(images)
    if (status == cv.STITCHER_OK):
        print('Panorama generated.')
        #percent by which the image is resized
        # scale_percent = 40
        # width = int(result.shape[1] * scale_percent / 100)
        # height = int(result.shape[0] * scale_percent / 100)
        # dsize = (width, height)
        # output = cv.resize(result, dsize)
        # cv.imshow("result", output)

        cv.imwrite(f'{path}/result.png', result)
    else:
        print('Unable to generate panorama.')
    
    cv.waitKey(0)