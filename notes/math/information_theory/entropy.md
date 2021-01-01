# Entropy

## Overview
Entropy is a measure of uncertainty, or the amount of information to reduce the uncertainty.
The formal definition is as follows.

Given a discrete random variable $X$,
with possible outcomes $x_{1},...,x_{n}$,
which occur with probability $\mathrm {P} (x_{1}),...,\mathrm {P} (x_{n})$,
the entropy of $X$ is formally defined as:
$$
\mathrm {H} (X)=-\sum_{i=1}^{n}{\mathrm {P} (x_i)\log \mathrm {P} (x_i)}
$$

You can think entropy as something related to the encoding of all the outcomes.
We use 0 and 1 to encode them.
The minimum average length of the all the encodings is the entropy.

The more outcomes a random variable has, the larger the entropy is.
The more unbalance the probability distribution is, the smaller the entropy is.

## The Logarithm

You can think the $-\log \mathrm {P} (x_i)$ as a measurement for the encoding length of that specific result $X=x_i$.
For example, if every outcome has a same probability of $\frac{1}{8}$, the encoding length with binary bits should be $-\log_2\frac{1}{8} = 3$.

## An Expectation Perspective

Entropy is an expectation of the encoding length of different outcomes. 

$$
\mathrm {H} (X)=\operatorname {E} [-\log(\mathrm {P} (X))]
$$
