import cv2
import sys, json
import argparse
from xml.dom import minidom
import numpy as np
import os

output_folder = '.'
sized_folder = output_folder+'/'+'sized_data'
dim=(700,700)

for p in [output_folder,sized_folder]:
	if not os.path.exists(p):
		os.makedirs(p)

ap = argparse.ArgumentParser()
ap.add_argument('-t', '--path_imgs_annotation', required=True, help = 'path to imgs with annotations')
args = ap.parse_args()

images_names = [img for img in os.listdir(args.path_imgs_annotation) if img.endswith(".jpg")]

nresize = 0
for imgname in images_names:
	imgpath = args.path_imgs_annotation+'/'+imgname
	annotation_path = args.path_imgs_annotation+'/'+imgname.replace('.jpg','.json')
	if not os.path.isfile(annotation_path):
		continue
	jsndata = json.load(open(annotation_path,'r'))
	output_labled_path = sized_folder+'/'+imgname
	img = cv2.imread(imgpath)
	h,w = img.shape[0],img.shape[1]
	
	#img = cv2.resize(img, (dim[1],dim[0]), interpolation = cv2.INTER_AREA)
	if w != dim[0] or h!= dim[1]:
		print(annotation_path,w,h,' Resizing')
		nresize+=1
		img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
		for indx, p in enumerate(jsndata['shapes']):
			points = [[i[0]/w, i[1]/h] for i in p['points']]
			points = [[i[0]*dim[0], i[1]*dim[1]] for i in points]
			jsndata['shapes'][indx]['points'] = points
			points = np.int32([points])
	else:
		print(annotation_path,w,h,' Skip')
	cv2.imwrite(output_labled_path,img)
	jsndata['imageWidth'] = dim[0]
	jsndata['imageHeight'] = dim[1]
	if jsndata['imagePath'] != imgname:
		print('Error image name = '+imgname +' while json has '+jsndata['imagePath'] )
		print(annotation_path)
		exit()
	json.dump(jsndata,open(output_labled_path.replace('.jpg','.json'),'w'))
	# exit()
print('Total number of resized images = ',nresize)
