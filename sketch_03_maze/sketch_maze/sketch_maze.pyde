# ChatGPT -> Пример кода для обработки коллизий. лабиринт собираем сокровища python processing
#1 Стена
#0 Пол
#3 Сокровище

tilemap = [
   [1,1,1,1,1,1,1,1,1,1],
   [1,0,0,0,1,0,0,1,0,0],
   [1,1,2,0,1,0,0,0,0,1],
   [1,0,0,1,1,0,1,1,0,1],
   [1,1,0,1,1,0,1,1,1,1],
   [1,0,0,2,0,0,0,0,2,1],
   [1,0,0,1,1,1,1,0,0,1],
   [1,0,1,1,0,0,1,0,0,1],
   [1,0,0,0,0,2,1,1,0,1],
   [1,1,1,1,1,1,1,1,1,1] 
];
cellWidth = 64
cellHeight = 64
circlePositionX = 1
circlePositionY = 1
score = 0  

def setup():
    size(640,640)   

def renderMap(): 
    global score
    for j in range(0, len(tilemap)):
        for i in range(0, len(tilemap[0])):
            if tilemap[j][i] == 0:
                fill(80)
                rect(i*cellWidth, j*cellHeight, cellWidth, cellHeight)
            elif tilemap[j][i] == 1:
                fill(157, 219, 208)
                rect(i*cellWidth, j*cellHeight, cellWidth, cellHeight)
            elif tilemap[j][i] == 2: 
                if  circlePositionX == i  and circlePositionY == j: 
                    tilemap[j][i] = 0 # забрали сокровище
                    score +=1 
                fill(80)
                rect(i*cellWidth, j*cellHeight, cellWidth, cellHeight)
                fill(255, 145, 145)
                ellipseMode(CORNER)
                ellipse(i*cellWidth+10, j*cellHeight+10, cellWidth-20, cellWidth-20)  
                   
def keyPressed(): 
    global circlePositionX   
    global circlePositionY 
     
    if (keyCode == LEFT ):
        if tilemap[circlePositionY][circlePositionX-1] != 1:
            circlePositionX -= 1 
    elif keyCode == UP:
        if tilemap[circlePositionY-1][circlePositionX] != 1:
            circlePositionY -= 1
    elif keyCode == RIGHT:
        if tilemap[circlePositionY][circlePositionX+1] != 1:
            circlePositionX += 1  
    elif keyCode == DOWN:
        if tilemap[circlePositionY+1][circlePositionX] != 1:
            circlePositionY += 1 
        
def drawPlayer():
    circleX = (circlePositionX + 1) * cellWidth - cellWidth/2
    circleY = (circlePositionY + 1) * cellHeight - cellHeight/2
    fill(255,0,255)
    ellipseMode(CENTER)
    circle(circleX,circleY,64) 
          
def draw():
    background(120)
    renderMap()
    drawPlayer()  
    textSize(50)
    text(score, 600, 50) 
    

  

 
