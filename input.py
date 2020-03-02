import os
import numpy as np
import tensorflow as tf

from proteinnet.tf_parser import read_protein
from SecStrPred import train

base_dir = '../'

train_location = base_dir + 'data/casp' + casp_version + '/training/' + training_size + '/'
eval_location = base_dir + 'data/casp' + casp_version + '/validation/'
test_location = base_dir + 'data/casp' + casp_version + '/testing/'

def read_data(model_train_size):
    casp_version = input("Enter the casp version you want to use (7 - 12)")
    
    train_path = train_location + casp_version
    train_files = os.listdir(train_path)
    print(train_files)
    file_queue = tf.train.string_input_producer(
            files,
    inputs = read_protein(train_files, )
    return inputs



