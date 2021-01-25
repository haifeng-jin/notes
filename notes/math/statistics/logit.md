# Logit Function

It is a function mapping the probability of an event to happen from the rang of [0, 1] to ${\displaystyle (-\infty ,+\infty )}$.

If the probability for an event to happen is $p$, the following is the logit function.
We sometime also refer to the value of the function as logit.

$$
{\displaystyle \operatorname {logit} (p)=\log \left({\frac {p}{1-p}}\right)}
$$

It is also the inverse function of sigmoid function.
In neural networks, for binary classification problem,
the output of a neural network is considered as logits
since their value ranges are ${\displaystyle (-\infty ,+\infty )}$.
They need to pass a sigmoid layer to become the probabilities.

For multi-class classification, the similar pair of inverse functions are
softmax and multinominal logit.
