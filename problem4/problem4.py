import tensorflow as tf

# Load the MNIST dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Reshape the input images into a single dimension
x_train = x_train.reshape(-1, 784)
x_test = x_test.reshape(-1, 784)
