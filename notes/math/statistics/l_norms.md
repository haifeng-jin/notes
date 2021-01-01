# L-Norms

$L^p$-norms are some functions which takes a vector as input and output a value.
It is written as $\left\|\mathbf x\right\|_ p$.

## L0-Norm
It is a measure of how many non-zero values are there in the vector.
If have to put it into notations, we need to first define $0^0=0$.
The the $L^0$-norm is as follows.

$$
\left\|\mathbf x\right\|_ 0 = |x_{1}|^{0}+|x_{2}|^{0}+\cdots +|x_{n}|^{0}
$$

## L1-Norm

$$
\left\|\mathbf x\right\|_ 1 = |x_{1}|+|x_{2}|+\cdots +|x_{n}|
$$

## L2-Norm

$$
\left\|\mathbf x\right\|_ 2 = \sqrt{x_{1}^{2}+x_{2}^{2}+\cdots +x_{n}^{2}}
$$

We also use its squared form quit often.

$$
\left\|\mathbf x\right\|_ 2^2 = x_{1}^{2}+x_{2}^{2}+\cdots +x_{n}^{2}
$$

## L-Infinity-Norm

$$
\left\|x\right\|_ {\infty }=\max \left\{|x_{1}|,|x_{2}|,\dotsc ,|x_{n}|\right\}
$$

## General Form 

For $0 < p < \infty $, we have the following general form.

$$
\left\|x\right\|_ {p}=\left(|x_{1}|^{p}+|x_{2}|^{p}+\dotsb +|x_{n}|^{p}\right)^{1/p}
$$

## Visualization

Following is a visualization of the contour line of different $p$ values with the norm value equal to 1.


<div>
<script type="text/paperscript" canvas="myCanvas">

function drawArrow(start, end, arrowSize) {
    arrowSize = arrowSize || 5;

    var path = new Path([start, end]);
    path.strokeColor = 'white';
    
    var vector = end - start;
    var arrowVector = vector.normalize(arrowSize);
    var arrowPath = new Path([
        end + arrowVector.rotate(135),
        end,
        end + arrowVector.rotate(-135),
    ]);
    arrowPath.strokeColor = 'white';
}
    
drawArrow(new Point(0, 150), new Point(300, 150));
drawArrow(new Point(150, 300), new Point(150, 0));

var center = new Point(150, 150);

var path0 = new Path.Rectangle(center - new Point(100, 100), 200);
path0.strokeColor = 'white';
path0.dashArray = [5, 5];

var text = new PointText(center + (new Point(1, -1))* 100);
text.justification = 'center';
text.fillColor = 'white';
text.content = '\u221E';
text.fontSize = 20;

function copy(path) {
    var path0 = path.clone();
    path0.rotate(90, center);
    var path0 = path.clone();
    path0.rotate(180, center);
    var path0 = path.clone();
    path0.rotate(270, center);
}

function drawIt(p) {
    var path = new Path();
    for (var i = 0; i < 90; i++) {
        var a = Math.tan(i * Math.PI / 180);
        var y = Math.pow(1.0/(Math.pow(a, p) + 1), 1.0/p);
        var x = a * y;
        path.add(center + (new Point(x, y)) * 100);
    }
    path.strokeColor = 'white';
    path.dashArray = [5, 5];
    copy(path);
    var textRadius = Math.pow(1.0 / 2, 1.0/p);
    var text = new PointText(center + (new Point(textRadius, -textRadius))* 100);
    text.justification = 'center';
    text.fillColor = 'white';
    text.content = p.toString();
    text.fontSize = 15;
}

drawIt(0.5);
drawIt(1.0);
drawIt(2.0);
drawIt(3.0);
drawIt(6.0);
</script>
<canvas id="myCanvas" width="300" height="300" resize></canvas>
</div>
