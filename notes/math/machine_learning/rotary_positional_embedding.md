# Rotary Positional Embedding

[[paper link](https://arxiv.org/abs/2104.09864)]

The idea of Rotary Positional Embedding (RoPE) is to only consider the relative
distance of two words in a transformer, not their absolute position in a
sentence.

This position information is used when we try to multiply the query and key of a
word. We want the result stay the same if the distance in the sentence (not in
the embedding space) between the two words are the same. The multiplication
result only consider the word embeddings and their relative distances.

In transformers, we get the embeddings of the tokens and modify that embedding
to get incorporate the position information of the token. With traditional
positional encoding, we just construct the vector and add to the embedding
vector element-wise. With RoPE, we directly alter the embedding of the words.


The process is like this, we first chop an n-dimensional embedding vector in to
many vectors of length 2, each of which is a vector in the 2-d plane. Then, we
rotate each of the vector by an angle $m \times\theta$, where $\theta$ is an
angle, which is the only hyperparameter needed for the algorithm, $m$ is the
position of the word in the sentence.

The inner product of 2 embeddings would not change as long as the word embedding
stays the same, and their distance in the sentence stay the same. This is
because when the relative position stay the same, the angle between the 2
vectors does not change for each of the 2-d vector pairs. Thus, when they add
up, the sum does not change.

In real computation, we just use a 2 by 2 matrix to multiply to perform the rotation.
The matrix is:

$$
R_\theta =
\begin{bmatrix}
\cos \theta & -\sin \theta \\
\sin \theta & \cos \theta
\end{bmatrix}
$$

For a concise math representation, complex numbers are often used to describe it.
For example, a complex number $z=a+b_i$ can be represented by a vector $(a, b)$
on a 2d plane. Rotating this vector by $\theta$ can be written as multiply it by
the matrix above. Then, if you apply Euler's formula: $e^{i\theta} =
\cos\theta + i\sin\theta$, you will get $z'=ze^{i\theta}$, where $z'$ is the
complex number representation for the rotated vector.