# TTPLA: An Aerial-Image Dataset for Detection and Segmentation of Transmission Towers and Power Lines

TTPLA is a public dataset which is a collection of aerial images on
Transmission Towers (TTs) and Powers Lines (PLs). This is the official repo of paper [TTPLA: An Aerial-Image Dataset for Detection
and Segmentation of Transmission Towers and
Power Lines](camera_ready_final.pdf). 

![Screenshot](fig/0307.jpg)

The repository includes:
* original images of TTPLA.
* pixel level annotation in COCO format.
* text files contain a list of images names after splitting to train, validate, and test.
* weights of training model using two different backbones and three different image sizes.

### Directors:
```
* `data_original_size/` contains the original images and annotations with the original size
* `data_700x700/` : contains the images and annotations with the 700x700 size.
* `data_550x550/` : contains the images and annotations with the 550x550 size.
* `data_640x360/` : contains the images and annotations with the 640x360 size.
```
### Splitting:
```
* `train.txt`: it contains the names of the train images.
* `val.txt`: it contains the names of the validation images.
* `test.txt`: it contains the names of the test images.
```
### Scripts:
```
* `resize_image_and_annotation-final.py` it is used to resize the images to target size.
* `remove_void.py` it is used to remove the void label if needed from data.
* `split_data.py` it is used to initially split the data. Then, the data is further manually filtered.
```


## Preparation data:

1. Modify `resize_image_and_annotation-final.py` to use the target image dimension. Then, call the script using
`python resize_image_and_annotation-final.py -t <images_path>`

2. Then call `remove_void.py` to remove `void` label if you would like to remove it.
`python remove_void.py -t <sized_images_path>`

3. It will produce new folder called `newjsons`, you may renamed to whatever is fit.

4. Use `split_jsons.py` which split the created `newjsons` to split into `train` , `val`, and `test` to prepare this before get the `COCO` json file.You can use the following command.
`python split_jsons.py -t jsons_no_void_700x700/`

5. Use `labelme2coco_2.py` to get the `COCO_json` that used by `Yolact`.
`python labelme2coco_2.py splitting_jsons_700x700/train_jsons/`


## Installation:
* Clone [Yolact](https://github.com/dbolya/yolact#evaluation) repository and enter it:
```
git clone https://github.com/dbolya/yolact.git
cd yolact
```
* Set up the environment using one of the following methods:
    * Using  [Anaconda](https://www.anaconda.com)
        * Run ```conda env create -f environment.yml```
    * Manually with pip
        * Set up a Python3 environment (e.g., using virtenv).
        * Install Pytorch 1.0.1 (or higher) and TorchVision.
        * Install some other packages:
            ```
          pip install cython
          pip install opencv-python pillow pycocotools matplotlib
          ```
## Train Model:
```
python eval.py --trained_model=weights/yolact_base_54_800000.pth

```

##Evaluation:

|Image Size| Backbone|configs| weights|
|:-------------:| ------------- |:-------------:| -----:|
|640 x 360 |Resnet50 | [config_img640_resnet50_aspect.py](/img640/resnet50)| [yolact_img640_secondval_399_30000_resnet50.pth](\img640\resnet50)|
|550 x 550 |Resnet50 | [config_img550_resnet50.py](/img640/resnet50)   | [yolact_img550_399_30000_resnet50.pth](/img550/resnet50) |
| 700 x 700|Resnet50 | [config_img700_resnet50.py](/img640/resnet50)  | [yolact_img700_399_30000_resnet50.pth](/img7000/resnet50) |
|640 x 360 |Resnet101| [config_img640_resnet101_aspect.py](/img640/resnet50)| [yolact_img640_secondval_399_45100_resnet101.pth](/img6400/resnet50) |
|550 x 550 |Resnet101| [config_img550_resnet101.py](/img640/resnet50)| [yolact_img550_399_45100_resnet101_b8.pth](/img550/resnet101) |
|700 x 700 |Resnet101| [config_img700_resnet101.py](/img640/resnet50)| [yolact_img700_399_45100_resnet101_b8.pth](/img700/resne101)|

##Results:
Average Precision for Different Deep Learning Models on TTPLA is reported in the following table
![results](fig/result.jpg)
![Classification falseness](fig/fig1_s20.jpg)
![Detection falseness](fig/fig3_s20.jpg)
![Segmentation falseness](fig/fig4_s20.jpg)



##Citation:
```
@inproceedings{ttpla-accv2020,
  author    = {Rabab Abdelfattah, Xiaofeng Wang, Song Wang},
  title     = {TTPLA: An Aerial-Image Dataset for Detection and Segmentation of Transmission Towers and Power Linesn},
  booktitle = {ACCV},
  year      = {2020},
}
```
##Contact:
For questions about our paper or code, please contact [Rabab Abdelfattah](rabab@email.sc.edu).
