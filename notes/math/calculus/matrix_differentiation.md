# Matrix Differentiation

## Overview
$\mathbf{y} = \mathbf{Ax}$ is a vector.
However, its derivative with respect to $\mathbf{x}$ is a matrix $\mathbf{A}$.
A vector is expanded to a matrix.
The new dimension appeared during the differentiation is the dimension of $\mathbf{x}$.
If the length of $\mathbf{x}$ is $n$, the length of $\mathbf{y}$ should also be $n$.
The derivative looks like $\frac{\partial \mathbf{y}}{\partial \mathbf{x}}$.
If we put the derivatives into the original vector shape, it looks like this.

$$
{\frac {\partial \mathbf {y} }{\partial \mathbf x}}={\begin{bmatrix}{\frac {\partial y_{1}}{\partial \mathbf x}}\\{\frac {\partial y_{2}}{\partial \mathbf x}}\\\vdots \\{\frac {\partial y_{m}}{\partial \mathbf x}}\\\end{bmatrix}}
$$

However, each of the $\mathbf x$ here is a vector, so the actual derivative is expanded with a dimension of the length of $\mathbf x$.

$$
{\frac {\partial \mathbf {y} }{\partial \mathbf {x} }}={\begin{bmatrix}{\frac {\partial y_{1}}{\partial x_{1}}}&{\frac {\partial y_{1}}{\partial x_{2}}}&\cdots &{\frac {\partial y_{1}}{\partial x_{n}}}\\{\frac {\partial y_{2}}{\partial x_{1}}}&{\frac {\partial y_{2}}{\partial x_{2}}}&\cdots &{\frac {\partial y_{2}}{\partial x_{n}}}\\\vdots &\vdots &\ddots &\vdots \\{\frac {\partial y_{m}}{\partial x_{1}}}&{\frac {\partial y_{m}}{\partial x_{2}}}&\cdots &{\frac {\partial y_{m}}{\partial x_{n}}}\\\end{bmatrix}}
$$

When we expand the dimension, we need to align that dimension well across different terms of the function.
For the following example, $\mathbf x$ and $\mathbf a$ are vectors.
So the function is a scalar before differentiation.
However, the $\mathbf x$ in one of the terms is transposed but not in the other one.
When we expand the scalar to a vector during differentiation, we should either expand according to the transposed $\mathbf x$ or the not transposed $\mathbf x$, but not both.
In this way, the two results can be added up together to $2\mathbf a$.
Otherwise, they will be a row and a column vector.

$$
\frac{\partial ({\mathbf x^\top \mathbf a + \mathbf a^\top \mathbf x})}{\partial \mathbf x} = 2\mathbf a
$$

## Rules

All the rules are expanded according to $\mathbf x$ as the last dimension not transposed.

$$
\frac{\partial ({\mathbf a^\top \mathbf x})}{\partial \mathbf x} = \mathbf a
$$

$$
\frac{\partial ({\mathbf x^\top \mathbf a})}{\partial \mathbf x} = \mathbf a
$$

For the [quadratic form](../linear_algebra/quadratic_form.md)

$$
{\frac  {\partial {\mathbf  {x}}^{\top }{\mathbf  {A}}{\mathbf  {x}}}{\partial {\mathbf  {x}}}}=2\mathbf{A}\mathbf{x}
$$
