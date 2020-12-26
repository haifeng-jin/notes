# Eigenvector and Eigenvalues

Intuitively, we can understand the eigenvectors of a matrix as follows.
See the matrix as a linear transformation of the space.
There are some some vectors remained in there original direction before and after the transformation.
They are only scaled during the transformation.
These vectors before the transformation are the eigenvectors.
The scalar to scale them during the transformation are the eigenvalues.

We can build an equation by the unchanged vectors.
$\mathbf{v}$ is the unchanged vector after the linear transformation $\mathbf{A}$,
but only scaled by $\lambda$.

$$
\mathbf{Av} = \lambda\mathbf{v}\\
\mathbf{Av} - \lambda\mathbf{v} = 0\\
(\mathbf{A} - \lambda \mathbf{I}) \mathbf{v} = 0\\
det(\mathbf{A} - \lambda \mathbf{I}) = 0
$$

$(\mathbf{A} - \lambda \mathbf{I}) \mathbf{v} = 0$ means $\mathbf{v}$ is linearly transformed to 0.
The only possible situation for this is the space is squeezed to lower dimension by the linear transformation,
during which $\mathbf{v}$ is squeezed to 0.
(The linear transformation is defined by matrix $(\mathbf{A} - \lambda \mathbf{I})$.
This means the determinant of the transformation matrix is 0.
So, we can solve it to get $\lambda$.
Put $\lambda$ value into the $(\mathbf{A} - \lambda \mathbf{I}) \mathbf{v} = 0$,
we get $\mathbf{v}$.

Notably, diagonal matrix's columns are eigenvectors and the only values are the eigenvalues.

Consider the following problem,
we want to compute a matrix $\mathbf{B}$ which is a transformation,
which is the same as apply another transformation defined by matrix $\mathbf{A}$ a hundred times. So $\mathbf{B}=\mathbf{A}^{100}$.
To compute this efficiently,
we want to somehow converted to a multiplication problem of a diagonal matrix instead of the original $\mathbf{A}$.
If we represent the transformation defined by $\mathbf{A}$ using the eigenvectors of $\mathbf{A}$ as the basis,
it would be much easier since in this transformation,
the basis has been scaled only,
instead of combined together.
So the transformation matrix should be a diagonal matrix if represented by the coordination system,
which use the eigenvectors as basis,
namely eigenbasis.
So to calculate the same transformation as $\mathbf{A}$ in the new coordination system,
we calculate $\mathbf{D}=\mathbf{C}^{-1}\mathbf{AC}$,
where $\mathbf{C}$ is the translate matrix,
that $\mathbf{Cx}$ translate $\mathbf{x}$,
which is in the new eigenvector coordination system back to the original coordination system.
The column of $\mathbf{C}$ are the eigenvectors of $\mathbf{A}$.
So $\mathbf{D}$ is the transformation $\mathbf{A}$ defined in the new coordination system by the eigenvectors.
$\mathbf{D}$ is a diagonal matrix since it is the $\mathbf{A}$ transformation in the eigenvector space which should only be the scale of the axis.
We calculate $\mathbf{E}=\mathbf{D}^{100}$.
Finally, $\mathbf{B}=\mathbf{CEC}^{-1}$.
Use $\mathbf{C}$ to translate the coordinate system back to the original one.

