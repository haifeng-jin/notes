# Linear Regression

## Definition

The equation of linear regression is as follows.

$$
\mathbf {y} =\mathbf{X}{\boldsymbol {\beta }}+{\boldsymbol {\varepsilon }}
$$

where $\mathbf {y}$ is the prediction target vector,
$\mathbf{X}$ is the feature matrix,
where each row is a feature vector,
the first column of which only contains 1s,
$\boldsymbol {\beta}$ is the parameter to learn,
$\boldsymbol {\varepsilon }$ is the error term.

## Solution

The solution is also called estimation of the parameters.
The most straight-forward solution is the ordinary least squares (OLS) estimation.
We will also introduce maximum likelihood estimation (MLE) and maximum a posteriori (MAP),
which are the most widely used estimation methods in machine learning.

### Ordinary Least Squares

This method directly minimize the square of the error term $\boldsymbol {\varepsilon }$.
We see the error term as an vector, we want to minimize the length of the vector,
which is the same as minimizing the square of the length of the vector.
The notation for the length of a vector is ${\bigl \|}\boldsymbol {\varepsilon }{\bigr \|}$.
Its square is ${\bigl \|}\boldsymbol {\varepsilon }{\bigr \|}^2$
The loss function is:

$$
\min_{\boldsymbol \beta} {\bigl \|}\boldsymbol {\varepsilon }{\bigr \|}^2 \\
$$


Here we use capital $\mathbf{Y}$ since it can also be a matrix for multivariate regression.
We need to calculate the partial derivative of the loss function with respect to $\boldsymbol {\beta}$,
which is also called the [gradient](../calculus/gradient.md) since $\boldsymbol {\beta}$ is a vector.
Then we set the gradient to zero to minimize the loss since the loss is convex.

$$
\min_{\boldsymbol \beta} {\bigl \|}\boldsymbol {\varepsilon }{\bigr \|}^2 
=\min_{\boldsymbol \beta} {\bigl \|}\mathbf{Y} - \mathbf{X}{\boldsymbol {\beta }}{\bigr \|}^2
=\min_{\boldsymbol \beta} (\mathbf Y - \mathbf{X}{\boldsymbol {\beta }})^\top(\mathbf Y - \mathbf{X}{\boldsymbol {\beta }})\\
=\min_{\boldsymbol \beta} \mathbf Y^\top \mathbf Y - \mathbf Y^\top \mathbf{X}{\boldsymbol {\beta }}- (\mathbf{X}{\boldsymbol {\beta }})^\top \mathbf Y  + (\mathbf{X}{\boldsymbol {\beta }})^\top\mathbf{X}{\boldsymbol {\beta }}\\
=\min_{\boldsymbol \beta} \mathbf Y^\top \mathbf Y - \mathbf Y^\top \mathbf{X}{\boldsymbol {\beta }}- {\boldsymbol {\beta }}^\top\mathbf{X}^\top \mathbf Y  + {\boldsymbol {\beta }}^\top\mathbf{X}^\top\mathbf{X}{\boldsymbol {\beta }}
$$

Set the first order derivative with respect to $\boldsymbol \beta$ to zero. Need [matrix diferentiation rules](../calculus/matrix_differentiation.md#rules)

$$
\frac{\partial}{\partial \boldsymbol \beta}(
\mathbf Y^\top \mathbf Y - \mathbf Y^\top \mathbf{X}{\boldsymbol {\beta }}- {\boldsymbol {\beta }}^\top\mathbf{X}^\top \mathbf Y  + {\boldsymbol {\beta }}^\top\mathbf{X}^\top\mathbf{X}{\boldsymbol {\beta }}) = -2\mathbf X ^\top \mathbf Y + 2X^\top\mathbf X \boldsymbol \beta = 0\\
\boldsymbol \beta = (\mathbf X^\top\mathbf X)^{-1}\mathbf X ^\top\mathbf Y
$$

### Maximum Likelihood Estimation

### Maximum a Posteriori
