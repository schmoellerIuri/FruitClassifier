# Fruit Classifier
Project of a fruits images linear classifier, using convoulutional residual neural networks .

**<h1>1 - Classes</h1>**

These are the following classes and its ids:

0 banana 🍌

1 clementine 🍊

2 lemon 🍋

3 tomato 🍅

4 strawberry 🍓

5 apple 🍎

6 pineapple 🍍

7 pear 🍐

8 papaya 🥭

9 coconut 🥥

**<h1>2 - Running Environment and implementation</h1>**

**Our image database is located in this current repository, it contains about to 650 images. Is important to point that a data augmentation was made to improve the amount of training data**

**<h2>Running environment</h2>**

To run our project you just have to access:

<a href="https://colab.research.google.com/drive/17slxQlLX9yw3CXFnD0n8IKAwh1q1Stdi"><img src="https://colab.research.google.com/img/colab_favicon.ico" width="50" height="50"></a>

**<h2>Data augmentation</h2>**

The data augmentation was done using gamma and logarithm transformations. Therefore, we used a convolutional mean filter using openCV. The code used in data augmentation is <a href="https://github.com/schmoellerIuri/FruitClassifier/blob/master/Images/DataAugmentation.py">Here!</a>

**<h2>Training and predictions</h2>**

We used deep learning to train our Convolutional Neural Network. First, we separated the training, test and validation data as 70%, 15% and 15% respectively using SciKitImage. 

Then we used a base model for our network: the ResNet Keras' implementation. That is a Residual Convolutional Neural Network, a CNN where each convolutional layer reuses data from previous layers, learning residual functions. In our model we used the 50 Layers model of the network. Since our database is too small we decided to use the imagenet pre trained weights. We've also added three more layers to the model, adapting the output of the network to only 10 neurons that represents each one of our fruit classes.

We can see the ResNet50 architecture bellow:

<img src="https://miro.medium.com/v2/resize:fit:1400/1*rPktw9-nz-dy9CFcddMBdQ.jpeg">
