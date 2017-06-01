import numpy as np
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import sys
from Utils import Utils
import scipy.misc

IMAGES_TO_PROCESS = './train64/'
FOLDER_TO_SAVE = './preprocessed/'

def main():
	print "Augmenting images"
	print "From folder:" + IMAGES_TO_PROCESS
	print "To folder:" + FOLDER_TO_SAVE

	images_path = Utils.files_in_path(IMAGES_TO_PROCESS)
	Utils.maybe_create_directory(FOLDER_TO_SAVE)

	images_len = len(images_path)
	print str(images_len) + " images to process"

	datagen = ImageDataGenerator(
		featurewise_center=True,
		featurewise_std_normalization=True
    )

	i = 0;

	for image_path in images_path:
		augment_and_save_image(image_path, datagen)

		i += 1
		print "preprocessed " + str(i) + " images (" + str((i/float(images_len))*100) + "%)"

	print "From folder:" + IMAGES_TO_PROCESS
	print "To folder:" + FOLDER_TO_SAVE


def augment_and_save_image(image_path, datagen):
	img = load_img(IMAGES_TO_PROCESS + image_path)  # this is a PIL image

	x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
	x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)

	save_prefix = image_path[:-4]

	for batch in datagen.flow(x, batch_size=1):
		scipy.misc.imsave(FOLDER_TO_SAVE + image_path, batch[0])
		break
	
main()