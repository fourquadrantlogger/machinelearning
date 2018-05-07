from __future__ import absolute_import, division, print_function

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import tensorflow as tf
import tensorflow.contrib.eager as tfe
tf.enable_eager_execution()

print("TensorFlow version: {}".format(tf.VERSION))
print("Eager execution: {}".format(tf.executing_eagerly()))



train_dataset_fp = open("/home/lipeng/.keras/datasets/iris_training.csv",'r').read()

def parse_csv(line):
  example_defaults = [[0.], [0.], [0.], [0.], [0]]  # sets field types
  parsed_line = tf.decode_csv(line, example_defaults)
  # First 4 fields are features, combine into single tensor
  features = tf.reshape(parsed_line[:-1], shape=(4,))
  # Last field is the label
  label = tf.reshape(parsed_line[-1], shape=())
  return features, label

train_dataset = tf.data.TextLineDataset(train_dataset_fp)
train_dataset = train_dataset.skip(1)             # skip the first header row
train_dataset = train_dataset.map(parse_csv)      # parse each row
train_dataset = train_dataset.shuffle(buffer_size=1000)  # randomize
train_dataset = train_dataset.batch(32)

# View a single example entry from a batch
features, label = iter(train_dataset).next()
print("example features:", features[0])
print("example label:", label[0])


# example features: tf.Tensor([6.  2.7 5.1 1.6], shape=(4,), dtype=float32)
# example label: tf.Tensor(1, shape=(), dtype=int32)
