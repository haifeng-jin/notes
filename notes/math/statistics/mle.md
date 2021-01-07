# Maximum Likelihood Estimation

Suppose we have a probability distribution with parameter $\boldsymbol\theta$.
We also have some samples drawn from the distribution $\mathbf X$.
We would like to estimate $\boldsymbol\theta$ based on $\mathbf X$ to maximize the following probability.

$$
{\hat {\boldsymbol\theta }}={\underset {\boldsymbol\theta \in \Theta }{\operatorname {arg\;max} }}\ p(\mathbf X\mid \boldsymbol\theta )
$$

Intuitively, we would like to find the parameters, which would most likely to generate these samples.
