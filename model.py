from __future__ import absolute_import,division, print_function, unicode_literals
import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
from tf_parser import read_protein

data = keras.datasets.fashion_mnist

(train_samples, train_labels), (test_samples, test_label) = data.
