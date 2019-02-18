# Tensorflow


## 组件
+ tensorflow serving

##
![img](img/tensorflow_programming_environment.png)

## 
 sudo docker run --runtime=nvidia -it --rm tensorflow/tensorflow:latest-gpu python -c "import tensorflow as tf;print(tf.__version__)"


docker run --runtime=nvidia -it --rm tensorflow/tensorflow:latest-gpu \
   python -c "import tensorflow as tf; tf.enable_eager_execution(); print(tf.reduce_sum(tf.random_normal([1000, 1000])))"
## 

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/lib64
export PATH=$PATH:/usr/local/cuda/bin
export CUDA_HOME=$CUDA_HOME:/usr/local/cuda
 