# Maximum a Posteriori Estimation

You can think it as an advanced version of [maximum likelihood estimation](mle.md) (MLE).
In MLE, we assume the parameter $\boldsymbol\theta$ is a constant value.
However, in maximum a posteriori (MAP) estimation, we assume the parameter $\boldsymbol\theta$ is also a random variable.

Instead of maximizing $p(\mathbf X\mid \boldsymbol\theta )$, we would like to maximize the posterior $p(\boldsymbol\theta\mid \mathbf X )$.
The meaning of the posterior here is that given the samples $\mathbf X$, the probability for the parameters to be $\boldsymbol\theta$.

$$
{\hat {\boldsymbol\theta }}={\underset {\boldsymbol\theta \in \Theta }{\operatorname {arg\;max} }}\ p(\boldsymbol\theta\mid \mathbf X ) =
={\underset {\boldsymbol\theta \in \Theta }{\operatorname {arg\,max} }}\ {\frac {p(x\mid \theta )\,p(\theta )}{ \int _ {\Theta }p(x\mid \vartheta )\,p(\vartheta )\,d\vartheta }}={\underset {\boldsymbol\theta \in \Theta}{\operatorname {arg\,max} }}\ p(x\mid \theta )\,p(\theta )
$$

As you see, we explicitly modeled the prior for $\boldsymbol\theta$ as $p(\boldsymbol\theta)$.
