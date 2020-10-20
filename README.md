# TTPLA: An Aerial-Image Dataset for Detection and Segmentation of Transmission Towers and Power Lines

TTPLA is a public dataset which is a collection of aerial images on
Transmission Towers (TTs) and Powers Lines (PLs). This is the official repository of paper [TTPLA: An Aerial-Image Dataset for Detection
and Segmentation of Transmission Towers and
Power Lines](camera_ready_final.pdf). 

![Screenshot](fig/69_00806_80.jpg)

The repository includes:
* The original images of TTPLA dataset with pixel level annotation in COCO format [here](https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1AycMYoqSydB73YA0-55sKfRxWF7jMqLU).
* Splitting text files contain a list of images names after splitting to train.txt, validate.txt, and test.txt.
* Weights of training models based on two different backbones and three different image sizes.

## Preparation data:

1. Modify `resize_image_and_annotation-final.py` to use the target image dimension (line 10). Then, call the script using
`python resize_image_and_annotation-final.py -t <images_path>`. It will produce new folder called `sized_data`.

2. Then call `remove_void.py` to remove `void` label if you would like to remove it.
`python remove_void.py -t <sized_images_path>`. It will produce new folder called `newjsons`, you may renamed to whatever is fit.

3. Based on three lists of train.txt, test.txt, and val.txt, `split_jsons.py` is used to split the created `newjsons` to three folders `train` , `val`, and `test` to prepare this before get the `COCO` json file.You can use the following command.
`python split_jsons.py -t newjsons/`. It will produce new folder called `splitting_jsons`, you may renamed to whatever is fit.

5. Use `labelme2coco_2.py` to get the `COCO_json` that used by `Yolact`.
`python labelme2coco_2.py splitting_jsons/train_jsons/`. This step is done for three folders `train_jsons` , `val_jsons`, and `test_jsons`.

 ### Tips to use our files directly
  * Install yolact [Yolact](https://github.com/dbolya/yolact#evaluation).
  * Rename `yolact` folder to `yolact700`. Based on different sizes, it can rename also to `yolact550` or `yolact640`.
  * In setp 1 in `Prepration data`, rename the generated `sized_data` folder name to `data_700x700` and upload in `yolact700/data/data_700x700`. Based on different sizes, `data_550x550` and `data_640x360` are the other named folders with different sizes.
  * Use the suitable configuration from next table according to image size and backbone. Rename the picked config file to config.py and insert in `yolact700/data/`.
  * The generated json from step 5 in `Prepration data`, rename to `train_coco_700x700`, `2_test_json700`, `2_val_json700` and put them into `yolact700/data/` if you would like to use our config file directly or you can use any name and modify the pathes into config file.
  
## Train Model:
For train image for example with size 700x700, 
```
python train.py --config=yolact_img700_val_config --batch_size=8 --resume=weights/yolact_img550_108_12253_interrupt.pth
```
For evaluation,
```
python eval.py --config=yolact_img550_secondtest_config --mask_proto_debug --trained_model=weights/weights_img550_resnet50/yolact_img550_400_30061_resnet50_sep7_2217.pth --fast_nms=false

```

## Evaluation:

|Image Size| Backbone|configs| weights|
|:-------------:| ------------- |:-------------:| -----:|
|640 x 360 |Resnet50 | [config_img640_resnet50_aspect.py](https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1ocoYiTDFBcdI8Es8dZlMbsbFGkaLKw98)| [yolact_img640_secondval_399_30000_resnet50.pth](https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1IDfQlBJ2VAIpyaOSUs2Ecmf_rsl8nSdc)|
|550 x 550 |Resnet50 | [config_img550_resnet50.py](https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1buxmIli7cxiFwJ7krOCTOojwgDeR2AUM)   | [yolact_img550_399_30000_resnet50.pth](https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1mKYRP7LOVgrFN5Vsug-tyI6XDEZ8c62k) |
|700 x 700|Resnet50 | [config_img700_resnet50.py](https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1NCe8W7QKlDhDF-nrH2iLAr0kiHdC6T7w)  | [yolact_img700_399_30000_resnet50.pth](https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1y8g-KepFdcSBWKRdHTHB8vygjKsFTyKr) |
|640 x 360 |Resnet101| [config_img640_resnet101_aspect.py](https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1sq3WSdH-wqRLbIaZO9g4uBYA6WQec3uC)| [yolact_img640_secondval_399_45100_resnet101.pth](https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1IDfQlBJ2VAIpyaOSUs2Ecmf_rsl8nSdc) |
|550 x 550 |Resnet101| [config_img550_resnet101.py](https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1XM7ryEokOe98Y6XNmx9qvuK8rPujoJvL)| [yolact_img550_399_45100_resnet101_b8.pth](https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1zP4usEnaAUeGuqq179iLocy2J5TO4eJH) |
|700 x 700 |Resnet101| [config_img700_resnet101.py](https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1QfPvi2FTJv1JByqM70qM7nQjGpNI_kNi)| [yolact_img700_399_45100_resnet101_b8.pth](https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1IDfQlBJ2VAIpyaOSUs2Ecmf_rsl8nSdc)|

## Results:

Average Precision for Different Deep Learning Models on TTPLA is reported in the following table
![results](fig/result.jpg)


![Classification falseness](fig/mod_fig1.png {width=40px height=400px})
![Detection falseness](fig/mod_fig3.png)
![Segmentation falseness](fig/mod_fig4.png)



## Citation:
```
@inproceedings{ttpla-accv2020,
  author    = {Rabab Abdelfattah, Xiaofeng Wang, Song Wang},
  title     = {TTPLA: An Aerial-Image Dataset for Detection and Segmentation of Transmission Towers and Power Linesn},
  booktitle = {ACCV},
  year      = {2020},
}
```
## Contact:
For questions about our paper or code, please contact [Rabab Abdelfattah](rabab@email.sc.edu).
