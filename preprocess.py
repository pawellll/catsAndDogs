import cv2 as cv
import numpy as np

from Utils import Utils

IMAGES_TO_PROCESS = './train64/'
FOLDER_TO_SAVE = './preprocessed/'

def main():
	print "Preprocessing images"
	images = Utils.files_in_path(IMAGES_TO_PROCESS)

	Utils.maybe_create_directory(FOLDER_TO_SAVE)

	images_len = len(images)
	print str(images_len) + " images to process"


	i = 0;

	for image in images:
		img = cv.imread(IMAGES_TO_PROCESS + image)
		processed = preprocess_image(img)
		cv.imwrite(FOLDER_TO_SAVE + image, processed)

		i += 1
		print "processed:" + str((i/float(images_len))*100) + "%"

def preprocess_image(img):	
	cv.normalize(img,  img, 0, 255, cv.NORM_MINMAX)
	kernel = np.ones((3,3),np.float32)/9
	img = cv.filter2D(img,-1,kernel)

	return img

main()