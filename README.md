## SRGAN
Implementation of _Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network_ using Keras (tf) for my postgraduate project in Universitat Politècnica de Catalunya.

<p align="center">
    <img src="https://github.com/calebemonteiro/AIDL_Project/blob/master/resources/architecture.jpg" width="640"\>
</p>

Paper: https://arxiv.org/abs/1609.04802

## Requirements:
    You will need the following to run the above:
    Keras==2.3.1
    tensorflow==2.1.0
    opencv-python==4.3.0
	matplotlib==3.3.0
	argparse==1.4.0
	numpy==1.19.1

## File Structure:
    Model.py   : Contains Generator and Discriminator Network
    Utils.py   : Contains utilities to process images
    train.py   : Used for training the model


## Usage:
    
    Note : During the training the images generated and model will be saved into the directories "images" and "model" following the
	"sample_interval" parameter.
    
     * Training:
        Run below command to train model. Set parameters accordingly.
        > python train.py --train_folder='./data/train/' --batch_size=8 --epochs=2000 --sample_interval=25



## Output:
Below are few results (from epoch 0 to 5000):

#### Epoch 0
<p align="left">
    <img src="https://github.com/calebemonteiro/AIDL_Project/blob/master/resources/epoch_0.png" width="480"\>
</p>

#### Epoch 500
<p align="left">
    <img src="https://github.com/calebemonteiro/AIDL_Project/blob/master/resources/epoch_500.png" width="480"\>
</p>

#### Epoch 1000
<p align="left">
    <img src="https://github.com/calebemonteiro/AIDL_Project/blob/master/resources/epoch_1000.png" width="480"\>
</p>

#### Epoch 1500
<p align="left">
    <img src="https://github.com/calebemonteiro/AIDL_Project/blob/master/resources/epoch_1500.png" width="480"\>
</p>

#### Epoch 2000
<p align="left">
    <img src="https://github.com/calebemonteiro/AIDL_Project/blob/master/resources/epoch_2000.png" width="480"\>
</p>

#### Epoch 5000
<p align="left">
    <img src="https://github.com/calebemonteiro/AIDL_Project/blob/master/resources/epoch_5000.png" width="480"\>
</p>
