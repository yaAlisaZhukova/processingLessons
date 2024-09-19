rectList = [] 
collected = 0

def setup():
  size(400, 500)
  chooseRandomXYPosition() 

def chooseRandomXYPosition():
    global rectList 
    for i in range(0, 5): 
        paramDictionary = {"x": int(random(0, width)), "y" : int(random(0,height))} 
        rectList.append(paramDictionary) 
     
        
def mousePressed():  
    global collected
    global rectList  
    for item in rectList: 
        if dist(mouseX, mouseY, item["x"], item["y"]) < 20:
           rectList.remove(item) 
           collected +=1 
              
def drawCoin():
    background(200) 
    for item in rectList:  
        fill(0,255,0) 
        ellipse(item["x"], item["y"], 20, 20)  
  
def draw():  
  drawCoin() 
  
  textSize(20) 
  fill(0) 
  text(collected,370,40)
  
   
  
 
   
  
   
