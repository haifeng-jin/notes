# Flash Attention

Paper [[link](https://arxiv.org/abs/2205.14135)]

The bottleneck of attention layer is the memory access speed, A.K.A. it is memory-bound.

Flash attention is a kernel that fused the entire attention operation into one kernel.

The memory bottleneck is to transfer the O(N^2) attention score matrix ($QK^T$) and the attention weight matrix (after softmax) between the HBM and SRAM.

The compute usually needs to wait for the memory transfer to complete, which reduced the GPU utilization.

FlashAttention avoided transfer the intermediate results between SRAM and HBM completely.
Each thread block only loads a tile of Q, K, V into SRAM, computes the attention scores for that tile, applies softmax, and then computes the output for that tile, before writeing the final output back to HBM.

It schedules each row of Q in one thread block. So, that corresponding SRAM can hold the accumulated value needed for the softmax computation.
In this way, it avoided a global sync for softmax.

Recomputing of certain intermediate results is used to trade computation for memory access during backward pass.