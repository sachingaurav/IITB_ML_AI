# Building-a-CNN
Train CNNs using Python and Keras using CIFAR-10 dataset which has 60000 (32 x 32) colour images of 10 classes

Define your own convolutional layers in Keras and train those layers on the CIFAR-10 dataset. Implement everything on a GPU.

Get familiar with CNNs in Keras: The MNIST dataset
Setting up notebook on a GPU
Conduct experiments with the CIFAR-10 dataset:
Build a base model using the CIFAR-10 dataset
Experiment with hyperparameters and draw observations

The VGG-16 was trained on the ImageNet challenge (ILSVRC) 1000-class classification task. The network takes a (224, 224, 3) RBG image as the input. The '16' in its name comes from the fact that the network has 16 layers with trainable weights - 13 convolutional layers and 3 fully connected ones (the VGG team had tried many other configurations, such as the VGG-19, which is also quite popular)

Thus, conv3-64 means 64 (3, 3) square filters.  Note that all the conv layers in VGG-16 use (3, 3) filters and that the number of filters increases in powers of two (64, 128, 256, 512). 
In all the convolutional layers, the same stride length of 1 pixel is used with a padding of 1 pixel on each side, thereby preserving the spatial dimensions (height and width) of the output.

After every set of convolutional layers, there is a max pooling layer. All the pooling layers in the network use a window of 2 x 2 pixels with stride 2. Finally, the output of the last pooling layer is flattened and fed to a fully connected (FC) layer with 4096 neurons, followed by another FC layer of 4096 neurons, and finally to a 1000-softmax output. The softmax layer uses the usual cross-entropy loss. All layers apart from the softmax use the ReLU activation function.

Experiment - I: Using dropouts after conv and FC layers
In the first experiment, we will use dropouts both after the convolutional and fully connected layers.

Experiment - II: Remove the dropouts after the convolutional layers (but retain them in the FC layer). Also, use batch normalization after every convolutional layer.

Experiment - III: Use batch normalization and dropouts after every convolutional layer. Also, retain the dropouts in the FC layer

Experiment - IV: Remove the dropouts after the convolutional layers and use L2 regularization in the FC layer. Retain the dropouts in FC.

Experiment-V: Dropouts after conv layer, L2 in FC, use BN after convolutional layer

Experiment-VI: Add a new convolutional layer to the network. Note that by a 'convolutional layer', the professor is referring to a convolutional unit with two sets of Conv2D layers with 128 filters each 

Experiment - VII: Add more feature maps to the conv layers: from 32 to 64 and 64 to 128.


The results of the experiments done so far are summarised below. Note that 'use BN' refers to using BN after the convolutional layers, not after the FC layers.

Experiment - I (Use dropouts after conv and FC layers, no BN): 
Training accuracy =  84%, validation accuracy  =  79%
Experiment - II (Remove dropouts from conv layers, retain dropouts in FC, use BN): 
Training accuracy =  98%, validation accuracy  =  79%
Experiment - III (Use dropouts after conv and FC layers, use BN):
Training accuracy =  89%, validation accuracy  =  82%
Experiment - IV (Remove dropouts from conv layers, use L2 + dropouts in FC, use BN):
Training accuracy = 94%, validation accuracy = 76%.
Experiment-V: Dropouts after conv layer, L2 in FC, use BN after convolutional layer
Train accuracy =  86%, validation accuracy = 83%
Experiment-VI: Add a new convolutional layer to the network
Train accuracy =  89%, validation accuracy = 84
Experiment-VII: Add more feature maps to the convolutional layers to the network
Train accuracy =  92%, validation accuracy = 84%

