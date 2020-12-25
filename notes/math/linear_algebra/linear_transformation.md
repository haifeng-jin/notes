# Linear Transformation

Vectors should be stored in columns.

A $m\times n$ ($m$ rows and $n$ columns) matrix $\mathbf{A}$ can be seen as a linear transformation of a $n$ dimensional space into $m$ dimensional space.
It is a mapping from $n$-dimensional space to $m$-dimensional space.

The $n$ column vectors in $\mathbf{A}$ are the coordinates of the vectors in the new $m$-dimensional space.
During the transformation of the space, the the basis of the $n$ dimensional space are mapped to these vectors in the new space.

So a column vector $\mathbf{x}$ which original was a point in the $n$-dimensional space,
would get its new coordinate in the $m$-dimensional space as $\mathbf{Ax}$.
In this multiplication, sum of element-wise multiplication are calculated between $\mathbf{x}$ and each row of $\mathbf{A}$.

Each of the $n$ columns use the $m$ unit vectors (basis in the new space) to represent its coordinate.
The $i$th row of $\mathbf{A}$,
which has $n$ elements,
represents how long these $n$ basis vectors are on the $i$th dimension of the $m$ dimensions.
So this multiplication between $\mathbf{x}$ and the $i$th row would calculate the length of $\mathbf{x}$ in the $i$th dimension.

Matrix multiplication can be understand as a sequence of linear transformations of spaces.
For example, $\mathbf{ABC}$ can be seen as: first transform by $\mathbf{C}$, then by $\mathbf{B}$, finally by $\mathbf{A}$.
They read from right to left like $f(g(x))$, which first calculate $g$.
