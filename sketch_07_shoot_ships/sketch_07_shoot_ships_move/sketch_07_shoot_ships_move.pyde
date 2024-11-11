shipList = [[-500], [-320], [100], [320],  [480]]
 
bullets = []
gunX = 280
gunY = 570
bullet_speed = 5
def setup():
    size(600,600)
    
def gun():
    fill(255, 154, 165)
    rectMode(CENTER)
    rect(gunX, gunY, 60, 20)
        
def keyPressed():
    global bullets
    if key == ' ': 
        bullets.append([gunY - 10]) 
        
def ship(x):    
    fill(122, 89, 255)
    rect(55+x,38,10,30)
    rect(50+x,40,6,20)
    quad(30+x, 50, 85+x, 50, 70+x, 75, 45+x, 75)
    
def draw():
     
    background(147)
    global circleList 
    gun()
    
    for bullet in bullets: 
        bullet[0] = bullet[0] - bullet_speed  
        circle(gunX, bullet[0], 20) 
  
    for shipX in shipList:
        ship(shipX[0]) 
        shipX[0] = shipX[0] + 1
        if shipX[0] == 650:
            shipX[0] = -50
            
    for bullet in bullets:
        for shipX in shipList:
            if dist(gunX, bullet[0], shipX[0]+50, 60) < 20:  
                bullets.remove(bullet)
                shipList.remove(shipX)
            
