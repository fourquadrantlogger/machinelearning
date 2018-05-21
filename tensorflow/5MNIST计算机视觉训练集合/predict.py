# -*- coding: utf-8 -*-

import sys
import modelandtrain
import download
reload(sys)
sys.setdefaultencoding('utf8')


import tensorflow as tf
sess=modelandtrain.train()


correct_prediction = tf.equal(tf.argmax(modelandtrain.y,1), tf.argmax(modelandtrain.y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print(sess.run(accuracy, feed_dict={modelandtrain.x: download.mnist.test.images, modelandtrain.y_: download.mnist.test.labels}))