import cv2
import sys, json
import argparse
import numpy as np
import os

output_folder = 'splitting_jsons'

train_folder = output_folder+'/'+'train_jsons'
val_folder = output_folder+'/'+'val_jsons'
test_folder = output_folder+'/'+'test_jsons'

ap = argparse.ArgumentParser()
ap.add_argument('-t', '--path_annotation_jsons', required=True, help = 'path to jsons annotations')
args = ap.parse_args()

jsons_names = [js for js in os.listdir(args.path_annotation_jsons) if js.endswith(".json")]

train = []
with open('train.txt','r') as hndl:
	for l in hndl:
		train.append(l.strip())

test = []
with open('test.txt','r') as hndl:
	for l in hndl:
		test.append(l.strip())

val = []
with open('val.txt','r') as hndl:
	for l in hndl:
		val.append(l.strip())

print(len(train),len(test),len(val),len(jsons_names),len(train)+len(test)+len(val))
for p in [output_folder,train_folder,val_folder,test_folder]:
	if not os.path.exists(p):
		os.makedirs(p)

for t in jsons_names:
	if t in train:
		os.system('cp '+args.path_annotation_jsons+'/'+t+' '+train_folder+'/'+t)
	if t in test:
		os.system('cp '+args.path_annotation_jsons+'/'+t+' '+test_folder+'/'+t)
	if t in val:
		os.system('cp '+args.path_annotation_jsons+'/'+t+' '+val_folder+'/'+t)
