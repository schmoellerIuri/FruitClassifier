# Fruit Classifier using Convolutional Residual Neural Networks

## 1 - Classes

Here are the classes and their corresponding IDs:

0. banana 🍌
1. clementine 🍊
2. lemon 🍋
3. tomato 🍅
4. strawberry 🍓
5. apple 🍎
6. pineapple 🍍
7. pear 🍐
8. papaya 🥭
9. coconut 🥥

## 2 - Running Environment and Implementation

Our image database resides in this repository, containing approximately 650 images. We've performed data augmentation to enhance the training data.

### Running Environment

To run this project, access it via Google Colab using the provided link:

<a href="https://colab.research.google.com/drive/17slxQlLX9yw3CXFnD0n8IKAwh1q1Stdi"><img src="https://colab.research.google.com/img/colab_favicon.ico" width="50" height="50"></a>

### Data Augmentation

We conducted data augmentation using gamma and logarithm transformations. This involved employing a convolutional mean filter via openCV. Find the code used for data augmentation [here](https://github.com/schmoellerIuri/FruitClassifier/blob/master/Images/DataAugmentation.py).

### Training and Predictions

#### Training

For training, we adopted deep learning techniques utilizing a Convolutional Neural Network (CNN). The data was divided into training, test, and validation sets with proportions of 70%, 15%, and 15%, respectively, using SciKitLearn.

We utilized the ResNet model in Keras, specifically the ResNet50 architecture. Due to the small database size, we opted for the pre-trained weights from ImageNet. To adapt the network output to our ten fruit classes, we added three more layers. Google Colab's TPUs were used to enhance training performance.

The architecture of ResNet50 is displayed below:

![ResNet50 Architecture](https://miro.medium.com/v2/resize:fit:1400/1*rPktw9-nz-dy9CFcddMBdQ.jpeg)

#### Predictions

Our model yielded impressive results. We evaluated its performance using the validation data through the classification report function provided by ScikitLearn.metrics. The output is as follows:

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
    macro avg      0.99      0.99      0.99       101
    weighted avg   0.99      0.99      0.99       101

