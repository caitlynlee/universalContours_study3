import harris_corners as hc
import os
import shutil

image_dir = ("/Users/caitlyn/Documents/"
				"Dartmouth/wheatlab/universal_contours/images/")
output_dir = ("/Users/caitlyn/Documents/"
				"Dartmouth/wheatlab/universal_contours/sorted_images/")

if not os.path.exists(output_dir):
	os.mkdir(output_dir)

for file in os.listdir(image_dir):
	if file == ".DS_Store": 
		image_path = os.path.join(image_dir, file)
		os.remove(image_path)

	else:
		image_path = os.path.join(image_dir, file)
	
		num_corners = hc.count_corners(image_path)

		if num_corners == 13:
			print "moving file! corners: " + str(num_corners)
			corner_dir = os.path.join(output_dir, str(num_corners))
			
			if (os.path.exists(corner_dir)):
				shutil.move(image_path, os.path.join(corner_dir,file))
			else: 
				os.mkdir(corner_dir)
				shutil.copy(image_path, os.path.join(corner_dir,file))
				
