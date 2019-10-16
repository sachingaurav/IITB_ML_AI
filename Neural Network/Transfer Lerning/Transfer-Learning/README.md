# Transfer Learning

implement transfer learning in Python. For this implementation, we will use the flower recognition dataset from Kaggle. This dataset has around 4000 images from 5 different classes, namely daisy, dandelion, rose, sunflower and tulip. 

we conducted two transfer learning experiments. In the first experiment, we removed the last fully connected layers of ResNet (which had learnt how to classify the 1000 ImageNet images). Instead, we added our own pooling, fully connected and a 5-softmax layer and trained only those. Notice that we got very good accuracy in just a few epochs. In case we weren't satisfied with the results, we could modify this network further (add an FC layer, modify the learning rate, replace the global average pooling layer with max pool, etc.).

 

In the second experiment, we froze the first 140 layers of the model (i.e. used the pre-trained ResNet weights from layers 1-140) and trained the rest of the layers. Note that while updating the pre-trained weights, we should use a small learning rate. This is because we do not expect the weights to change drastically (we expect them to have learnt some generic patterns, and want to tune them only a little to accommodate for the new task). 