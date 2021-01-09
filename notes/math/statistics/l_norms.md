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

We also use its squared form quite often.

$$
\left\|\mathbf x\right\|_ 2^2 = x_{1}^{2}+x_{2}^{2}+\cdots +x_{n}^{2}
$$

## L-Infinity-Norm

$$
\left\|x\right\|_ {\infty }=\max \left\{|x_{1}|,|x_{2}|,\dotsc ,|x_{n}|\right\}
$$

## General Form 

For $0< p< \infty$, we have the following general form.

$$
\left\|x\right\|_ {p}=\left(|x_{1}|^{p}+|x_{2}|^{p}+\dotsb +|x_{n}|^{p}\right)^{1/p}
$$

## Visualization

Following is a visualization of the contour line of different $p$ values with the norm value equal to 1.


<div>
<!-- Define inlined JavaScript -->
<script type="text/javascript" src="/js/figure.js"></script>
<script type="text/javascript">
// Only executed our code once the DOM is ready.
window.onload = function() {
	// Get a reference to the canvas object
	var canvas = document.getElementById('myCanvas');
	// Create an empty project and a view for the canvas:
	paper.setup(canvas);
    draw();
	// Draw the view now:
	paper.view.draw();
}

function draw() {
    drawArrow(new paper.Point(0, 150), new paper.Point(300, 150));
    drawArrow(new paper.Point(150, 300), new paper.Point(150, 0));
    
    var center = new paper.Point(150, 150);
    
    var path0 = new paper.Path.Rectangle(center.subtract(new paper.Point(100, 100)), 200);
    path0.strokeColor = 'white';
    path0.dashArray = [5, 5];
    
    var text = new paper.PointText(center.add(new paper.Point(1, -1).multiply(100)));
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
        var path = new paper.Path();
        for (var i = 0; i < 90; i++) {
            var a = Math.tan(i * Math.PI / 180);
            var y = Math.pow(1.0/(Math.pow(a, p) + 1), 1.0/p);
            var x = a * y;
            path.add(center.add((new paper.Point(x, y)).multiply(100)));
        }
        path.strokeColor = 'white';
        path.dashArray = [5, 5];
        copy(path);
        var textRadius = Math.pow(1.0 / 2, 1.0/p);
        var text = new paper.PointText(center.add((new paper.Point(textRadius, -textRadius)).multiply(100)));
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
}
</script>
<canvas id="myCanvas" width="300" height="300"></canvas>
</div>
