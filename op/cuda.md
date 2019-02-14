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
