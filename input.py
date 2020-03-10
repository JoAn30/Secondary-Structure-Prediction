import os
import numpy as np
import tensorflow as tf

from proteinnet.tf_parser import read_protein
from SecStrPred import train

base_dir = '../'

train_location = base_dir + 'data/casp' + casp_version + '/training/' + training_size + '/'
eval_location = base_dir + 'data/casp' + casp_version + '/validation/'
test_location = base_dir + 'data/casp' + casp_version + '/testing/'

def read_train_data(model_train_size, casp_version): 

    train_path = train_location + casp_version
    train_files = os.path.join(train_dir, file) for file in train_files]
    print(train_files)
    file_tensor = tf.convert_to_tensor(train_files)
    file_queue = tf.train.string_input_producer(
            file_tensor,
            shuffle=True)
    train_inputs = read_protein(file_queue, max_length) #Check max length at some point.
    return train_inputs

def read_test_data(model_train_size, casp_version):





