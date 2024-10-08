bullets = []
gunX = 280
gunY = 570
bullet_speed = 5

def setup():
    size(600, 600) 
    
def gun():
    fill(255, 154, 165)
    rect(gunX, gunY, 60, 20)
        
def keyPressed():
    global bullets
    if key == ' ': 
        bullets.append([gunY - 10])
       
def draw():
    background(134)
    gun()
    for bullet in bullets: 
        bullet[0] = bullet[0] - bullet_speed 
        circle(gunX + 30, bullet[0], 20)
        
 
