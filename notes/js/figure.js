function drawArrow(start, end, arrowSize) {
    arrowSize = arrowSize || 5;

    var path = new paper.Path([start, end]);
    path.strokeColor = 'white';
    var vector = end.subtract(start);
    var arrowVector = vector.normalize(arrowSize);
    var arrowPath = new paper.Path([
        end.add(arrowVector.rotate(135)),
        end,
        end.add(arrowVector.rotate(-135)),
    ]);
    arrowPath.strokeColor = 'white';
}
