#ГАЧА 3.0  
sc = 0
guy = 1
def setup():
    global one, two, three, four, five, six, seven, eight, nine
    background(255)
    one = loadImage ('1.png')
    two = loadImage ('2.png')
    three = loadImage ('3.png')
    four = loadImage ('4.png')
    five = loadImage ('5.png')
    six = loadImage ('6.png')
    seven = loadImage ('7.png')
    eight = loadImage ('8.png')
    nine = loadImage ('9.png')
    size(600,600)
     
def draw(): 
    global sc, guy  
    if keyPressed:
        if key == '3':
            guy = 3
        if key == '2':
            guy = 2
        if key == '1':
            guy = 1
    if guy == 1:
        shelly()         
    if guy == 2:
        breeze()
    if guy == 3:
        toodles()
        
def shelly():
    global sc
    sc = sc + 1
    if sc == 1:
        background(255)
        one = loadImage ('2.png')
        image(one,120,80,321,411)
    if sc == 20:
        background(255)
        one = loadImage ('1.png')
        image(one,170,100,242,378)
    if sc == 40:
        background(255)
        one = loadImage ('2.png')
        image(one,120,80,321,411)
    if sc == 60:
        background(255)
        one = loadImage ('3.png')
        image(one,160,90,257,401)
    if sc == 80:
        sc = 0
        
def breeze():
    global sc
    sc = sc + 1
    if sc == 1:
        background(255) 
        image(four,130,90,271,387)
    if sc == 20:
        background(255) 
        image(five,130,90,273,385)
    if sc == 40:
        background(255) 
        image(six,130,90,260,390)
    if sc == 60:
        background(255) 
        image(five,130,90,273,385)
    if sc == 80:
        sc = 0
        
def toodles():
    global sc
    sc = sc + 1
    if sc == 1:
        background(255) 
        image(seven,145,100,228,374)
    if sc == 20:
        background(255) 
        image(eight,135,100,266,370)
    if sc == 40:
        background(255) 
        image(nine,145,100,211,372)
    if sc == 60:
        background(255) 
        image(eight,135,100,266,370)
    if sc == 80:
        sc = 0
