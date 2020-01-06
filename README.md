# G7-7588的tensorfolw gpu测试

## 安装

计算机配置
GeForce GTX 1050 Ti	Pascal 768	Up to 4 GB GDDR5

### 安装tensorflow的GPU支持环境

    cuda toolkit 9.0
    cuDNN for cuda 9.0  - v7.4.3

## 安装tensorflow-gpu

conda create  -n tfgpu1.12.0 tensorflow-gpu=1.12.0
conda env list
conda activate tfgpu-1.12.0

## 开发

- 代理设置 
export http_proxy=127.0.0.1:1080

- sklearn机器学习用于点云分类
    随机森林
    最佳近邻

## 工作日志

- 2018.11.18 	nvidia-410,tensorflow-gpu=1.12,	python=3.5 =>run ok

CUDA_VISIBLE_DEVICES=0 python tensorflow/examples/tutorials/mnist/mnist_with_summaries.py

Linux
	CUDA_VISIBLE_DEVICES=0 python gpu.py gpu 1500

Windows
	set CUDA_VISIBLE_DEVICES=0
	python gpu.py gpu 1500
