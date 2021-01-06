# Installa TensorFlow
import tensorflow as tf
from tensorflow import keras

# Librerias de ayuda
import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.pyplot import *
from pylab import *
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# print(tf)
# print(tf.__version__)

# mnist = tf.keras.datasets.mnist
# # print(type(mnist))
# (x_train, y_train), (x_test, y_test) = mnist.load_data()
# x_train, x_test = x_train / 255.0, x_test / 255.0
# print(x_train.all)
# print(len(x_test))

plt.figure()
x = np.arange(0, 5, 0.1)
y = np.sin(x)
plt.plot(x, y)
# plot(x, y)
# plt.x
# plt.imshow(x_train)
# plt.plot(1,30)
# plt.colorbar()
# plt.grid(False)
# show()
# plt.draw()
plt.show()

# c = np.array([[3.,4], [5.,6], [6.,7]])
# step = tf.reduce_mean(c, 1)                                                                                 
# with tf.Session() as sess:
#     print(sess.run(step))

