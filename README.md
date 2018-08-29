# Image-Augumentation-Tool-Augumetator-
Augumentation Tool for generating dataset to traing Objection classification model Using FRCNN


Image augmentation tool:

Applications:

1.)Used to transform images to different forms like rotate,shear etc to increase the dataset size to train Object classification        
   model in caffe.
2.)We need Image datasets to annotated using labelimg tool (you can download from this link:https://github.com/tzutalin/labelImg) 
   you can use this tool to annotate images with PASCAL VOC xml format to train FRCNN model in caffe .
3.)This augmentation tool helps in balancing data, increase datasets if we have limited data, help to feed images with different 
   perspective, helps in reducing false positive of classification model and increase accuracy in dataset perspective.
   Provide 17 types of Augmentation.
   
   Different types of Augmentation:
        1.Horizontal Flip.
        2.Vertical Flip.
        3.Rotate 90 Degree.
        4.Brightness.
        5.Contrast.
        6.Hue
        7.Gamma.
        8.Saturation.
        9.Rotate to angle.
        10.Rotate to Bounding box.
        11.Transpose.
        12.Salt and pepper.
        13.Shading.
        14.Shear right.
        15.Shear left.
        16.Resize.
        17.Crop Center.    

Dependencies to Install this tool:
Tool works with python 2.7.

it is better if have a seperate environment for python(use anaconda or virtualenv)
reference links for setting up environment:
conda:
https://medium.freecodecamp.org/why-you-need-python-environments-and-how-to-manage-them-with-conda-85f155f4353c

virtualenv:
https://virtualenv.pypa.io/en/stable/userguide/

Inside this environment you can install all dependency libraries:
use pip to install libraries inside environment.


pip install -U pip
pip install -U matplotlib
pip install -U imgaug
pip install -U numpy
pip install -U cv2
pip install -U qt4
pip install -U imutils
pip install -U shutil
pip install -U elementree

running tool:
download the source code and run it in the environment where you set all dependencies the tool starts working 




NOTE:
1.You can’t generate xml for Horizontal flip , vertical flip,rotate 90 degree,crop centre because the change in image is very large the annotated bound box don’t fit objects objects go out of bounding box.

2.Other augmentation are configure to fit bounding box after augmenting so xml can be generated in PASCAL VOC format so you can make use of it.

3.There are few things have to fixed in terms of GUI and options but tool is working fine you can check for fixes and upgrade predioacally.





