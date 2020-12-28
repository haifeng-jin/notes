# Derivatives

1. Calculus is mainly about calculating the area under a curve.
We set a starting point on the X-axis and set $x$ as the moving endpoint on the X-axis.

    If the curve is $f(x)$, and the area under the curve is $A(x)$.
We have $dA$ = $f(x)dx$,
where $dx$ is a very tiny length on the X-axis,
$f(x)dx$ is the area of the very thin rectangle at $x$.
$dA$ means the very small change of function $A$ from $x$ to $x+dx$.
From $dA=f(x)dx$, we have $dA/dx = f(x)$.
We call $f(x)$ the derivative of function $A$.

    To calculate the derivative of A: $\frac {dA}{dx}$ as $\frac{A(x+dx)-A(x)}{dx}$.
By some transformation we can get the result.
For example,
$A(x) = x^2$,
$\frac{dA}{dx} = \frac{(x+dx)^2-x^2}{dx} = \frac{2xdx + d^2x}{dx}= 2x + dx$.
Since $dx$ is very small, so $\frac{dA}{dx} = 2x$.

    Don't think $dx$ as infinitely small, but think of it as a comparatively small value.

2. Three rules of derivative.

    * Constant rule: $f'(x) = 0$
 
    * Sum rule: $(\alpha f(x)+ \beta g(x))' = \alpha f'(x) + \beta g'(x)$
 
    * Product rule: $(f(x)g(x))' = f'(x)g(x) + f(x)g'(x)$
 
    * Quotient rule: $\left({\frac {f(x)}{g(x)}}\right)'={\frac {f'(x)g(x)-f(x)g'(x)}{g^{2}(x)}}$
 
    * Chain rule: $(f(g(x)))' = f'(g(x))g'(x)$

3. A simple definition of the mathimatical constant $e$ is $(e^x)' = e^x$.

4. Implicit differentiation.

    For example, $f(x, y)=g(x, y)$.
    From this equation, we cannot directly see a form of $y=...$.
    We cannot directly calculate the derivative.
    What we know is this equation defines a curve (or some dots or something) in the plane.

    We can conclude $f'(x, y)=g'(x, y)$. Two questions needs to be answered.

    * Is $f'(x, y)$ the derivative of $x$ or $y$?
    It doesn't matter,
    since $dy$ can be seen as a function of $dx$,
    and vice versa.

    * Why they still equal when calculate derivative?
    The curve defined by $f(x, y)$=$g(x, y)$ constrain $x$ and $y$ to have a certain relationship.
    It might be the intervals, where $f$ and $g$ overlap.
    We don't need to consider single points overlaps since there is no derivative if they are scattered single points.
    Therefore, the equation is a definition of some curve in some intervals.
    As long as point $(x, y)$ is on the curve, we have $f(x, y)=g(x, y)$.
    Therefore, when we move a little bit $f$ changes by $df$, which is $f + df$,
    on the right of the equation is $g + dg$.
    Since $f=g$ and $f +df = g + dg$, $df =dg$.

