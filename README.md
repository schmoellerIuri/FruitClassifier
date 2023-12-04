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

**<h1>Training</h1>**

We used deep learning to train our Convolutional Neural Network. First, we separated the training, test and validation data as 70%, 15% and 15% respectively using SciKitLearn. 

Then we used a base model for our network: the ResNet Keras' implementation. That is a Residual Convolutional Neural Network, a CNN where each convolutional layer reuses data from previous layers, learning residual functions. In our model we used the 50 Layers model of the network. Since our database is too small we decided to use the imagenet pre trained weights. We've also added three more layers to the model, adapting the output of the network to only 10 neurons that represents each one of our fruit classes. To improve the training performance we used the TPUs provided by google colab during the process.

We can see the ResNet50 architecture bellow:

<img src="https://miro.medium.com/v2/resize:fit:1400/1*rPktw9-nz-dy9CFcddMBdQ.jpeg">

**<h1>Predictions</h1>**
We had great results using our model, to check the performance with validation data we used the classification report function provided by ScikitLearn.metrics.
We've got the following output:

4/4 [==============================] - 1s 32ms/step
Classification report for classifier CNN:
              precision    recall  f1-score   support

           0       1.00      1.00      1.00         9
           1       1.00      0.89      0.94         9
           2       0.94      1.00      0.97        16
           3       1.00      1.00      1.00        18
           4       1.00      1.00      1.00         6
           5       1.00      1.00      1.00        10
           6       1.00      1.00      1.00         9
           7       1.00      1.00      1.00         7
           8       1.00      1.00      1.00         8
           9       1.00      1.00      1.00         9

    accuracy                           0.99       101
   macro avg       0.99      0.99      0.99       101
weighted avg       0.99      0.99      0.99       101

