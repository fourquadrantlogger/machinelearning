import tensorflow as tf


a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b  # + provides a shortcut for tf.add(a, b)
sess=tf.Session()
writer = tf.summary.FileWriter("log",sess.graph)

print(sess.run(adder_node, {a: 3, b:4.5}))
print(sess.run(adder_node, {a: [1,3], b: [2, 4]}))


# https://www.tensorflow.org/api_docs/python/tf/summary/FileWriter

# tensorboard --logdir=/CODE/github.com/timeloveboy/machinelearning/tensorflow/2tensorboard/log