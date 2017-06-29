import cv2 as cv
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import sys
from Utils import Utils
import scipy.misc
from scipy import ndimage

IMAGES_TO_PREPROCESS = './data/original_9000/'
FOLDER_TO_SAVE = './data/preprocessed_9000/'

size_x = 64
size_y = 64


def main():

	images_path = Utils.files_in_path(IMAGES_TO_PREPROCESS)
	Utils.maybe_create_directory(FOLDER_TO_SAVE)

	images_len = len(images_path)
	print str(images_len) + " images to process"

	# need to fit datagen
	# datagen = ImageDataGenerator(
	# 	featurewise_center=True,
	#	featurewise_std_normalization=True
	#	samplewise_center=True,
	#	samplewise_std_normalization=True
	#)

	# load all images (9000 = 8000 train + 1000 verification) to fit 
	# datagen.fit(x)

   	i = 0;

	for image_path in images_path:
		# preprocessed_image = preprocess(image_path, datagen)
		# scaled_image = scale_image(preprocessed_image)
		# save_image(scaled_image, image_path)
	
		full_path = IMAGES_TO_PREPROCESS + image_path

		print "preprocessing:"  + full_path

		im = cv.imread(full_path)
		im = scale_image(im)
		cv.imwrite(FOLDER_TO_SAVE + image_path, im)

		i += 1
		print "preprocessed " + str(i) + " images (" + str((i/float(images_len))*100) + "%)"

	print "From folder:" + IMAGES_TO_PREPROCESS
	print "To folder:" + FOLDER_TO_SAVE


def preprocess(image_path, datagen):
	img = load_img(IMAGES_TO_PROCESS + image_path)  # this is a PIL image

	x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
	x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)

	save_prefix = image_path[:-4]

	for batch in datagen.flow(x, batch_size=1):
		return batch[0]


def save_image(image, image_path):
	scipy.misc.imsave(FOLDER_TO_SAVE + image_path, image)


def scale_image(image):
	scaled = cv.resize(image, (size_x, size_y))			
	return scaled;


if __name__ == '__main__':
	main()
