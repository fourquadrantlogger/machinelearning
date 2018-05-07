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

5.安装tensorflow，我这里安装的是cpu版本的：

(tensorflow) [lipeng@lipeng-pc]$ pip install --upgrade tensorflow

## 步骤
+ 安装anaconda ：python的科学发行版，内置数百个python的库
https://www.continuum.io/downloads#linux

```
bash Anaconda.sh
```
