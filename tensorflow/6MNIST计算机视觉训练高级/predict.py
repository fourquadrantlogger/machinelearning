# -*- coding: utf-8 -*-

import sys
import modelandtrain
import download
reload(sys)
sys.setdefaultencoding('utf8')


import tensorflow as tf
sess=modelandtrain.train()

print("test accuracy %g"%modelandtrain.accuracy.eval(feed_dict={
    modelandtrain.x: download.mnist.test.images, modelandtrain.y_: download.mnist.test.labels, modelandtrain.keep_prob: 1.0}))