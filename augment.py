import numpy as np
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import sys
from Utils import Utils
import scipy.misc

IMAGES_TO_PROCESS = './reduced_8000/'
FOLDER_TO_SAVE = './augmented_8000/'


def main():
	print "Augmenting images"

	images_path = Utils.files_in_path(IMAGES_TO_PROCESS)
	Utils.maybe_create_directory(FOLDER_TO_SAVE)

	images_len = len(images_path)
	print str(images_len) + " images to process"

	datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

	i = 0;

	for image_path in images_path:
		augment_and_save_image(image_path, datagen)

		i += 1
		print "preprocessed " + str(i) + " images (" + str((i/float(images_len))*100) + "%)"


def augment_and_save_image(image_path, datagen):
	img = load_img(IMAGES_TO_PROCESS + image_path)  # this is a PIL image

	x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
	x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)

	save_prefix = image_path[:-4]

	i = 0
	for batch in datagen.flow(x, batch_size=1):

		scipy.misc.imsave(FOLDER_TO_SAVE + save_prefix + '_' + str(i) + '.jpg', batch[0])

		i += 1
		if i > 3:
			break

main()
