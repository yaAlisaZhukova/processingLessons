Forum Processsing Python
https://discourse.processing.org/
*****************************************************************************************************************
                                                Lesson 1
*****************************************************************************************************************
![alt text](https://github.com/Elenn/processing_lessons/blob/main/How/01_Lesson_Circle.png?raw=true)
--------------------------------------------- 
0. Задание: 
Нарисуй снеговика
----------------------------------------
1.
- Даунлодим Processing
https://processing.org/download

-  Распаковываем zip
processing-4.3-windows-x64.zip

- Раним processing.exe

- Добавляем Python

Java -> Manage Models -> Python
-> Python Mode for Processing 4 -> Install

--------------------------------------
2. Раню первый скрипт
```
size(640, 360)
circle(320, 180, 100)
```
Где 320 - позиция центра x,
    180 - позиция центра y,
	100 - диаметр
	
circle(0, 0, 100) - координаты идут с верхнего левого угла	

---------------------------------------
3. Сохраняю как папку 
sketch_HelloCircle

в которой файл с кодом сохраняется как

sketch_HelloCircle.pyde

-----------------------------------------
4. setup() & draw()

C:\web\AlicaPython\Git\01_Lesson_Circle\sketch_setup_draw
```
def setup():
  size(640, 360)
  background(0)

def draw():
  noStroke()
  fill(255, 100, 200)
  circle(320, 180, 100)
```


------------------------------------------
5. Ты можешь рисовать и другие фигуры
https://processing.org/reference  

2d Primitives:
	circle() 
	ellipse()  
	line() 
	point() 
	rect() 
	square() 
	triangle()
-----------------------------------------
6. 
- Для того, что бы посмотреть, какие параметры нужны для каждой фигуры
- Выдели название фигуры
- Правая кнопка -> Find in Reference
- Смотрим параметры Parameters
- Так для круга
первый параметр x-coordinate (координата x)
второй параметр y-coordinate (координата y)
третий параметр width and height (ширина и длинна)

![alt text](https://github.com/Elenn/processing_python/blob/main/01_Lesson/How/references.png?raw=true)
![alt text](https://github.com/Elenn/processing_python/blob/main/01_Lesson/How/circleReference.png?raw=true)  
**************************************************************************************************************
                                               Lesson 2
**************************************************************************************************************

![alt text](https://github.com/Elenn/processing_python/blob/main/02_Lesson/how/lesson_02.png?raw=true)

0. Задание:
- Создай фигуру, состоящую из 
rect(), square(), triangle(), circle() or line()
- Перенеси код для фигуры в метод
- Вызови этот метод несколько раз с разными параметрами, так, что бы фигура
оказалась нарисована несколько раз
-----------------------------------------------
1. - Создай фигуру, в которой используются

    rect()
    square()  
    triangle() 
    circle()

- Раскрась их в разные цвета с помошью fill()
- Образец:
```
def setup():
    size(640, 360)
    
def draw():
    background("#FFFFCC")
    
    fill("#006600")
    rect(390, 135, 30, 100)
    square(320, 200, 100) 
    
    fill("#666600")
    triangle(320, 200, 370, 150, 420, 200) 
    
    square(350, 240, 40)  
    
    fill("#FFFF00")
    circle(10,10,100) 
```	

size(600,600)
fill(128,0,128)
strokeWeight(3)
stroke(100,0,100)
rect(90,90,100,100)

stroke(148,0,148)
rect(96,96,88,88)
------------------------------------------------------
2. - Перенеси код для твоей фигуры в метод
- Вызови твой метод внутри метода draw()
- Образец:

```
def setup():
    size(640, 360)
    frameRate(1)
    
def house():
    fill("#006600")
    rect(390, 135, 30, 100)
    square(320, 200, 100) 
    
    fill("#666600")
    triangle(320, 200, 370, 150, 420, 200) 
    
    square(350, 240, 40)  
    
def draw():
    background("#FFFFCC")  
     
    house() 
    
    fill("#FFFF00")
    circle(10,10,100) 
```
---------------------------------------------------
3. Метод с параметрами
- Я хочу вызывать метод несколько раз с разными
значениями параметра x
- В результате будет нарисовано несколько фигур
```
x = 320
y = 135

def setup():
    size(640, 360)
    frameRate(1)
    
def house(x,y):
    fill("#006600")
    rect(x + 70, y, 30, 100)
    square(x, 200, 100) 
    
    fill("#666600")
    triangle(x, y + 65, x + 50, y + 15, x + 100, 200) 
    
    square(x + 30, y + 105, 40) 
     
    
def draw():
    background("#FFFFCC")  
     
    house(x,y)
    house(x+150,y)
    house(x-150,y)
    
    fill("#FFFF00")
    circle(10,10,100)
``` 
***********************************************************************************************************************
                                                     Lesson 3
***********************************************************************************************************************

![alt text](https://github.com/yaAlisaZhukova/processingLessons/blob/main/How/ball_x_y_back_forth.gif?raw=true) 

0. Задание: Создай/модифицируй програмку, что бы шарик отскакивал от прямоугольника внизу,
а не от нижнего края.

- План создания программки:
- Надо нарисовать шарик
- Заставить его двигаться
- При столкновении с границами, шарик должн менять направление

--------------------------------------------------------------------------
1. Переменные

- мы объявляем глобальные переменные x и y, которые доступны и внутри любого метода.
- теперь мы создаем круг, используя переменные.

```
y=10
x=10

def setup():
    size(640, 360)  
    
def draw():
    background(0)  
    
    circle(x, y, 50) 
```
--------------------------------------------------------------------------
2. изменяем значение глобальной переменной внутри метода

- глобальные переменные доступны внутри любого метода.

- но для того, что бы изменить их значение надо использовать
global перед именем переменной 

- метод draw() в среде разработки Processing вызывается много раз.
Мы написали код, когда каждый раз при вызове этого метода значение x увеличивается на 1:
x = x + 1

- визуально мы видим это, как движение шарика

 
``` 
y=10
x=10

def setup():
    size(640, 360)  
    
def draw():
    background(0) 
    
    global x
	
    x = x + 1  
    
    circle(x, y, 50) 
```
---------------------------------------------------------------------
3. Двигаем шарик по X
```
x = 10
speedX = 1 
def setup():  
    size(640, 360) 
      

def draw():
    background(255)
    global x
    global speedX  
    
    x = x + speedX 
     
    ellipse(x, 100, 20,20)
```	
---------------------------------------------------------------------
4. Двигаем шарик по Y
```
y = 300
speedY = -1 
def setup():  
    size(640, 360) 
      

def draw():
    background(255)
    global y
    global speedY   
    
    y = y + speedY 
     
    ellipse(100, y, 20,20)
```	 
---------------------------------------------------------------------
5. Двигаем круг в двух направлениях x и y
(по вертикали и по горизонтали)

```
y=10
x=10

def setup():
    size(640, 360)  
    
def draw():
    background(0) 
    
    global x
    global y
    x = x + 1 
    y = y + 1 
    
    circle(x, y, 50)
```	
---------------------------------------------------------------------
6. Двигается шарик туда обратно по X
```
x = 10
speedX = 1 
def setup():  
    size(640, 360) 
      

def draw():
    background(255)
    global x
    global speedX 
    
    if(x <= 0):  
       speedX = 1   
    elif(x > width): 
       speedX = -1
                  
    x = x + speedX 
     
    ellipse(x, 100, 20,20)
```	
---------------------------------------------------------------------
7. Двигается шарик туда обратно по Y
```
y = 300
speedY = -1 
def setup(): 
    global konfetolapkaImage
    size(640, 360) 
      

def draw():
    background(255)
    global y
    global speedY 
    
    if(y <= 0):  
       speedY = 1   
    elif(y > height): 
       speedY = -1
                  
    y = y + speedY 
     
    ellipse(100, y, 20,20)
```	
--------------------------------------------------------------------
8. Двигается шарик туда обратно по X и Y
```	
x = 10
y = 10
speedX = 1 
speedY = 1 
def setup():  
    size(640, 360) 
      

def draw():
    background(255)
    global x
    global y
    global speedX  
    global speedY 
    
    if(x <= 0):  
       speedX = 1   
    elif(x > width): 
       speedX = -1
    elif(y <= 0):  
       speedY = 1   
    elif(y > height): 
       speedY = -1
                  
    x = x + speedX 
    y = y + speedY
     
    ellipse(x, y, 20,20)
```		
---------------------------------------------------------------------
9. Имидж. 
- сохраняем имидж с прозрачным фоном в проект
\sketch_imgKonfetolapka\konfetolapka1.png 

``` 
def setup(): 
    global konfetolapkaImage
    size(640, 360)
    konfetolapkaImage = loadImage("konfetolapka1.png")  
      

def draw():
    background(255)
    image(konfetolapkaImage, 320, 300, 50, 50)
```
---------------------------------------------------------------------
10. Имидж движется вверх и когда достигает верха, то останавливается

```
y = 300
speedY = 30 
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
```
---------------------------------------------------------------------
11. Имидж движется вверх и когда достигает верха, то идет вниз

```
y = 300
speedY = -1 
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
    
    print y 
    if(y == 0):  
       speedY = 1   
            
    y = y + speedY 
     
    drawKonfetolapka(y)
```
---------------------------------------------------------------------
12. Имидж движется вверх и когда достигает верха, то идет вниз,
Когда достигает нижней границы, то идет вверх

```
y = 300
speedY = -1 
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
       speedY = 1   
    elif(y > height): 
       speedY = -1
                  
    y = y + speedY 
     
    drawKonfetolapka(y)
```  
------------------------------------------------------------------
13. Меняем направление движения шарика, когда он сталкивается с краями

- добавляем переменные speedX, speedY, которые меняют свое значение на противоположное
(то есть 1 на -1), когда шарик сталкивается с краями

- то есть движение вниз:
y = y + 1

меняется на движение вверх:
y = y - 1 


- после того, как мы объявили размер экрана в строчке size(640, 360),
- переменная width, принимает значени, объявленноя нами, то есть 640 
- переменная height, принимает значени, объявленноя нами, то есть 360

```	
y=10
x=10
speedX = 1
speedY = 1

def setup():
    size(640, 360)  
    
def draw():
    background(0) 
    
    global x
    global y
    global speedX
    global speedY
    
    if(x == 0  or x > width ): 
        speedX = speedX * -1 
    elif( y == 0  or y > height):
        speedY = speedY * -1   
                                   
    x = x + speedX
    y = y + speedY
    
    circle(x, y, 50)
```
----------------------------------------
14. Добавили прямоугольник внизу, 
пожалуйста выполните 

Задание: Создай/модифицируй програмку, что бы шарик отскакивал от прямоугольника внизу,
а не от нижнего края.		
*********************************************************************************************************************
                                                     Lesson 4
												  mousePressed()	 
*********************************************************************************************************************

![alt text](https://github.com/Elenn/processing_python/blob/main/04_Lesson/how/mousePressed.png?raw=true) 

0. Задание: Написать код, когда при нажатии мышки
меняется цвет круга на случайный: r = random(0, 255)
- то есть использовать в fill(255, 100, 200) 
переменные fill(r,b,g)
- что бы их изменить в методе mousePressed()
надо объявить эти три переменные global
----------------------------------------------
1. mousePressed()
- При нажатии на мышку, шарик появляется в другой позиции по x

```
circleX = 100

def setup():
    size(640, 360)
        
def mousePressed():
    global circleX
    circleX = 400 
        
    
def draw(): 
    background("#FFFFCC")  
     
    noStroke()
    fill(255, 100, 200)
    circle(circleX, 180, 100)  
```	
----------------------------------------------
2. mousePressed()
- При нажатии на мышку, шарик начинает опять движение с крайней левой точки

```
circleX = 10

def setup():
    size(640, 360)
        
def mousePressed():
    global circleX
    circleX = 0 
        
    
def draw():
    global circleX
    background("#FFFFCC")  
     
    noStroke()
    fill(255, 100, 200)
    circle(circleX, 180, 100)
    
    circleX = circleX + 1; 
```	
---------------------------------------------
3. mousePressed()
- При нажатии на мышку, шарик останавливается

```
speedX = 4 
def setup():  
    size(640, 360) 
    
def mousePressed():
    global speedX
    speedX = 0      

def draw():
    background(255)
    global x
    global speedX 
    
    if(x <= 0):  
       speedX = 4 
    elif(x > width):  
       speedX = -4    
                  
    x = x + speedX
     
    ellipse(x, 200, 30, 30)
```

--------------------------------------------------
4. 
- mouseX 
- mouseY
- При нажатии на мышку, шарик появляется в месте, где мы нажали мышку
   
```
circleX = 10
circleY = 180

def setup():
    size(640, 360)
        
def mousePressed():
    global circleX
    global circleY
    circleX = mouseX 
    circleY = mouseY
        
    
def draw():
    global circleX
    background("#FFFFCC")  
     
    noStroke()
    fill(255, 100, 200)
    circle(circleX, circleY, 100)
    
    circleX = circleX + 1; 
``` 
-----------------------------------------------
5. 
- move mouse => change background
- Двигаем мышку в правую/левую половину экрани - меняется фон экрана
```
def setup():
  size(640, 360) 
  

def draw():  
  if mouseX > 320:
     background(255)
  else:
     background(0) 
   
  
  stroke(127)
  strokeWeight(4)
  line(320,0,320, height)
```
----------------------------------------------
6. 
- добавляем степень прозрачности для fill(), четвертый параметр
- random(50, 120) - случайное значение от 50 до 120
- меняется размер шарика от 50 до 120 пикселей
 
``` 
circleX = 10
circleY = 180

def setup():
    size(640, 360)
        
def mousePressed():
    global circleX
    global circleY
    circleX = mouseX 
    circleY = mouseY
        
    
def draw():
    global circleX
    background("#FFFFCC")  
    circleSize = random(50, 120);
     
    noStroke()
    fill(0, 255, 0, 28);
    circle(circleX, circleY, circleSize)
    
    circleX = circleX + 1;
```
---------------------------------------------------------
7. toggle
startMoving = not startMoving
- нажимаем первый раз - движение останавливается
- нажимаем второй раз - движение начинается

```
circleX = 10
circleY = 180
startMoving = True

def setup():
    size(640, 360)
        
def mousePressed():
    global circleX
    global circleY
    global startMoving
	
    circleX = mouseX 
    circleY = mouseY
    startMoving = not startMoving  
    
def draw():
    global circleX
    background("#FFFFCC")  
     
    noStroke()
    fill(0, 255, 0);
    circle(circleX, circleY, 80)
    
    if startMoving:
        circleX = circleX + 1; 
```	
----------------------------------------------
8. toggle
При нажатии на мышку, шарик исчезает, 
при нажатии второй раз шарик появляется

```
showCirle = True

def setup():
    size(640,320)
    
def mousePressed():
    global showCirle 
    showCirle =  not showCirle 
    
def draw():
    background(127) 
    if showCirle:
        circle(100, 100, 50) 
```
--------------------------------------------
9. keyPressed()
   keyCode 
При нажатии на стрелочку '->' шарик перемещается вправо

```
x = 50
def setup():
    size(600, 600)
    
def keyPressed():
    global x
    if (key == CODED):  
        if (keyCode == RIGHT): 
           x = x + 100   
            
def draw():
    background(145)
    global x
    ellipse(x, 200, 50, 50)
```	
----------------------------------------------------------
10. keyPressed() 
    key 
При нажатии на букву 'z' шарик перемещается вправо

```
x = 50
def setup():
    size(600, 600)
    
def keyPressed():
    global x 
    if (key == 'z'): 
        x = x + 100   
            
def draw():
    background(145)
    global x
    ellipse(x, 200, 50, 50)	
```	
**********************************************************************************************************************
                                                       Lesson 5
**********************************************************************************************************************   

![alt text](https://github.com/Elenn/processing_python/blob/main/05_Lesson/how/nestedLoops.png?raw=true)

0. Задание: Создать поле из разноцветных квадратов (см. картинку)
случайных цветов
--------------------------
1. - for loop, range
- range(0, 64) вызываем исполнения кода внутри for loop 
каждый раз от 0 до 63 
-(то есть x принимает последовательно значения 0, 1, 2, 3 . . .63)
- circle(x*10, 180, 10) - позиция x умножается на 10, на ширину круга, что бы они не перекрывались
```
def setup():
   size(640, 360) 
 
def draw():
   background(0);
   fill(255) 
   
   for x in range(0, 64): 
       circle(x*10, 180, 10)
```	   
----------------------------
2. - for loop, range, increment by 10
- вызываем исполнения кода внутри for 
каждый раз от 0 до 639 с шагом 10
-(то есть x принимает последовательно значения 0, 10, 20, 30 . . .630)


```
def setup():
   size(640, 360) 
 
def draw():
   background(0);
   fill(255) 
   
   for x in range(0, 640, 10): 
       circle(x, 180, 10)
```	 
-------------------------------------
3. - Вложенные циклы: Nested for loops;
- noLoop() - вызываем метод draw() только одина раз 
- то есть мы повторяем созданную нами строчку из кругов еще и по высоте (y) 
- ellipseMode(CORNER): круг, это часный случай элипса, когда ширина равна высоте,
поэтому мы используем ellipseMode 
- значение CORNER - значит, что позицию x и y мы определяем у левого верхнего
угла квадрата, в который вписан наш круг
```
def setup():
   size(640, 360)
   noLoop()   
 
def draw():
   background(0);
   fill(255)
   circleWidth = 60 
   
   ellipseMode(CORNER)  
   
   for x in range(0, 640/circleWidth + 1): 
       for y in range(0, 360/circleWidth): 
           circle(x*circleWidth, y*circleWidth, circleWidth)
```		   
************************************************************************************************************************
                                                    Lesson 6
													List
************************************************************************************************************************

![alt text](https://github.com/Elenn/processing_python/blob/main/06_Lesson/how/listShow.png?raw=true)

0. - Задача: Есть лист(список), который содержит положительные и отрицательные целые значения
```
myList = [3, -9, 8, 54, -1, 2]
```
- Если значение отрицательное, то заменить его на соответствующее положительное значение,
то есть -3 на 3.
- Представить в виде набора прямоугольников соответствующей длинны, перед которыми написано значение
---------------------------------------------------
1. Рисуем несколько кругов в ряд с позицией x из List
```
clrcleX = []
def setup():
    global clrcleX
    size(640, 320) 
    clrcleX = [30, 150, 480]
    
def draw(): 
    for x in clrcleX:
        fill(255,0,0)
        circle(x,150,50) 
``` 
---------------------------------------------------------- 
2. Рисуем несколько кругов в случайном месте канвы по x из List
```
clrcleXList = []
def setup():
    global clrcleXList
    size(640, 320) 
    clrcleXList = [random(20, 630), random(20, 630),random(20, 630), random(20, 630), random(20, 630)]
    
def draw(): 
    y = 0
    for x in clrcleXList:
        y += 50 
        fill(255,0,0)
        circle(x,y,30)
```	
-------------------------------------------------------------	
3. List append. Рисуем несколько кругов в случайном месте канвы по x из List
```
clrcleXList = []
def setup():
    global clrcleXList
    size(640, 320) 
    for i in range(0, 5):
       clrcleXList.append(random(20, 630))
    
def draw(): 
    y = 0
    for x in clrcleXList:
        y += 50 
        fill(255,0,0)
        circle(x,y,30)
```	
------------------------------------------------------------------
4. List of Dictionary. Рисуем несколько кругов в случайном месте канвы по x из List
```
clrcleParamList = []
def setup():
    global clrcleParamList
    size(640, 320) 
    
    for i in range(0, 5): 
       paramDictionary = {"x": int(random(20, 630)), "r": random(0, 255), "g": random(0, 255), "b": random(0, 255)} 
       clrcleParamList.append(paramDictionary)
    
def draw(): 
    y = 0
    for param in clrcleParamList:
        y += 50 
        fill(param["r"],param["g"],param["b"])
        circle(param["x"],y,30)
```
-----------------------------------------------------------
5. Показываем содержимое листа(списка) в виде графика
```
def setup():
  textSize(18) 
  fill(0)
  strokeWeight(16)
  strokeCap(SQUARE)
  size(640, 360)
  noLoop()

def draw(): 
  background(0,255,0,16)
  myList = [3, -9, 8, 54, -1, 2]
  y = 100
  
  for value in myList: 
     if value < 0:
         value = value * -1
         
     text(value, 35, y + 6)    
     line(70, y, value*10 + 70, y)
     y =  y + 30 
```
**************************************************************************************************************************************************
                                                    Lesson 7
													Images
**************************************************************************************************************************************************
----------------------------------------------------
1. Показываем имидж
```
bonusImage 

def setup(): 
  global bonusImage
  size(640, 360)
  bonusImage = loadImage("catRight.gif")  

def draw():
   background(255)
   image(bonusImage, 50, 150) 
```
----------------------------------------------------
2. - Котенок, который машет лапой
- Сохраняем несколько имиджей в лист
-  Меняем вызов имиджа (не на каждом вызове метода draw, а только на каждом трицатом)
```
i = 0 

def setup():  
  global catImageList 
  size(640, 360)
  
  catImageList = []
  catRight = loadImage("catRight.gif") 
  catUp = loadImage("catUp.gif") 
  
  catImageList.append(catRight)
  catImageList.append(catUp)  

def draw():
   global i
   background(255) 
   image(catImageList[i], 50, 150) 
   if (frameCount%30==0 and i == (len(catImageList) - 1)): 
      i = 0
   elif(frameCount%30==0): 
      i = i + 1 
```
-------------------------------------------------------
3. #TODO: если сталкивается с пеньком, уменьшаем очки на 1
   #TODO: добавить бонус мешочки, до которых можно допрыгнуть
   #TODO: если очки будут равны нулю, то Gave Over 
```
i = 0 
x = -20
y = 350
jump = False
score = 10

def setup():  
  global runningGirlList 
  size(1140, 660) 
  
  runningGirlList = []
  runningGirl1 = loadImage("runningGirl1.gif") 
  runningGirl2 = loadImage("runningGirl2.gif") 
  runningGirl3 = loadImage("runningGirl3.gif") 
  runningGirl4 = loadImage("runningGirl4.gif") 
  runningGirl5 = loadImage("runningGirl5.gif") 
  runningGirl6 = loadImage("runningGirl6.gif") 
  runningGirl7 = loadImage("runningGirl7.gif") 
  runningGirl8 = loadImage("runningGirl8.gif") 
  runningGirl9 = loadImage("runningGirl9.gif")
  runningGirl10 = loadImage("runningGirl10.gif") 
  runningGirl11 = loadImage("runningGirl11.gif") 
  runningGirl12 = loadImage("runningGirl12.gif")   
  
  runningGirlList.append(runningGirl1)
  runningGirlList.append(runningGirl2)
  runningGirlList.append(runningGirl3)
  runningGirlList.append(runningGirl4)
  runningGirlList.append(runningGirl5)
  runningGirlList.append(runningGirl6)
  runningGirlList.append(runningGirl7)
  runningGirlList.append(runningGirl8)
  runningGirlList.append(runningGirl9) 
  runningGirlList.append(runningGirl10) 
  runningGirlList.append(runningGirl11) 
  runningGirlList.append(runningGirl12) 
  
def keyPressed():
  global y 
  global jump
  global beforeJumpY
  if (key == CODED):  
    if (keyCode == UP):
      beforeJumpY = y 
      jump = True
      y = y - 100   

def draw():
   global i
   global x
   global y
   global score 
   background(155) 
   image(runningGirlList[i], x, y) 
   rect(250, 475, 20, 20 )
   rect(750, 475, 20, 20 ) 
     
   fill(0)
   textSize(22) 
   formatedText = "Your score: %s" % score
   text(formatedText, 10, 50);
   
   #TODO: если сталкивается с пеньком, уменьшаем очки на 1
   #TODO: добавить бонус мешочки, до которых можно допрыгнуть
   #TODO: если очки будут равны нулю, то Gave Over 
   
   if(frameCount%10==0):
      x = x + 10
      #после прыжка возвращаемся на свой уровень по y
      if(jump and y < beforeJumpY):
          i = 4
          y = y + 5
          
      #если добежал до правого края, возвращаем в начало    
      elif x > width - 100:
          x = 0
          
      #если доходим до последнего имиджа в листе runningGirlList, то начинаем с первого имиджа     
      elif (i == (len(runningGirlList) - 1)): 
          i = 0 
      else: 
          i = i + 1   
``` 
----------------------------------------------------
4. - Слайдер
- Определяем расстояние от положения курсора до линии слайдера:
- d = dist(mouseX, mouseY, x, height/2)
- первые два параметра это x,y положения курсора
- x - положение (x) кнопки слайдера
- height/2 - положение (y) слайдера по горизонтали

- соотносим ширину слайдера со шкалой от 0 до 100:
- map(mouseX, 50, width-50, 0, 100)
- первый параметр - это x положение курсора
- 2ой и 3ый параметра это реальное положение в пикселях начала и конца слайдера
- мы соотрносим начало слайдера значению 0, а конец слайдера значению 100
- это 4ый и 5ый параметры 

```
x = 50
score = 0 

def setup():
  textSize(50)
  textAlign(CENTER)
  fill(255)
  strokeWeight(16)
  size(640, 360)


def draw():
  global x
  global score
  background(0,255,0,16)
  line(50, height/2, width-50, height/2)
  
  ellipse(x, height/2, width/10, width/10)
  
  
  d = dist(mouseX, mouseY, x, height/2)
  
  if(d < 100 and mouseX > 50 and mouseX < width - 50):
    x = mouseX;
    score =  round(map(mouseX, 50, width-50, 0, 100)) 
    scoreText = "number: %s" % score
   
    text(scoreText, width/2, height/8)
``` 
***********************************************************************************************************************
                                      Lesson 8
***********************************************************************************************************************
 






   
   
   
   


     


 

 
 








