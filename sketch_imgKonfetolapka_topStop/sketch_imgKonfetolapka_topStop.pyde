y = 300
speedY = 1 
def setup(): 
    global konfetolapkaImage
    size(640, 360)
    konfetolapkaImage = loadImage("konfetolapka1.png")
  
def drawKonfetolapka(y):
    image(konfetolapkaImage, 320, y, 50, 50)     

def draw():
    background(255)
    global y
    global speedY 
    
    if(y <= 0):  
       speedY = 0   
                  
    y = y - speedY 
     
    drawKonfetolapka(y)
    
