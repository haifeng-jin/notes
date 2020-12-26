# Change of Basis

A matrix can be seen as a linear transformation of a space.
$\mathbf{Ax}$ means transform the vector $\mathbf{x}$,
which is in the original space,
into the new space,
but still using the original basis for coordination.
The original basis means the perpendicular unit vectors.
In this case, $\mathbf{x}$ should be a vector represented in the original basis coordination system.

Let's consider another problem, $\mathbf{x}$ is (3, 2).
However, it is not in the original coordinate system but a new coordinate system,
which uses $\mathbf{A}$'s column vectors as basis.
3 and 2 are the scalars for the column vectors in $\mathbf{A}$.
How can we translate the vector $\mathbf{x}$ back to the original coordination system?
I mean what is the coordinate of the $\mathbf{x}$ represented by the original coordination system.
It is the same as the above example, it should be $\mathbf{Ax}$.

So a matrix can have different meaning's in different situations.
It can either mean a transformation of the space,
or a translation from one coordination system to another.
It depends on the meaning of the vector multiplied on the right.
If x is using the new space basis, then means translation.
If in the old one, it means transformation.

Another problem is how to translate a vector $\mathbf{x}$ represented in the original system into the new coordination system.
Just use $\mathbf{A}^{-1}\mathbf{x}$,
where $\mathbf{A}$ consists of the basis vectors of the new coordination system as columns.
The reason is as follows.
Suppose \mathbf{x}$ is using the new coordinate system specified by $\mathbf{A}$.
$\mathbf{A}^{-1}\mathbf{Ax}$ is still $\mathbf{x}$.
$\mathbf{v} = \mathbf{Ax}$ is the translated $\mathbf{x}$ in the original coordinate system.
So $\mathbf{v}$ is $\mathbf{x}$ described by the original coordination system.
$\mathbf{A}^{-1}\mathbf{Ax}=\mathbf{x} \Rightarrow \mathbf{A}^{-1}\mathbf{v}=\mathbf{x}$,
so $\mathbf{A}^{-1}$ can translate $\mathbf{v}$ to $\mathbf{x}$.
So $\mathbf{A}^{-1}$ is the opposite translation of $\mathbf{A}$.

If we want to do an operation (rotate a vector for 90 degree) on a vector in the new coordination system,
what we do is translate it to the old system,
do the operation,
translate it back to the new.
$\mathbf{A}^{-1}\mathbf{BAx}$, $\mathbf{B}$ is the operation matrix, $\mathbf{A}$ is the translation matrix.
