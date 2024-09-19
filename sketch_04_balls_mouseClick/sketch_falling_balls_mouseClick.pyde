rectArray = [] 
collected = 0

def setup():
  size(400, 500)
  chooseRandomXYPosition() 

def chooseRandomXYPosition():
    global rectArray 
    for i in range(0, 5): 
        paramDictionary = {"x": int(random(0, 400)), "y" : int(random(0,500))} 
        rectArray.append(paramDictionary) 
     
        
def mousePressed():  
    global collected
    global rectArray  
    for item in rectArray: 
        if dist(mouseX, mouseY, item["x"], item["y"]) < 20:
           rectArray.remove(item) 
           collected +=1 
              
def drawCoin():
    background(200) 
    for item in rectArray:  
        fill(0,255,0) 
        ellipse(item["x"], item["y"], 20, 20)  
  
def draw():  
  drawCoin() 
  
  textSize(20) 
  fill(0) 
  text(collected,370,40)
  
   
  
 
   
  
   
