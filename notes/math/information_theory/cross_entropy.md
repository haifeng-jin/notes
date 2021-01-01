# Cross Entropy

## An Information Theory Perspective

It is very similar to [entropy](entropy.md),
if we think entropy as the lowest expectation of the encoding length,
Cross entropy deals with two different sets of probability distributions.
The optimal encoding scheme for the two distributions should be different to reach the lowest expectation of the encoding length.
If we use the encoding scheme for one distribution but the random variable follows the other probability distribution, cross entropy measures the expectation of the encoding length in this case.

If one probability distribution is $p$ and the encoding is optimized for distribution $q$, 
the cross entropy can be written as the following.

$$
H(p,q)=-\operatorname {E}_ {p}[\log q]
$$

## Loss Function

Cross entropy is usually used as a loss function for classification tasks.
Minimizing the cross entropy is actually maximizing the likelihood.
We can consider the target $y$ of each training sample is a drawn from a different Bernoulli distribution.
The likelihood for a sample to occur can be expressed as

$$
f(y;p)=p^{y}(1-p)^{1-y}\quad {\text{for }}y\in \{0,1\},
$$

where $p$ is the probability for $y=1$.
The overall likelihood for all samples is as follows.

$$
\prod_{i=1}^{m} f(y^{(i)};p^{(i)})
$$

Therefore, the loss function is:

$$
\max_\theta \prod_{i=1}^{m} f(y^{(i)};p^{(i)})\\
\max_\theta \prod_{i=1}^{m} \bigg [{p^{(i)}}^{y^{(i)}}(1-{p^{(i)}})^{1-y^{(i)}}\bigg ]
$$

It is the same as maximize its averaged log form, which is also called the log-likelihood.

$$
\max_\theta \quad\frac{1}{m}\log(\prod_{i=1}^{m} \bigg [{p^{(i)}}^{y^{(i)}}(1-{p^{(i)}})^{1-y^{(i)}}\bigg ])\\
\max_\theta \frac{1}{m}\sum_{i=1}^{m}\bigg [y^{(i)}\log p^{(i)} + (1-y^{(i)})\log(1-p^{(i)})\bigg ]
$$

It is the same as minimizing the negative of the above function.

$$
\min_\theta -\frac{1}{m}\sum_{i=1}^{m}\bigg [y^{(i)}\log p^{(i)} + (1-y^{(i)})\log(1-p^{(i)})\bigg ]
$$

Now, we have the exact same form for the cross entropy for classification loss.
