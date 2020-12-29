# Taylor Theorem

The derivative of a derivative is a higher order derivative.

The Tyler theorem is about using polynomials to simulate a function around a certain $x$ point.
Non-polynomial functions are hard to deal with.
Therefore, we would like to use their polynomial approximation instead.

We just let the higher order of derivative equal to each other when $x=a$ between the original function and the polynomial.
Then they will be similar to each other near that $x=a$
since the higher order derivative is deciding the curve shapes of the function.

The formal definition of the Taylor theorem is as follows.
Let $k \geq 1$ be an integer and let the function $f : \textbf{R} \rightarrow \textbf{R}$ be $k$ times differentiable at the point $a \in \textbf{R}$.
Then there exists a function $h_k : \textbf{R} \rightarrow \textbf{R}$ such that

$$
f(x)=f(a)+f'(a)(x-a)+{\frac {f''(a)}{2!}}(x-a)^{2}+\cdots +{\frac {f^{(k)}(a)}{k!}}(x-a)^{k}+h_{k}(x)(x-a)^{k},
$$

and

$$
\lim_{x\to a}h_{k}(x)=0
$$.

If we ignore the last term with $h_k$ and let $x=a$,
and get any order (let's say $n$th order) of derivative of the right side of the equation,
we will get $f^n(a)$.
All the rest terms became 0.
The former terms will become constants and becomes zero during the calculation of higher order derivatives.
The latter terms will become zero since they contain $(x-a)$.
Therefore, you calculate any order of derivative of the equation on both sides, they results in the same value at the point of $x=a$.

The remainder is just another term to describe the error of the approximation.
