# Regularization

Regularization usually refers to adding information to solve overfitting in a learning process.

It can be adding a term to the loss function, which is called a regularization term.
The term is usually an [L-Norm](l_norms.md) on the parameters of the model.

## Select the Right L-Norm

L1 can achieve sparsity.
In other words, add an L1 regularization term can make it use more zeros in the parameters.

L2 can make the polynomial curve more smooth since it doesn't make that many zeros.

L-infinity are more likely to make the parameters equal to each other.
