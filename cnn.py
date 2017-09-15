import numpy as np
np.random.seed(123)

from keras.models import Sequential  #stack of neural networks

from keras.layers import Dense, Dropout, Activation, Flatten #commonly used layers in a nerual net
from keras.layers import Convolution2D, MaxPooling2D

from keras.utils import np_utils

from keras.datasets import mnist

(X_train, y_train), (X_test, y_test) = mnist.load_data() # does it split it for you??

print X_train.shape
print X_test.shape
