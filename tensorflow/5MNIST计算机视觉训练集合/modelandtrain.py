# -*- coding: utf-8 -*-

import sys


import tensorflow as tf
import download
reload(sys)
sys.setdefaultencoding('utf8')

x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x, W) + b)
y_ = tf.placeholder(tf.float32, [None, 10])


def train():

  # None表示第一个维度可以是任意长度

  cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

  train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

  sess = tf.InteractiveSession()
  writer = tf.summary.FileWriter("log", sess.graph)

  tf.global_variables_initializer().run()
  for _ in range(1000):
    batch_xs, batch_ys = download.mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

  return sess