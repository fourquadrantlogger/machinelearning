## Install prerequisites (rhel)
yum install numpy python-devel python-wheel python-mock

## Install Bazel
wget https://github.com/bazelbuild/bazel/releases/download/0.4.5/bazel-0.4.5-dist.zip
unzip bazel-0.4.5-dist.zip -d bazel

## Modify bazel WORKSPACE
cd bazel
Modify WORKSPACE (Optinal step to avoid warnings)
    from workspace(name = "io_bazel")
    to   workspace(name = "bazel_tools")

## Build bazel
./compile.sh

## Install cuda 8.0
https://developer.nvidia.com/cuda-downloads

## Install cuDNN
sudo tar -xvf cudnn-8.0-linux-ppc64le-v5.1.tgz -C /usr/local/
https://developer.nvidia.com/compute/machine-learning/cudnn/secure/v6/prod/8.0_20170427/cudnn-8.0-linux-ppc64le-v6.0-tgz

## Build TensorFlow
git clone https://github.com/tensorflow/tensorflow
cd tensorflow

export PYTHON_BIN_PATH=/usr/bin/python
export GCC_HOST_COMPILER_PATH=/usr/bin/gcc
export TF_NEED_JEMALLOC=0
export TF_NEED_GCP=0
export TF_NEED_HDFS=0
export TF_ENABLE_XLA=0
export TF_NEED_CUDA=1
export TF_NEED_OPENCL=0
export CUDA_TOOLKIT_PATH=/usr/local/cuda-8.0
export TF_CUDA_VERSION=8.0
export TF_CUDNN_VERSION=6
export CC_OPT_FLAGS="-O3"
export PATH=$PATH:/home/xxx/bazel/output/ (Add your bazel bin path)

./configure

----------------------------
Build with GPU
----------------------------
bazel build --config opt --config=cuda //tensorflow/tools/pip_package:build_pip_package
bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/tensorflow_pkg
pip install --user /tmp/tensorflow_pkg/tensorflow-xxx.whl

export LD_LIBRARY_PATH=/usr/local/cuda/targets/ppc64le-linux/lib/:$LIBRARY_PATH
export PYTHON_LIBRARY_PATH=/home/xlhu/.local/lib/python2.7/site-packages/

# Run an example to check
export PYTHON_LIBRARY_PATH=$PYTHON_LIBRARY_PATH:/home/xlhu/.local/lib/python3.5/site-packages/ (Depends on your own path)
git clone https://github.com/tensorflow/models.git
cd models/tutorials/image/mnist
python convolutional.py

----------------------------
Build with CPU Only
----------------------------
bazel build //tensorflow/tools/pip_package:build_pip_package
bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/tensorflow_pkg
pip install --user /tmp/tensorflow_pkg/tensorflow-xxx.whl
