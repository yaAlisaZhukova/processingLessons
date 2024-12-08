#ГАЧА 3.0  
sc = 0
guy = 1
imageX = 130
def setup():
    global one, two, three, four, five, six, seven, eight, nine, imageNumber
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
    imageNumber = two
    size(600,600)
     
def draw(): 
    global sc, guy, imageX
    background(255)  
    if keyPressed:
        if key == '3':
            guy = 3
        if key == '2':
            guy = 2
        if key == '1':
            guy = 1
        if keyCode == LEFT:    
            imageX = imageX - 1
        if keyCode == RIGHT:    
            imageX = imageX + 1
    if guy == 1:
        shelly()         
    if guy == 2:
        breeze()
    if guy == 3:
        toodles()
        
def shelly():
    global sc, imageNumber, imageX 
    sc = sc + 1 
    if sc == 1: 
        imageNumber = two  
    if sc == 20: 
        imageNumber = one  
    if sc == 40: 
        imageNumber = two 
    if sc == 60: 
        imageNumber = three  
    if sc == 80:
        sc = 0
        
    image(imageNumber,imageX,90,260,400) 
      
def breeze():
    global sc, imageNumber, imageX
    sc = sc + 1
    if sc == 1:
        imageNumber = four 
    if sc == 20:
        imageNumber = five 
    if sc == 40:
        imageNumber = six 
    if sc == 60:
        imageNumber = five 
    if sc == 80:
        sc = 0
        
    image(imageNumber,imageX,90,260,400)
        
def toodles():
    global sc, imageNumber, imageX
    sc = sc + 1
    if sc == 1:
        imageNumber = seven 
    if sc == 20:
        imageNumber = eight 
    if sc == 40:
        imageNumber = nine 
    if sc == 60:
        imageNumber = eight  
    if sc == 80:
        sc = 0
        
    image(imageNumber,imageX,90,260,400)     
