import numpy as np

#In this first part, we just prepare our data (mnist) 
#for training and testing

import keras
from keras.datasets import mnist


(X_train, y_train), (X_test, y_test) = mnist.load_data()
num_pixels = X_train.shape[1] * X_train.shape[2]  # 28 X 28
X_train = X_train.reshape(X_train.shape[0], num_pixels).T   # reshape c'est pour aplatir la matrice 1 X 784 
X_test = X_test.reshape(X_test.shape[0], num_pixels).T   
y_train = y_train.reshape(y_train.shape[0], 1)
y_test = y_test.reshape(y_test.shape[0], 1)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
y_train = y_train.astype('float32')
y_test = y_test.astype('float32')
X_train  = X_train / 255     #normalizer  pour avoir des donnees entre -1 et 1 .
X_test  = X_test / 255


#We want to have a binary classification: digit 5 is classified 1 and 
#all the other digits are classified 0

y_new = np.zeros(y_train.shape)
y_new[np.where(y_train==5.0)[0]] = 1
y_train = y_new

y_new = np.zeros(y_test.shape)
y_new[np.where(y_test==5.0)[0]] = 1
y_test = y_new


y_train = y_train.T
y_test = y_test.T


m = X_train.shape[1] #number of examples

#Now, we shuffle the training set
np.random.seed(138)
shuffle_index = np.random.permutation(m)
X_train, y_train = X_train[:,shuffle_index], y_train[:,shuffle_index]


#Display one image and corresponding label 
import matplotlib
import matplotlib.pyplot as plt
i = 3
print('y[{}]={}'.format(i, y_train[:,i]))
plt.imshow(X_train[:,i].reshape(28,28), cmap = matplotlib.cm.binary)
plt.axis("off")
plt.show()


#Let start our work: creating a neural network
#First, we just use a single neuron. 


#####TO COMPLETE

def signoid(z):
  return 1./(1.+np.exp(-z))

def cross_entropy(y,p):
  return - (y* np.log(p)+ (1-y)*ln(1-p))/len(y)

def back_propagation(y,p,x):
  return (p-y)*x




x= np.arange(-12.0,12.0,1.0,dtype=np.float32)
y= signoid(x)

plt.plot(x,y)
plt.show()



