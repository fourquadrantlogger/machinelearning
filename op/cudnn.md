下载解压CUDNN，注意对应版本

tar -xzvf cudnn-9.0-linux-x64-v7.1.tgz

复制相关文件到cuda特定目录下(我的cuda安装目录为/usr/local/cuda-9.0/)
sudo cp cuda/include/cudnn.h /usr/local/cuda-9.0/include
sudo cp cuda/lib64/libcudnn* /usr/local/cuda-9.0/lib64

修改文件权限
sudo chmod a+r /usr/local/cuda-9.0/include/cudnn.h /usr/local/cuda-9.0/lib64/libcudnn*
