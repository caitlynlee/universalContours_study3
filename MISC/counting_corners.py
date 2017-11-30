import harris_corners as hc
import os
import shutil

cwd = os.getcwd()
image_dir = os.path.join(os.pathdirname(cwd), "STIMULI", "images")


for filename in os.listdir(image_dir):
	if filename == ".DS_Store":
		image_path = os.path.join(image_dir, filename)
		os.remove(image_path)

	else:
		image_path = os.path.join(image_dir, filename)

		num_corners = hc.count_corners(image_path)

		#print "moving file! corners: " + str(num_corners)
		corner_dir = os.path.join(image_dir, str(num_corners))

		if (os.path.exists(corner_dir)):
			shutil.move(image_path, os.path.join(corner_dir,filename))
		else:
			os.mkdir(corner_dir)
			shutil.copy(image_path, os.path.join(corner_dir,filename))
