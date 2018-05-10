# -* - coding: UTF-8 -* -

import tensorflow as tf
import os

url="https://raw.githubusercontent.com/apachecn/MachineLearning/master/input/2.KNN/datingTestSet2.txt"

train_dataset_fp = tf.keras.utils.get_file(fname=os.path.basename(url),
                                           origin=url)

print("Local copy of the dataset file: {}".format(train_dataset_fp))