# GPU
#tech/snippet
Use env var to limit the GPU.

Bash:
CUDA_VISIBLE_DEVICES=1 python myscript.py

Python:
import os
os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID" # see issue #152
os.environ["CUDA_VISIBLE_DEVICES"]="0"

[https://stackoverflow.com/questions/37893755/tensorflow-set-cuda-visible-devices-within-jupyter](https://stackoverflow.com/questions/37893755/tensorflow-set-cuda-visible-devices-within-jupyter)