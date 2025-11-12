# Flash Attention

Paper [[link](https://arxiv.org/abs/2205.14135)]

The bottleneck of attention layer is the memory access speed, A.K.A. it is memory-bound.

Flash attention is a kernel that fused the entire attention operation into one kernel.

The memory bottleneck is to transfer the O(N^2) attention weight matrix ($QK^T$) and the 

Flash Attention is fast because it directly addresses the memory bottleneck of the standard attention mechanism in Transformers, particularly when running on GPUs.

The key to its speed is a technique called I/O-Awareness, which minimizes the amount of data transferred between the GPU's fast but small SRAM (on-chip memory/cache) and the slow but large HBM (High Bandwidth Memory/global GPU memory).