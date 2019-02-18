# -*- coding: utf-8 -*-

import sys
import tensorflow as tf
import download
reload(sys)
sys.setdefaultencoding('utf8')

# 权重初始化
# 要创建该模型，我们需要创建很多权重置和偏置量。通常，权重在初始化时应该加入少量的噪声来打破对称性以及避免0梯度。由于我们使用 ReLU神经元，因此较好的做法是用一个较小的正数来初始化偏置量，以避免神经元节点输出恒为0（dead neurons）。为了不在构建模型时反复执行初始化操作，我们定义两个函数用于初始化。
def weight_variable(shape):
  initial = tf.truncated_normal(shape, stddev=0.1)
  return tf.Variable(initial)


def bias_variable(shape):
  initial = tf.constant(0.1, shape=shape)
  return tf.Variable(initial)

# 卷积与池化
# TensorFlow还为卷积和池化操作提供了很大的灵活性。我们如何处理图片边界？我们的步幅是多少？在本例中，我们总是选择vanilla版本。我们的卷积使用1步长，零填充，使输出与输入的大小相同。我们的池化用简单传统的2x2大小的模板做最大池化，为了使代码更简介，我们还将这些操作抽象为函数。

def conv2d(x, W):
  return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')


def max_pool_2x2(x):
  return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],
                        strides=[1, 2, 2, 1], padding='SAME')


x = tf.placeholder(tf.float32, [None, 784])
y_ = tf.placeholder(tf.float32, [None, 10])

W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

y = tf.nn.softmax(tf.matmul(x, W) + b)

W_conv1 = weight_variable([5, 5, 1, 32])
b_conv1 = bias_variable([32])

x_image = x_image = tf.reshape(x, [-1,28,28,1])

h_conv1 = tf.nn.relu( conv2d(x_image, W_conv1) + b_conv1)
h_pool1 =  max_pool_2x2(h_conv1)

# 第二卷积层
# 为了构建一个深层次的网络，我们堆叠几层这种类型的模块。第二层将为每个5x5patch提取64特征。

W_conv2 =  weight_variable([5, 5, 32, 64])
b_conv2 =  bias_variable([64])

h_conv2 = tf.nn.relu( conv2d(h_pool1, W_conv2) + b_conv2)
h_pool2 = max_pool_2x2(h_conv2)
#
# 密集连接层
# 现在图像尺寸已经缩小到7x7，我们添加了一个具有1024个神经元的全连接层，以便对整个图像进行处理。我们从池化层将张量reshape成一些向量，然后乘以权重矩阵，添加偏置量并应用于ReLU。

W_fc1 = weight_variable([7 * 7 * 64, 1024])
b_fc1 = bias_variable([1024])

h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

# Dropout
# 为了避免过拟合，我们在输出层之前加入dropout 。我们创建一个占位符表示在神经元dropuot时保持不变的概率。这样可以让我们在训练过程中应用dropout，并在测试过程中将其关闭。TensorFlow的tf.nn.dropoutop除了可以屏蔽神经元的输出外，还可以自动处理神经元输出scale，所以用dropout的时候可以不用考虑任何额外scale。1

keep_prob = tf.placeholder(tf.float32)
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

# 输出层
# 最后，我们添加一层，就像上面提到的softmax回归层一样。

W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])

y_conv = tf.matmul(h_fc1_drop, W_fc2) + b_fc2


def train():
  sess = tf.InteractiveSession()
  writer = tf.summary.FileWriter("log", sess.graph)

  cross_entropy = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y_conv))
  train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
  correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_, 1))
  accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
  sess.run(tf.global_variables_initializer())
  for i in range(20000):
    batch = download.mnist.train.next_batch(50)
    if i % 100 == 0:
      train_accuracy = accuracy.eval(feed_dict={
        x: batch[0], y_: batch[1], keep_prob: 1.0})
      print("step %d, training accuracy %g" % (i, train_accuracy))
    train_step.run(feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.5})

  return sess


