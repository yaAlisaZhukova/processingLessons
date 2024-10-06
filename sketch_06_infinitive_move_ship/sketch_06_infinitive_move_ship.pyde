dx = 0
shipXList = [-590, -400, -320, -210, -88, 44, 200, 440, 590]
def setup():
    size(600, 600)
    
def ship(x):    
    fill(122, 89, 255)
    rect(54+x,25,10,40)
    rect(48+x,30,6,20)
    quad(30+x, 49, 86+x, 49, 69+x, 76, 45+x, 76)
    
def draw():
    background(155)
    global dx
    for x in shipXList:
       ship(x + dx)
    if dx == 600:
        dx = 0    
    dx = dx + 1   
    
