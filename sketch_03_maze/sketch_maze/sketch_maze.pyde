#tilemap https://www.youtube.com/watch?v=Byo5Pepe3cg
#1 is wall
#0 is floor
#int [] maprow = {1,1,1,1,1,1,1,1,1,1};
tilemap = [
   [1,1,1,1,1,1,1,1,1,1],
   [1,0,0,0,1,0,0,1,0,0],
   [1,1,0,0,1,0,0,0,0,1],
   [1,0,0,1,1,0,1,1,0,1],
   [1,1,0,1,1,0,1,1,1,1],
   [1,0,0,0,0,0,0,0,0,1],
   [1,0,0,1,1,1,1,0,0,1],
   [1,0,1,1,0,0,1,0,0,1],
   [1,0,0,0,0,0,1,1,0,1],
   [1,1,1,1,1,1,1,1,1,1] 
];
cellWidth = 64
cellHeight = 64
circlePositionX = 1
circlePositionY = 1  

def setup():
    size(640,640)   

def renderMap(): 
    for j in range(0, len(tilemap)):
        for i in range(0, len(tilemap[0])):
            if tilemap[j][i] == 0:
                fill(80)
                rect(i*cellWidth, j*cellHeight, cellWidth, cellHeight)
            elif tilemap[j][i] == 1:
                fill(157, 219, 208)
                rect(i*cellWidth, j*cellHeight, cellWidth, cellHeight)
                   
def keyPressed(): 
    global circlePositionX   
    global circlePositionY 
    if key == CODED: 
        if (keyCode == LEFT ):
            if tilemap[circlePositionY][circlePositionX-1] == 0:
                circlePositionX -= 1 
        elif keyCode == UP:
            if tilemap[circlePositionY-1][circlePositionX] == 0:
                circlePositionY -= 1
        elif keyCode == RIGHT:
            if tilemap[circlePositionY][circlePositionX+1] == 0:
                circlePositionX += 1  
        elif keyCode == DOWN:
            if tilemap[circlePositionY+1][circlePositionX] == 0:
                circlePositionY += 1 
        
def drawPlayer():
    circleX = (circlePositionX + 1) * cellWidth - cellWidth/2
    circleY = (circlePositionY + 1) * cellHeight - cellHeight/2
    fill(255,0,0)
    circle(circleX,circleY,64) 
          
def draw():
    background(120)
    renderMap()
    drawPlayer()  
    

  

 
