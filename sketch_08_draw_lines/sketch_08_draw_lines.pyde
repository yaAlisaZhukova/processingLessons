def setup():
    background(205)
    size(600,600)
def draw():
    if mousePressed:
        line(mouseX,mouseY,pmouseX,pmouseY)
    if keyPressed:
        if key == 'w' or key == 'W':
            stroke(255)
        if key == 'e' or key == 'E':
            stroke(0,255,0)
        if key == 'r' or key == 'R':
            stroke(255,0,0)
        if key == 's' or key == 'S':
            stroke(0,0,255)
            
        if frameRate % 10 == 0:
            saveFrame("output/line-######.png")   
def mousePressed():
    if mouseButton == RIGHT:
        stroke(205)
    if mouseButton == LEFT:
        stroke(0)
