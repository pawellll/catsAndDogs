from Utils import Utils
import random
import shutil

train_folder = './data/preprocessed_9000/'
verification_folder = './data/verification_1000//'

#  number of images to select = num_to_select * 2

num_to_select = 500

files = Utils.files_in_path(train_folder)

cat_files = list()
dog_files = list()

for imageFilePath in files:
	label_name = imageFilePath[0:3]

	if label_name == "cat":
		cat_files.append(imageFilePath)
	elif label_name == "dog":
		dog_files.append(imageFilePath)

i = 0

random_dogs = random.sample(dog_files, num_to_select)
random_cats = random.sample(cat_files, num_to_select)

for dog, cat in zip(random_dogs, random_cats):
	shutil.move(train_folder + dog, verification_folder + dog)
	shutil.move(train_folder + cat, verification_folder + cat)
