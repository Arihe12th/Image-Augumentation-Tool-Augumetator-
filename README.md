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
        16. Resize.
        17.Crop Center.    



