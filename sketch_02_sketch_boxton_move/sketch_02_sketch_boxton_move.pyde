boxtenX=1
boxtenSpeedX = 1

circleX = 300
circleY = 570

goldenKeyX = 0
goldenKeyY = 0

goldenKeyTaken = False 

def setup():
    size(600, 600)
    
def goldenKey(x,y): 
    strokeWeight(5)
    stroke(0)
    noFill()
    ellipse(20+x,30+y,25,25)
    
    line(30+x,30+y,80+x,30+y) 
    line(80+x,30+y,80+x,50+y)  
    line(60+x,30+y,60+x,50+y)
    
def door(): 
    fill(0)
    rect(500, 400, 550, 400)
    stroke(255)
    arc(580, 500, 20, 20, 0, PI, OPEN)   

def boxten(x): 
    strokeWeight(2)
    stroke(0)
    fill(128,0,128)
    ellipse(60+x,160,25,25)

    fill(128,0,128)
    strokeWeight(3)
    stroke(100,0,100)
    rect(x,90,100,100)
    stroke(148,0,148)
    rect(6+x,96,88,88)

    strokeWeight(2)
    stroke(0)
    fill(128,0,128)
    ellipse(60+x,160,25,25)

    fill(255)
    strokeWeight(2)
    stroke(0)
    ellipse(26+x,136,38,38)
    ellipse(75+x,137,38,38)

    fill(0)
    ellipse(26+x,136,25,25)
    ellipse(75+x,137,25,25)

    strokeWeight(3)
    stroke(148,0,148)
    line(6+x,96,15+x,105)
    line(94+x,96,85+x,105)
    line(6+x,185,15+x,175)
    line(94+x,184,85+x,175)

def keyPressed(): 
    global circleY
    global circleX 
     
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
    global circleY, goldenKeyX, goldenKeyY, goldenKeyTaken
    textSize(40)
    
    door()     
    
    if(boxtenX == 0  or boxtenX > 500): 
        boxtenSpeedX = boxtenSpeedX * -1
        
    boxtenX = boxtenX + boxtenSpeedX   
    boxten(boxtenX) 
       
    if dist(circleX, circleY, boxtenX + 50, 190) < 40:
        noLoop() 
        text("GAME OVER", 200, 300)
    
    circle(circleX, circleY, 40)
    
    if dist(circleX, circleY, goldenKeyX, goldenKeyY+30) < 20:
       goldenKeyTaken = True
    
    if goldenKeyTaken:  
       goldenKey(circleX, circleY)
       if circleX > 500 and circleY > 400: 
          text(u"Вы победили", 200, 300)
          noLoop() 
    else:
       goldenKey(goldenKeyX, goldenKeyY)     
        
    
    
    
     
