# tensorflow编译安装

## 环境
gcc、gpu、python3.5

## 创建一个新的python环境

 virtualenv --system-site-packages tensorflow

[lipeng@lipeng-pc:~]$ virtualenv --system-site-packages tensorflow
Running virtualenv with interpreter /usr/bin/python2
New python executable in /home/linuxidc/tensorflow/bin/python2
Also creating executable in /home/linuxidc/tensorflow/bin/python
Installing setuptools, pkg_resources, pip, wheel...done.

3.激活Virtualenv环境：

[lipeng@lipeng-pc:~]$ source ~/tensorflow/bin/activate
(tensorflow) [lipeng@lipeng-pc:~]$

4.安装pip：

(tensorflow) [lipeng@lipeng-pc]$ easy_install -U pip

5.cuda
https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1804&target_type=deblocal
6.安装tensorflow

http://www.tensorfly.cn/tfdoc/get_started/os_setup.html

## 步骤
+ 安装anaconda ：python的科学发行版，内置数百个python的库
https://www.continuum.io/downloads#linux

```
bash Anaconda.sh
```
