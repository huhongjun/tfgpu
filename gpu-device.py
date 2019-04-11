#!/usr/local/bin/python
# -*- coding: utf-8 -*-

def is_gpu_available(cuda_only=True):
  """
  code from https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/platform/test.py
  Returns whether TensorFlow can access a GPU.
  Args:
    cuda_only: limit the search to CUDA gpus.
  Returns:
    True iff a gpu device of the requested kind is available.
  """
  from tensorflow.python.client import device_lib as _device_lib

  if cuda_only:
    return any((x.device_type == 'GPU')
               for x in _device_lib.list_local_devices())
  else:
    return any((x.device_type == 'GPU' or x.device_type == 'SYCL')
               for x in _device_lib.list_local_devices())

def get_available_gpus():
    """
    code from http://stackoverflow.com/questions/38559755/how-to-get-current-available-gpus-in-tensorflow
    """
    from tensorflow.python.client import device_lib as _device_lib
    local_device_protos = _device_lib.list_local_devices()
    return [x.name for x in local_device_protos if x.device_type == 'GPU']

def test_is_gpu_available():
    #for i in range(4):
    if(is_gpu_available()):
        str = 'with' if is_gpu_available(True) else 'without'
        print("GPU is available, %s CUDA installed" % str)

def test_get_available_gpus():
    devices = get_available_gpus();
    i = 0 
    for d in devices:
        i = i + 1
        print("你的第 %2d 个GPU是： %5s" % (i,d))
        
test_is_gpu_available()

test_get_available_gpus()