# Bayes Theorem


## Equation

$$
P(A\mid B)={\frac {P(B\mid A)P(A)}{P(B)}}
$$


## Likelihood

In the equation above, $P(B\mid A)$ is usually called the likelihood.
It represents the likelihood for $B$ to be true given $A$ is true.
$A$ can be a probability distribution that fits with the training data.

## Prior

$P(A)$ is usually called the prior, which is the probability for $A$ to be true.
For example, in a classification task, $P(A)$ can be the prior probability of a sample, without any further information,
belongs to a certain class.

## Evidence

$P(B)$ is usually called the evidence.
It is some piece of information that alters our judgement for how likely that $A$ would be true.

## Posterior

$P(A\mid B)$ is usually called the posterior probability.
With evidence $B$ being true, it is the probability for $A$ to be true.
For example, given a sample $B$, how likely it is from the distribution of $A$.
