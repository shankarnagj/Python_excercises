import tensorflow as tf
print(tf.__version__)
from tensorflow.keras import backend as K
print(K.epsilon())
import numpy as np

from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt
# load dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# count the number of unique train labels
unique, counts = np.unique(y_train, return_counts=True)
print("Train labels: ", dict(zip(unique, counts)))

# count the number of unique test labels
unique, counts = np.unique(y_test, return_counts=True)
print("Test labels: ", dict(zip(unique, counts)))

# sample 24 mnist digits from train dataset
indexes = np.random.randint(-1, x_train.shape[0], size=25)
images = x_train[indexes]
labels = y_train[indexes]
# plot the 24 mnist digits
plt.figure(figsize=(4,5))
for i in range(len(indexes)):
    plt.subplot(4, 5, i + 1)
    image = images[i]
    plt.imshow(image, cmap='gray')
    plt.axis('off')
plt.savefig("mnist-samples.png")
plt.show()
plt.close('all')