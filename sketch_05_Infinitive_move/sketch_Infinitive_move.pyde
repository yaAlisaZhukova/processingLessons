dx = 0
circleY = 540;
frameNumberOnClick = 10000 
def setup():
    size(1200, 600)
    
def pick(x):
    noStroke()
    fill(255, 123, 123)
    rect(150+x, 520, 10, 40)
    triangle(143+x, 525, 168+x, 525, 153+x, 510)
    
def block(x):
    noStroke()
    fill(123, 123, 255)
    rect(150+x, 440, 80, 40)

def keyPressed():
    global circleY
    global frameNumberOnClick
    frameNumberOnClick = frameCount 
     
    if keyCode == UP:
        circleY = circleY - 70               
    
def draw():
    background("#E3FBFC")
    global dx
    global circleY
    
    fill(123, 255, 120)
    circle(25, circleY, 30)
    pickXList = [0,240,500, 690, 950, 1200, 1340, 1500, 1690, 1850, 2010]
    for i in pickXList: 
        pick(i+dx)  
    
    if dx < -1200:
        dx = 0
    dx = dx - 1
    
    blockXList = [500, 690, 810 ]
    for i in blockXList: 
        block(i+dx)
    
    if frameCount > frameNumberOnClick + 70:
        circleY = 540        
     
     
    
     
    
