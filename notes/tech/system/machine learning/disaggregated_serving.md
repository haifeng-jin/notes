# Disaggregated Serving

[Paper link](https://arxiv.org/abs/2401.09670)

The compute pattern of prefill and decoding are very different.
During prefill, the sequence is long and a lot of KV caches to create.
During decoding, they just use the previous KV caches for one more token.
If we batch them together on the same GPU, they would slow each other as one may wait for the other to finish.
Due to the different compute pattern, their compute time varies a lot on different stages.
So a lot of time were wasted on waiting.

The key idea is just to serve prefill and decoding on different GPUs, the compute with similar pattern get batched together for more efficient computing.
