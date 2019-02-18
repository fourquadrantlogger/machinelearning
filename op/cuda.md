+ GPU版本信息
```
lspci | grep -i nvidia
```
+ 会输出CUDA的版本信息
```
nvcc -V
nvidia-smi 
# 如果出现了你的GPU列表
```
+ 测试cuda
```
cd /usr/local/cuda-8.0/samples/1_Utilities/deviceQuery
sudo make
./deviceQuery

```
如果显示的是一些关于GPU的信息，则说明安装成功了

## 多版本切换

```
sudo rm -rf cuda
sudo ln -s /usr/local/cuda-9.0 /usr/local/cuda
或
sudo ln -s /usr/local/cuda-10.0 /usr/local/cuda
```