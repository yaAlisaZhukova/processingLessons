playerX = 50
playerY = 250
velocityX = 0
velocityY = 0
onGround = False
getSward = False

def setup():
    global breezeNoSward, breeze, sward, getSward
    size(600, 400) 
    breezeNoSward = loadImage('breezeNoSward.png')
    breeze = loadImage('breeze.png')
    sward = loadImage('sward.png')

def draw():
    global onGround, playerX, playerY, velocityX, velocityY, getSward 
    background(135, 206, 235)  # Голубое небо
    
    push()
    fill(200, 130, 10)
    noStroke()
    rect(0, 380, 600, 20)
    pop()

    # Гравитация
    if not onGround:
        velocityY += 0.5
    
    # Движение 
    playerX += velocityX
    playerY += velocityY

    # Пол (простая платформа)
    groundY = height - 140
    if playerY >= groundY:
        playerY = groundY
        velocityY = 0
        onGround = True
    else:
        onGround = False

    # Рисуем игрока
    fill(255, 0, 0) 
    if getSward: 
       image(breeze,  playerX, playerY, 81, 135)
    else:
       image(breezeNoSward,  playerX, playerY, 81, 135) 
    
    # Рисуем платформу
    fill(0, 255, 0)
    rect(350, 300, 200, 10)  # Пример платформы 
    if not getSward:
        image(sward, 400, 280, 106, 30)
      
    
    # Проверка столкновения с платформой
    if (350 < playerX < 500 and playerY + 81 >= 250 and velocityY > 0):
        playerY = 250 - 81
        velocityY = 0
        onGround = True
        getSward = True

def keyPressed():
    global onGround, velocityX, velocityY
    if key == ' ' and onGround:  # Прыжок по пробелу
        velocityY = -15
        onGround = False
    if keyCode == LEFT:  # Движение влево
        velocityX = -3
    if keyCode == RIGHT:  # Движение вправо
        velocityX = 3

def keyReleased():
    global velocityX
    if keyCode in (LEFT, RIGHT):
        velocityX = 0