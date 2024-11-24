x = [10,11,12]
y = [5,5,5]
appleX = 12
appleY = 10 
dx = 1 
dy = 0 
boxSize = 20  
gameover = False

def setup():
    size(600,600) 
    
def keyPressed():
    global dx, dy
    if keyCode == LEFT: 
       dx = -1
       dy = 0 
    elif keyCode == UP: 
       dx = 0
       dy = -1     
    elif keyCode == RIGHT: 
       dx = 1
       dy = 0    
    elif keyCode == DOWN: 
       dx = 0
       dy = 1  
    
def draw():
    background(255)
    global appleX, appleY, gameover 
    
    for i in range(0, width/boxSize):
      line(i*boxSize, 0, i*boxSize, height)
    
    for i in range(0, height/boxSize):
      line(0, i*boxSize, width, i*boxSize )
     
    for i in range(0, len(x)):  
        fill (0,255,0) 
        rect(x[i]*boxSize, y[i]*boxSize, boxSize, boxSize);
        
    fill(255,0,0);
    rect(appleX*boxSize, appleY*boxSize, boxSize, boxSize); 
      
    if not gameover:
        if(frameCount%18==0): 
            x.append(x[len(x)-1] + dx)
            y.append(y[len(y)-1] + dy)
            
            if x[len(x)-1] < 0 or x[len(x)-1] > width/boxSize or y[len(x)-1] < 0 or y[len(x)-1] > height/boxSize:
                gameover = True 
                        
            for i in range(0, len(x)-2): 
                if(x[len(x)-1] == x[i] and  y[len(y)-1] == y[i]):  #если коснется своего тела, то gameover
                   gameover = True 
            
            if x[len(x)-1]==appleX and y[len(x)-1]==appleY:
                appleX = int(random(0,width/boxSize))
                appleY = int(random(0,height/boxSize)) 
            else:    
                x.remove(x[0]) # удаляем хвост
                y.remove(y[0]) # удаляем хвост
    else:
        fill(0)
        textSize(30)
        text("GAME OVER", 20, height/2)    
