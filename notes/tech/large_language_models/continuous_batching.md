# Continuous Batching

This is a technique to reduce request waiting time and increase the GPU utilization during serving.

[Blog link](https://www.anyscale.com/blog/continuous-batching-llm-inference)

[Paper link](https://www.usenix.org/conference/osdi22/presentation/yu)

## The problem

When think of batching during inference, the requests have to arrive almost at the same time and they need to have exact the same number of tokens.
Only in this way, we can batch them together to generate the next token for each request.
This results in longer waiting time for the late-arriving requests.
It also prevent from the shorter answers to return since it has to finish the longest sequence in the batch before return all of the results together.

## Handling sequences of different lengths in the same batch

Continuous batching came up with a technique to handle sequences of different lengths.
They now can be batched together.
What it did was just categorize the ops into two groups.
One is different-length-compatible, for example, matmul generating the next K, Q, V vector, layer-norm, gelu.
The other group is not compatible different-length-compatible, for example, attention layers, that uses the $\mathbf{Q}\mathbf{K}^{T}$.
Then, it do the ops in the first group in a batched manner, but split them by request when execuing the ops in the second group.

In this way, sequences of different lengths can be batched together for serving.

## Iteration-level scheduling

Then, it does some scheduling at every interation.
It iteration is generation one more token for each sequence in the batch.
It may remove sequence from the batch if it reached the end or add a new squence to it when a new request arrives.

So, now, the shorter answer no longer needs to wait for the longer answer to finish, and the newly arrived requests also do not need to wait to join a batch.
