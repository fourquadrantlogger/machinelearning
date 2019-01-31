# Tensorflow


## 组件
+ tensorflow serving

##
![img](img/tensorflow_programming_environment.png)

## 

docker run --runtime=nvidia -it --rm tensorflow/tensorflow:latest-gpu \
   python -c "import tensorflow as tf; tf.enable_eager_execution(); print(tf.reduce_sum(tf.random_normal([1000, 1000])))"
