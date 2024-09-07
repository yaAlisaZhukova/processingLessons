boxtenX=1
boxtenSpeedX = 1

circleX = 300
circleY = 570


def setup():
    size(600, 600)
    
def goldenKey(): 
    strokeWeight(2)
    stroke(0)
    noFill()
    ellipse(30,30,25,25)
    
    line(42,30,125,30) 
    line(125,30,125,50)  
    line(105,30,105,50)
    
def door(): 
    fill(0)
    rect(500, 400, 550, 400)
    stroke(255)
    arc(580, 500, 20, 20, 0, PI, OPEN)   

def boxten(x): 
    strokeWeight(2)
    stroke(0)
    fill(128,0,128)
    ellipse(150+x,160,25,25)

    fill(128,0,128)
    strokeWeight(3)
    stroke(100,0,100)
    rect(90+x,90,100,100)
    stroke(148,0,148)
    rect(96+x,96,88,88)

    strokeWeight(2)
    stroke(0)
    fill(128,0,128)
    ellipse(150+x,160,25,25)

    fill(255)
    strokeWeight(2)
    stroke(0)
    ellipse(116+x,136,38,38)
    ellipse(165+x,137,38,38)

    fill(0)
    ellipse(116+x,136,25,25)
    ellipse(165+x,137,25,25)

    strokeWeight(3)
    stroke(148,0,148)
    line(96+x,96,105+x,105)
    line(184+x,96,175+x,105)
    line(96+x,185,105+x,175)
    line(184+x,184,175+x,175)

def keyPressed(): 
    global circleY
    global circleX 
    if key == CODED: 
        if (keyCode == DOWN ):
            circleY = circleY + 2
        elif keyCode == UP:
            circleY = circleY - 2
        elif keyCode == RIGHT:
            circleX = circleX + 2
        elif keyCode == LEFT:
            circleX = circleX - 2   
    
def draw():
    background(125)
    global boxtenX
    global boxtenSpeedX
    global circleY     
    
    if(boxtenX == 0  or boxtenX > 500): 
        boxtenSpeedX = boxtenSpeedX * -1
        
    boxtenX = boxtenX + boxtenSpeedX   
    boxten(boxtenX - 100)
    
    circle(circleX, circleY, 40)
    goldenKey()
    door()
    
    
     
