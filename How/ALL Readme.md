Forum Processsing Python
https://discourse.processing.org/
*****************************************************************************************************************
                                                 Коллизии
*****************************************************************************************************************
1. CircleCircle

```
def collideCircleCircle(x, y,d, x2, y2, d2):
#2d
# dist()  — функция вычисления расстояния между двумя точками
  if dist(x,y,x2,y2) <= (d/2)+(d2/2):
    return True
  else:
    return False


def setup():
    size(600, 400)
    
def draw():
    background(100)
    if collideCircleCircle(300, 200, 50, mouseX, mouseY, 100):
        fill(255, 0, 0)
    else:
        fill(255)
    ellipse(300, 200, 50, 50)
    ellipse(mouseX, mouseY, 100, 100)
```
---------------------------------------------------------------
2. LineCircle 

```
def collideLineCircle( x1,  y1,  x2,  y2,  cx,  cy,  diameter):
  # is either end INSIDE the circle?
  # if so, return true immediately
  
    def collidePointCircle(x, y, cx, cy, d):
        #2d
        if dist(x,y,cx,cy) <= d/2:
            return True
        else:
            return False
        
    def collidePointLine(px,py,x1,y1,x2,y2, buffer):
        # get distance from the point to the two ends of the line
        d1 = dist(px,py, x1,y1);
        d2 = dist(px,py, x2,y2);
    
        #get the length of the line
        lineLen = dist(x1,y1, x2,y2);
    
        # since floats are so minutely accurate, add a little buffer zone that will give collision
        if buffer == None:
            buffer = 0.1   # higher # = less accurate
    
        #if the two distances are equal to the line's length, the point is on the line!
        # note we use the buffer here to give a range, rather than one #
        if d1+d2 >= lineLen-buffer and d1+d2 <= lineLen+buffer:
            return True
        else:
            return False

        
    inside1 = collidePointCircle(x1,y1, cx,cy,diameter)
    inside2 = collidePointCircle(x2,y2, cx,cy,diameter)
    if inside1 or inside2:
        return True
    
    # get lengthgth of the line
    distX = x1 - x2
    distY = y1 - y2
    length = sqrt( (distX*distX) + (distY*distY) );
    
    # get dot product of the line and circle
    dot = ( ((cx-x1)*(x2-x1)) + ((cy-y1)*(y2-y1)) ) / pow(length,2)
    
    # find the closest point on the line
    closestX = x1 + (dot * (x2-x1))
    closestY = y1 + (dot * (y2-y1))
    
    # is this point actually on the line segment?
    # if so keep going, but if not, return false
    onSegment = collidePointLine(closestX,closestY,x1,y1,x2,y2,0.1);
    if not onSegment:
        return False
    
    # draw a debug circle at the closest point on the line
    #if _collideDebug:
        #ellipse(closestX, closestY,10,10)
    
    
    # get distance to closest point
    distX = closestX - cx
    distY = closestY - cy
    distance = this.sqrt( (distX*distX) + (distY*distY) )
    
    if distance <= diameter/2:
        return True
    else:
        return False




def setup():
    size(600, 400)
    
def draw():
    background(100)
    if collideLineCircle(300, 200, 50, 50,  mouseX, mouseY, 100):
        fill(255, 0, 0)
    else:
        fill(255)
    line(300, 200, 50, 50)
    ellipse(mouseX, mouseY, 100, 100)
```
-------------------------------------------------------
3. RectCircle
```
def collideRectCircle(rx, ry, rw, rh, cx, cy, diameter):
  #2d
  # временные переменные для установки краёв для тестирования
  # rectmode — CORNER, ellipseMode — CENTER, то есть оба по-умолчанию
  testX = cx
  testY = cy

  # which edge is closest?
  if cx < rx:
    testX = rx       # Левый край
  elif cx > rx+rw:
    testX = rx+rw     # правый край

  if cy < ry:
    testY = ry       # верхний край
  elif cy > ry+rh:
    testY = ry+rh   # нижний край

  # получить расстояние от ближайших краев с помощью processing функции dist()
  distance = dist(cx,cy,testX,testY) 

  # если расстояние меньше радиуса, столкновение!
  if distance <= diameter/2:
    return True
  else:
    return False


def setup():
    size(600, 400)
    
def draw():
    background(100)
    if collideRectCircle(300,200, 100, 50, mouseX, mouseY, 100):
        fill(255,0,0)
    else:
        fill(255)
    rect(300,200, 100, 50)
    ellipse(mouseX, mouseY, 100, 100)
```
----------------------------------------------------    
4. Функция-детектор соприкосновения прямоугольника и прямоугольника

```
def collideRectRect (x, y, w, h, x2, y2, w2, h2):
  # работает правильно, даже если rectMode стоит CENTER
    if (x + w >= x2) and  (x <= x2 + w2) and  (y + h >= y2) and (y <= y2 + h2):
        return True
    else:
        return False

def setup():
    size(600, 400)
    
def draw():
    background(100)
    rectMode(CENTER)
    if collideRectRect(300,200, 100, 50, mouseX, mouseY, 100, 50):
        fill(255,0,0)
    else:
        fill(255)
    rect(300,200, 100, 50)
    rect(mouseX, mouseY, 100, 50)
```	
---------------------------------------------------------
5. PointCircle
```
def collidePointCircle(x, y, cx, cy, d):
    if dist(x,y,cx,cy) <= d/2:
        return True
    else:
        return False

def setup():
    size(600, 400)
    
def draw():
    background(100)
    if collidePointCircle(mouseX, mouseY, 300, 200, 70):
        fill(255, 0, 0)
    else:
        fill(255)
    ellipse(300, 200, 70, 70)
    strokeWeight(10)
    point(mouseX, mouseY)
    strokeWeight(1)
```	
----------------------------------------------------------
6. PointRect
```
def collidePointRect(pointX, pointY, x, y, xW, yW):
#если точка находится между краёв прямоугольника:
    if (pointX >= x) and (pointX <= x + xW) and (pointY >= y) and (pointY <= y + yW): 
        return True
    return False

def setup():
    size(600, 400)
    
def draw():
    background(100)
    strokeWeight(10)
    if collidePointRect(mouseX, mouseY, 200, 300, 60, 70):
        fill(255, 0, 0)
    else:
        fill(255)
    point(mouseX, mouseY)
    rect(200, 300, 60, 70)
```	
----------------------------------------------------
7. нажимаем на кнопки - показываем или прячем кружок

```  
showCircle = False
def collidePointRect(pointX, pointY, x, y, xW, yW):
#если точка находится между краёв прямоугольника:
    if (pointX >= x) and (pointX <= x + xW) and (pointY >= y) and (pointY <= y + yW): 
        return True
    return False 

def setup():
    size(600, 400)
    
def draw():
    global showCircle
    background(100) 
    if collidePointRect(mouseX, mouseY, 200, 330, 150, 30) and mousePressed:
        showCircle = True
    if collidePointRect(mouseX, mouseY, 400, 330, 150, 30) and mousePressed:
        showCircle = False  
    
    fill(132, 211, 183)  
    rect(200, 330, 150, 30, 7)
    fill(0)
    textSize(16)  
    text(u'Показать кружок',205, 350 )
    
    fill(247,112,128)  
    rect(400, 330, 150, 30, 7)
    fill(0)
    text(u'Спрятать кружок',405, 350) 
    
    if showCircle:
        circle(20, 20, 20)  
```		
*****************************************************************************************************************
                                                Lesson 1
*****************************************************************************************************************
![alt text](https://github.com/Elenn/processing_lessons/blob/main/How/01_Lesson_Circle.png?raw=true)
--------------------------------------------- 
0. Задание: 
Нарисуй снеговика
---------------------------------------- 
1. Даунлодим processing-3.5.4
 
- Если переходите с processing-4.3
на processing-3.5.4
 
https://processing.org/releases
-> Version 3.5.4 
-> Windows 64-bit

- распакуйте zip processing-3.5.4-windows64.zip

- удалите Python Mode for Processing 4 - папку 
C:\Users\<userName>\Documents\Processing

- Java -> Add Models  
-> Python Mode for Processing 3 -> Install 
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
- Так для круга ellipse()
первый параметр x-coordinate (координата x)
второй параметр y-coordinate (координата y)
третий параметр width and height (ширина и длинна)

![alt text](https://github.com/Elenn/processing_python/blob/main/01_Lesson/How/references.png?raw=true)
![alt text](https://github.com/Elenn/processing_python/blob/main/01_Lesson/How/circleReference.png?raw=true)  
**************************************************************************************************************
                                               Lesson 2
                                               Функции
                                               Вызов функции
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
------------------------------------------------------
4. Самолетик. Метод с параметрами.

```
def setup():
    size(600,600)
    
def airplane(x):
     fill(39, 82, 113)
     noStroke()
     ellipse(x,150,155,25) 
     quad(-90+x, 130, -80+x, 125, -30+x, 150, -65+x, 150)  
     quad(-10+x, 110, x, 100, 50+x, 140, 15+x, 140) 
     quad(-10+x, 190, x, 200, 50+x, 160, 15+x, 160)     
   
def draw():
    airplane(0)
    airplane(200)
```
------------------------------------------------------
5. Кораблик. Метод с параметрами.

``` 
def setup():
    size(600, 600)
    
def ship(x):    
    fill(122, 89, 255)
    rect(25+x,38,10,30)
    rect(20+x,40,6,20)
    quad(x, 50, 55+x, 50, 40+x, 75, 15+x, 75)
    
def draw():
    ship(0) 
    ship(200) 
```
--------------------------------------------------
6. Кролик. Метод с параметрами.
```
def setup():
    size(600,600)
    
def rabbit(x):
    ellipse(-5+x, 50, 10, 40) 
    ellipse(5+x, 50, 10, 40)
    ellipse(x, 70, 30, 30) 
    
def draw():
    background(147)  
    rabbit(20)
``` 
--------------------------------------------------
7. boxten. Метод с параметрами.

```
def setup():
    size(600, 600)
    
def boxten(x): 
    strokeWeight(2)
    stroke(0)
    fill(128,0,128)
    ellipse(60+x,160,25,25)

    fill(128,0,128)
    strokeWeight(3)
    stroke(100,0,100)
    rect(x,90,100,100)
    stroke(148,0,148)
    rect(6+x,96,88,88)

    strokeWeight(2)
    stroke(0)
    fill(128,0,128)
    ellipse(60+x,160,25,25)

    fill(255)
    strokeWeight(2)
    stroke(0)
    ellipse(26+x,136,38,38)
    ellipse(75+x,137,38,38)

    fill(0)
    ellipse(26+x,136,25,25)
    ellipse(75+x,137,25,25)

    strokeWeight(3)
    stroke(148,0,148)
    line(6+x,96,15+x,105)
    line(94+x,96,85+x,105)
    line(6+x,185,15+x,175)
    line(94+x,184,85+x,175)
    
def draw():
    boxten(0) 
    boxten(200) 
```
------------------------------------------
8. Машинка. Метод с параметрами. 
```
def setup():
    size(600, 600)
    
def car(x,y):  
    fill(155)
    circle(x, 38+y, 18) 
    circle(52+x, 38+y, 18)
    circle(x, 130+y, 18)
    circle(52+x, 130+y, 18)
    fill(155, 166, 255)
    rect(-2+x, 20+y, 55, 135, 6, 6, 18, 18)
    fill(155) 
    rect(3+x, 115+y, 45, 30, 6, 6, 18, 18)
    
def draw():
    car(0, 50) 
    car(120, 420)
``` 
***********************************************************************************************************************
                                                       Lesson 3
                                                     - Движение шарика
													 - Переменные 
													 - Глобальные переменные
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
4. Двигаем шарик по X, 
   когда шарик доходит до правого края, он появляется на позиции -25
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
     
    fill(255,146,142) 
    ellipse(x, 100, 50, 50)
  
    if x == 640:
       x = -25
```	
---------------------------------------------------------------------
5. Двигаем шарик по Y
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
6. Двигаем круг в двух направлениях x и y
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
7. Двигается шарик туда обратно по X
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
8. Двигается шарик туда обратно по Y
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
9. Двигается шарик туда обратно по X и Y
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
10. Имидж. 
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
11. Имидж движется вверх и когда достигает верха, то останавливается

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
12. Имидж движется вверх и когда достигает верха, то идет вниз

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
13. Имидж движется вверх и когда достигает верха, то идет вниз,
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
14. Меняем направление движения шарика, когда он сталкивается с краями

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
15. Добавили прямоугольник внизу, 
пожалуйста выполните 

Задание: Создай/модифицируй програмку, что бы шарик отскакивал от прямоугольника внизу,
а не от нижнего края.		
*********************************************************************************************************************
                                                    Lesson 4
                                                  - mousePressed()
                                                  - keyPressed()
                                                  - переменные
                                                  - глобальные переменные												  
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
- При нажатии на мышку, шарик исчезает, 
- при нажатии второй раз шарик появляется

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
- При нажатии на стрелочку '->' шарик перемещается вправо

```
x = 50
def setup():
    size(600, 600)
    
def keyPressed():
    global x 
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
- При нажатии на букву 'z' шарик перемещается вправо

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
                                                       - range(0, 64) 
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
2. Рисуем вертикальные линии 

```
boxSize = 10
def setup(): 
    size(640, 320)  
     
def draw():  
    for i in range(0, 64):
      line(i*10, 0, i*10, height)
```    
----------------------------
3. Рисуем вертикальные линии 

```
boxSize = 20
def setup(): 
    size(640, 320)  
     
def draw():  
    for i in range(0, width/boxSize):
      line(i*boxSize, 0, i*boxSize, height)
``` 
----------------------------
4. Рисуем горизонтальные линии 

```
boxSize = 20
def setup(): 
    size(640, 320)  
     
def draw():  
	for i in range(0, height/boxSize):
      line(0, i*boxSize, width, i*boxSize, )
``` 
----------------------------
5. Рисуем вертикальные и горизонтальные линии 

```
boxSize = 20
def setup(): 
    size(640, 320)  
     
def draw():  
    for i in range(0, width/boxSize):
      line(i*boxSize, 0, i*boxSize, height)
	  
	for i in range(0, height/boxSize):
      line(0, i*boxSize, width, i*boxSize, )
``` 
-----------------------------
6. - for loop, range, increment by 10 (шаг 10)
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
-------------------------------------------------------------	
7. - Вложенные циклы: Nested for loops;
- for loop, range, increment by 10 (шаг 10)
- вызываем исполнения кода внутри for 
каждый раз от 0 до 639 с шагом 10
-(то есть x принимает последовательно значения 0, 10, 20, 30 . . .630)


```
def setup():
   size(640, 360) 
 
def draw():
   background(0);
   fill(255) 
   
   for y in range(0, 360, 10):
       for x in range(0, 640, 10): 
           circle(x, y, 10)
```	 
-------------------------------------
8. - Вложенные циклы: Nested for loops;
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
   
   for y in range(0, 360/circleWidth + 1): 
       for x in range(0, 640/circleWidth): 
           circle(x*circleWidth, y*circleWidth, circleWidth)
```
-------------------------------------------
9. - Вложенные циклы: Nested for loops;
- шахматная доска 

```
def setup():
   size(600, 600)
   noLoop()   
 
def draw():
   background(0);
   fill(255)
   rectWidth = 60 
   
   ellipseMode(CORNER)  
   
   for y in range(0, 8): 
       for x in range(0, 8):
           fill(255)
           if( x%2==0 and y%2!=0) or (x%2!=0 and y%2==0):
               fill(146) 
           rect(x*rectWidth, y*rectWidth, rectWidth, rectWidth) 
```	
--------------------------------------------------
10.  шахматная доска (без вложенных циклов)

```
x = 0 
def setup():
    size(640, 640)  
    
def draw(): 
    global x
    
    for y in range(0, 9):
        noFill()
        if (y%2==0 and x%160!=0) or (y%2!=0 and x%160==0):
            fill(146) 
        rect(x, y*80, 80, 80)
    x += 80
```	   
************************************************************************************************************************
                                                    Lesson 6
                                                    - List
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
1. Рисуем несколько кругов в ряд с позицией из List
clrcleX[0]
clrcleX[1]
clrcleX[2]

```
clrcleX = [30, 150, 480]
def setup(): 
    size(640, 320)  
    
def draw():  
  fill(255,0,0)
  circle(clrcleX[0],150,50) 
  circle(clrcleX[1],150,50)
  circle(clrcleX[2],150,50)
``` 
---------------------------------------------------
2. Рисуем несколько кругов в ряд с позицией x из List
цикл for
for x in clrcleX

```
clrcleX = [30, 150, 480]
def setup(): 
    size(640, 320)  
    
def draw(): 
    for x in clrcleX:
        fill(255,0,0)
        circle(x,150,50)
```		
---------------------------------------------------------- 
3. Рисуем несколько кругов в случайном месте канвы по x из List
```
clrcleXList = [random(20, 630), random(20, 630),random(20, 630), random(20, 630), random(20, 630)]
def setup(): 
    size(640, 320)  
    
def draw(): 
    for x in clrcleXList: 
        fill(255,0,0)
        circle(x,150,30)
```	
---------------------------------------------------------- 
4. List append
- Добавляем круг по нажатию мышки.
```
clrcleX = [30, 150, 480]
def setup():
    size(600, 600)
    
def mouseClicked():
    global clrcleX 
    clrcleX.append(random(20, 580))    
    
def draw(): 
    for x in clrcleX: 
        fill(255,0,0)
        circle(x,150,30)
```	
-------------------------------------------------------------	
5. List append
- Рисуем несколько кругов в случайном месте канвы по x из List
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
        fill(255,0,0)
        circle(x,150,30)
```	
------------------------------------------------------------------
6. List remove 
   len
- Удаляем круги при нажатии на мышку.

```
clrcleX = [30, 150, 480]
def setup():
    size(600, 600)
    
def mouseClicked():
    global clrcleX
    if(len(clrcleX) > 0): 
        clrcleX.remove(clrcleX[0])
        print(clrcleX)    
    
def draw():
    background(155) 
    for x in clrcleX: 
        fill(255,0,0)
        circle(x,150,30)
``` 
-----------------------------------------------------------
7. Бесконечное движение шариков
```
circleList = [[100], [320]]
def setup():
    size(600,600)
    
def draw():
    background(147)
    global circleList
	
    for x in circleList:
        circle(x[0], 150, 50)
        x[0] = x[0] + 1
        if x[0] == 650:
            x[0] = -50
``` 
-----------------------------------------------------------
8. Бесконечное движение корабликов
```
circleList = [[100], [320]]
def setup():
    size(600,600)
    
def ship(x):    
    fill(122, 89, 255)
    rect(25+x,38,10,30)
    rect(20+x,40,6,20)
    quad(x, 50, 55+x, 50, 40+x, 75, 15+x, 75)   
    
def draw():
    background(147)
    global circleList
  
    for x in circleList:
        ship(x[0])
        x[0] = x[0] + 1
        if x[0] == 650:
            x[0] = -50 
```
------------------------------------------------------------
9. translate. Бесконечное движение Больших корабликов
```
circleList = [[100], [320]]
def setup():
    size(600,600, P3D)
    
def ship(x): 
    pushMatrix()   
    fill(122, 89, 255)
    translate(150, 150, 250) 
    rect(25+x,38,10,30)
    rect(20+x,40,6,20)
    quad(x, 50, 55+x, 50, 40+x, 75, 15+x, 75)   
    popMatrix()
    
def draw():
    background(147)
    global circleList
  
    for x in circleList:
        ship(x[0])
        x[0] = x[0] + 1
        if x[0] == 650:
            x[0] = -50 
```          
-----------------------------------------------------------
10. Показываем содержимое листа(списка) в виде графика
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
--------------------------------------------------
11. Простейшая стрелялка. Нажимаем на клавишу пробел.
```
bullets = [[550],[530],[500],[280]]
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
        
``` 
---------------------------------------------------
12. Простейшая стрелялка. Нажимаем на клавишу пробел.
Только 5 пулек в наличии.

```
bullets = [[550],[530],[500],[280]]
gunX = 280
gunY = 570
bullet_speed = 5

def setup():
    size(600,600)
    
def keyPressed():
    global bullets 
    if key == ' ' and len(bullets) < 5 : 
        bullets.append([gunY - 10]) 
    
def gun():
    fill(255, 154, 165)
    rect(gunX, gunY, 60, 20) 
    
def draw():
    background(146) 
    gun()  
        
    for bullet in bullets:  
        if bullet[0] < 0:
           bullets.remove(bullet)
        else:
             bullet[0] = bullet[0] - bullet_speed    
        fill(255, 154, 165) 
        circle(gunX + 30, bullet[0], 20)
```
*********************************************************************************************************************************
                                                    Lesson 7
                                                    dist
													коллизии
*********************************************************************************************************************************
1. Исчезают шарик при нажатии на него.
```
showCircle = True
circleX  =  150
circleY  = 150

def setup():
  size(400, 500)   
  
def draw(): 
  background(200)  
  global showCircle
  
  if mousePressed and dist(mouseX, mouseY, circleX, circleY) < 20:
    showCircle = False

  if showCircle:        
    fill(0,255,0)    
    ellipse(circleX, circleY, 20, 20)
```
-------------------------------------------------
1.1. Исчезают снеговик при нажатии на него.
```
showCircle = True
circleX  =  150
circleY  = 150

def setup():
  size(400, 500) 
  
def snowman():
    circle(100, 255, 30) 
    circle(100, 300, 60)     
  
def draw(): 
  background(200)  
  global showCircle 
  
  if mousePressed and dist(mouseX, mouseY, 100, 280) < 80:
    showCircle = False

  if showCircle:        
    fill(0,255,0)    
    snowman()
```
-------------------------------------------------
2. Исчезают шарик при нажатии на кнопку Hide,
показываем шарик при нажатии на кнопку Show

```
circleX  = 150
circleY  = 150
showCircle = True

def setup():
  size(400, 500)   
  
def draw(): 
  background(200)  
  global showCircle
  
  if mousePressed and dist(mouseX, mouseY, 30, 16) < 20:
    showCircle = True
  if mousePressed and dist(mouseX, mouseY, 100, 16) < 20:
    showCircle = False

  if showCircle:        
    fill(0,255,0)    
    ellipse(circleX, circleY, 20, 20)
  
  fill(0,255,0) 
  ellipse(30, 16, 50, 25)
  fill(255, 65, 100)
  ellipse(100, 16, 50, 25)
  
  fill(10) 
  textSize(16)  
  text(u'Show', 10, 20) 
  text(u'Hide', 83, 20)
```  
-------------------------------------------------	
3. Исчезают шарики при нажатии на них.

```
coinList = [[20, 85], [380, 77], [175, 200], [350, 20], [44, 450]]  

def setup():
  size(400, 500)   
  
def draw(): 
  background(200) 
  fill(0,255,0)
  
  for item in coinList:   
    if mousePressed and dist(mouseX, mouseY, item[0], item[1]) < 20:
        coinList.remove(item) 
        
    ellipse(item[0], item[1], 20, 20)
```	
-------------------------------------------------------------------	
4. Исчезают шарики при нажатии на них. Показываем счет.

```
coinList = [[20, 85], [380, 77], [175, 200], [350, 20], [44, 450]]  
collected = 0

def setup():
  size(400, 500)   
  
def draw(): 
  background(200)
  global collected
  
  textSize(20) 
  fill(0) 
  text(collected,370,40)    
  
  for item in coinList:   
    if mousePressed and dist(mouseX, mouseY, item[0], item[1]) < 20:
        coinList.remove(item)
        collected +=1 
        
    fill(0,255,0)    
    ellipse(item[0], item[1], 20, 20)     
```	
-------------------------------------------------------------
5. - Исчезают шарики при нажатии на них. 
- Показываем счет. 
- Добавляем шарики при нажатии на кнопку '+'

```	
coinList = [[20, 85], [380, 77], [175, 200], [350, 120], [44, 450]]  
collected = 0
def setup():
    size(400, 500) 
    
def addRandomCircles():
    global coinList  
    innerList = [random(0, width), random(10,height-20)] 
    coinList.append(innerList)        

def mouseClicked():
    if dist(mouseX, mouseY, 65, 25) < 40: 
        addRandomCircles()    
            
def draw(): 
    background(200)
    global collected
    
    textSize(20) 
    fill(0) 
    text(collected,370,40)   
     
    noFill() 
    rect(10, 10, 30, 30) 
    textSize(20)  
    text('+',16,30)   
    
    for item in coinList:   
        if mousePressed and dist(mouseX, mouseY, item[0], item[1]) < 20:
            coinList.remove(item)
            collected +=1 
    
        fill(0,255,0)    
        ellipse(item[0], item[1], 20, 20)
    
```	
--------------------------------------------
6. Сбиваем движущиеся кружочки.
```
circleList = [[100], [320]]
bullets = []
gunX = 280
gunY = 570
bullet_speed = 5
def setup():
    size(600,600)
    
def gun():
    fill(255, 154, 165)
    rect(gunX, gunY, 60, 20)
        
def keyPressed():
    global bullets
    if key == ' ': 
        bullets.append([gunY - 10]) 
    
def draw():
    background(147)
    global circleList 
    gun()
    
    for bullet in bullets: 
        bullet[0] = bullet[0] - bullet_speed  
        circle(gunX + 30, bullet[0], 20) 
  
    for circleX in circleList:
        circle(circleX[0], 100, 50)
        circleX[0] = circleX[0] + 1
        if circleX[0] == 650:
            circleX[0] = -50
            
    for bullet in bullets:
        for circleX in circleList:
            if dist(gunX + 30, bullet[0], circleX[0], 100) < 20:
                bullets.remove(bullet)
                circleList.remove(circleX)
                 
```	
--------------------------------------------
7. Сбиваем движущиеся караблики.
```
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
    rect(25+x,38,10,30)
    rect(20+x,40,6,20)
    quad(x, 50, 55+x, 50, 40+x, 75, 15+x, 75)
    
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
            if dist(gunX, bullet[0], shipX[0]+20, 75) < 20:  
                bullets.remove(bullet)
                shipList.remove(shipX)
                
```
-------------------------------------------------
8. Сбиваем движущиеся караблики. Разный размер. svg.
```
shipList =  [[10, 100], [320, 200], [520, 300]]
 
bullets = []
gunX = 280
gunY = 570
bullet_speed = 5
def setup():
    global myShip
    size(600,600)
    myShip = loadShape("ship.svg")
    
def gun():
    fill(255, 154, 165)
    rectMode(CENTER)
    rect(gunX, gunY, 60, 20)
        
def keyPressed():
    global bullets
    if key == ' ': 
        bullets.append([gunY - 10])   
    
def draw():
    background(147)
    global circleList 
    gun()
    
    for bullet in bullets: 
        bullet[0] = bullet[0] - bullet_speed  
        circle(gunX, bullet[0], 20) 
  
    for shipX in shipList:
        shape(myShip, shipX[0], 10, shipX[1], 150) 
        shipX[0] = shipX[0] + 1
        if shipX[0] == 650:
            shipX[0] = -50
            
    for bullet in bullets:
        for shipX in shipList:
            if dist(gunX, bullet[0], shipX[0]+20, 75) < 20:  
                bullets.remove(bullet)
                shipList.remove(shipX)
```	
LenaPlay\sketch_10_image_svg\ship.svg
```
<svg width="100" height="100" xmlns="http://www.w3.org/2000/svg"> 
   <rect width="10" height="30" x="25" y="38" fill="blue" />
   <rect width="6" height="20" x="20" y="40" fill="blue" />
   <polygon points="0,50 55,50 40,75 15,75" style="fill:blue;stroke:blue;stroke-width:3" /> 
</svg>
```
			
--------------------------------------------------
9. Один ряд из лабиринта
```
#1 Стена
#0 Пол 
	   
tilemap = [1,0,0,0,1,0,0,1,0,1] 

cellWidth = 64
cellHeight = 64 

def setup():
    size(640,640)   

def renderMap():  
	for i in range(0, len(tilemap)):
		if tilemap[i] == 0:
			fill(80)
			rect(i*cellWidth, 0, cellWidth, cellHeight)				
		elif tilemap[i] == 1:
			fill(157, 219, 208)
			rect(i*cellWidth, 0, cellWidth, cellHeight)      
          
def draw():
    background(120)
    renderMap() 
``` 
--------------------------------------------------
10. Один ряд из лабиринта с сокровищами
```
#1 Стена
#0 Пол 
	   
tilemap = [1,0,2,0,1,0,0,1,0,1] 

cellWidth = 64
cellHeight = 64 

def setup():
    size(640,640)   

def renderMap():  
	for i in range(0, len(tilemap)):
		if tilemap[i] == 0:
			fill(180)
			rect(i*cellWidth, 0, cellWidth, cellHeight)				
		elif tilemap[i] == 1:
			fill(157, 219, 208)
			rect(i*cellWidth, 0, cellWidth, cellHeight) 
        elif tilemap[i] == 2:
			fill(180)
			rect(i*cellWidth, 0, cellWidth, cellHeight) 
			
            fill(255, 145, 145)
            ellipseMode(CORNER)
            ellipse(i*cellWidth+10, 10, cellWidth-20, cellWidth-20)  			
          
def draw():
    background(120)
    renderMap() 
``` 
----------------------------------------------------
10. Лабиринт

```
#1 Стена
#0 Пол 
	   
tilemap = [
   [1,1,1,1,1,1,1,1,1,1],
   [1,0,0,0,1,0,0,1,0,0],
   [1,1,1,0,1,0,0,0,0,1],
   [1,0,0,1,1,0,1,1,0,1],
   [1,1,0,1,1,0,1,1,1,1],
   [1,0,0,1,0,0,0,0,2,1],
   [1,0,0,1,1,1,1,0,0,1],
   [1,0,1,1,0,0,1,0,0,1],
   [1,0,0,0,0,1,1,1,0,1],
   [1,1,1,1,1,1,1,1,1,1] 
];

cellWidth = 64
cellHeight = 64 

def setup():
    size(640,640)   

def renderMap(): 
     
    for j in range(0, len(tilemap)):
        for i in range(0, len(tilemap[0])):
            if tilemap[j][i] == 0:
                fill(80)
                rect(i*cellWidth, j*cellHeight, cellWidth, cellHeight)
            elif tilemap[j][i] == 1:
                fill(157, 219, 208) 
          
def draw():
    background(120)
    renderMap()
``` 
---------------------------------------------------
11. Собираем сокровища в лабиринте
ChatGPT -> Пример кода для обработки коллизий. лабиринт собираем сокровища python processing

```
#1 Стена
#0 Пол
#2 Сокровище
 
tilemap = [
   [1,1,1,1,1,1,1,1,1,1],
   [1,0,0,0,1,0,0,1,0,0],
   [1,1,2,0,1,0,0,0,0,1],
   [1,0,0,1,1,0,1,1,0,1],
   [1,1,0,1,1,0,1,1,1,1],
   [1,0,0,2,0,0,0,0,2,1],
   [1,0,0,1,1,1,1,0,0,1],
   [1,0,1,1,0,0,1,0,0,1],
   [1,0,0,0,0,2,1,1,0,1],
   [1,1,1,1,1,1,1,1,1,1] 
];
cellWidth = 64
cellHeight = 64
circlePositionX = 1
circlePositionY = 1
score = 0  

def setup():
    size(640,640)   

def renderMap(): 
    global score
    for j in range(0, len(tilemap)):
        for i in range(0, len(tilemap[0])):
            if tilemap[j][i] == 0:
                fill(80)
                rect(i*cellWidth, j*cellHeight, cellWidth, cellHeight)
            elif tilemap[j][i] == 1:
                fill(157, 219, 208)
                rect(i*cellWidth, j*cellHeight, cellWidth, cellHeight)
            elif tilemap[j][i] == 2: 
                if  circlePositionX == i  and circlePositionY == j: 
                    tilemap[j][i] = 0 # забрали сокровище
                    score +=1 
                fill(80)
                rect(i*cellWidth, j*cellHeight, cellWidth, cellHeight)
                fill(255, 145, 145)
                ellipseMode(CORNER)
                ellipse(i*cellWidth+10, j*cellHeight+10, cellWidth-20, cellWidth-20)  
                   
def keyPressed(): 
    global circlePositionX   
    global circlePositionY 
     
    if (keyCode == LEFT ):
        if tilemap[circlePositionY][circlePositionX-1] != 1:
            circlePositionX -= 1 
    elif keyCode == UP:
        if tilemap[circlePositionY-1][circlePositionX] != 1:
            circlePositionY -= 1
    elif keyCode == RIGHT:
        if tilemap[circlePositionY][circlePositionX+1] != 1:
            circlePositionX += 1  
    elif keyCode == DOWN:
        if tilemap[circlePositionY+1][circlePositionX] != 1:
            circlePositionY += 1 
        
def drawPlayer():
    circleX = (circlePositionX + 1) * cellWidth - cellWidth/2
    circleY = (circlePositionY + 1) * cellHeight - cellHeight/2
    fill(255,0,255)
    ellipseMode(CENTER)
    circle(circleX,circleY,64) 
          
def draw():
    background(120)
    renderMap()
    drawPlayer()  
    textSize(50)
    text(score, 600, 50) 
``` 
---------------------------------------------------------------
12. Гонки. Да они ВСЕ по встречке едут!!!!!

```
carListY = [[-1100], [-890], [-500], [-350], [250]] 
carListY2 = [[-680], [300] ]
carListY3 = [[-300]]
carListY4 = [[-320], [-110], [480]]
carLength = 135
lineBetweenRoads = [-50,100,250,400,550,700,900]
dy = 0
myCarX = 350
myCarY = 500
def setup():
    size(600, 600) 
    
def blueCar(x,y):  
    fill(155)
    circle(2+x, 18+y, 18) 
    circle(54+x, 18+y, 18)
    circle(2+x, 110+y, 18)
    circle(54+x, 110+y, 18)
    fill(155, 166, 255)
    rect(x, y, 55, carLength, 6, 6, 18, 18)
    fill(155) 
    rect(5+x, 95+y, 45, 30, 6, 6, 18, 18)
    
def myCar(x,y):  
    fill(155)
    circle(2+x, 18+y, 18) 
    circle(47+x, 18+y, 18)
    circle(2+x, 100+y, 18)
    circle(47+x, 100+y, 18)
    fill(255, 166, 183)
    rect(x, y, 50, 120, 18, 18, 6, 6)
    fill(155) 
    rect(5+x, 10+y, 40, 28, 18, 18, 8, 8)

def road():
    fill(100) 
    rect(135,0,360,600) #дорога 
    
    for i in range(0,6):
       fill(255)
       noStroke()
       rect(width/2,lineBetweenRoads[i],20,100) #белая дорожная разметка
	   
def carMove(): 
    for y in carListY:
        blueCar(150, y[0])
        y[0] = y[0] + 1
        if y[0] == 1000:
            y[0] = -150 
        if dist(myCarX, myCarY, 150, y[0] + carLength) < 30:
            noLoop()
			
    for y in carListY2:
        blueCar(235, y[0])
        y[0] = y[0] + 1
        if y[0] == 1000:
            y[0] = -150 
        if dist(myCarX, myCarY, 235, y[0] + carLength) < 30:
            noLoop()
			
    for y in carListY3: 
        blueCar(335, y[0] + dy)
        y[0] = y[0] + 1
        if y[0] == 1000:
            y[0] = -150 
        if dist(myCarX, myCarY, 335, y[0] + carLength) < 30:
            noLoop() 
			
    for y in carListY4:
        blueCar(435, y[0] + dy)
        y[0] = y[0] + 1
        if y[0] == 1000:
            y[0] = -150 
        if dist(myCarX, myCarY, 435, y[0] + carLength) < 30:
            noLoop()  
        
def keyPressed():
    global myCarX
    if keyCode == RIGHT: 
       myCarX = myCarX + 5
    if keyCode == LEFT: 
       myCarX = myCarX - 5  
                                        
def draw():
    background(155)
    road()
    carMove()
    myCar(myCarX, myCarY)   
```
				
**************************************************************************************************************************************************
                                                    Lesson 8
                                                    - Dictionary
**************************************************************************************************************************************************
1. Dictionary
- positionXY["x"]
- positionXY["y"]
- Используем ключи Dictionary, что бы получить значения
 
```
positionXY = {"x": 100, "y": 100}
def setup():
    size(600,600)
    
def draw():
    circle(positionXY["x"],positionXY["y"],50)
```	
----------------------------------
2. List of Dictionary
- Рисуем несколько кругов в случайном месте канвы по x из List
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
**************************************************************************************************************************************************
                                                    Lesson 9
                                                    - Images
													- loadImage
													- svg
													- loadShape
**************************************************************************************************************************************************
----------------------------------------------------
1. Показываем имидж
``` 
def setup(): 
  global bonusImage
  size(640, 360)
  bonusImage = loadImage("catRight.png")  

def draw():
   background(255)
   image(bonusImage, 50, 150) 
```
----------------------------------------------------
2. - Котенок, который машет лапой
- Сохраняем несколько имиджей в лист
-  Меняем вызов имиджа (не на каждом вызове метода draw, а только на каждом трицатом)
-LenaPlay\sketch_10_sketch_Image
```
i = 0 
catImageList = []

def setup():  
  global catImageList 
  size(640, 360)  
  catRight = loadImage("catRight.png") 
  catUp = loadImage("catUp.png") 
  
  catImageList.append(catRight)
  catImageList.append(catUp)  

def draw():
   global i
   background(255) 
   
   image(catImageList[i], 50, 150) 
   
   if (i == 1 and frameCount%30==0): 
      i = 0
   elif(i == 0 and frameCount%30==0): 
      i = 1 
```
----------------------------------------------------
3. - Котенок, который машет лапой. Длинна листа. len(catImageList). 
- Сохраняем несколько имиджей в лист
-  Меняем вызов имиджа (не на каждом вызове метода draw, а только на каждом трицатом)
```
i = 0 
catImageList = []

def setup():  
  global catImageList 
  size(640, 360) 
  
  catRight = loadImage("catRight.png") 
  catUp = loadImage("catUp.png") 
  
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
--------------------------------------------------------
4. День рождения слона
- LenaPlay\sketch_10_image_elephant_birthday 
- https://scratch.mit.edu/projects/1103624373/

```
x = 130
y = 400
sc = 0
cakeX = 680
cakeY = 30
showCake = True
def setup(): 
  global savanna, elephantA, elephantB, cake
  size(640, 640)
  savanna = loadImage("Savanna.png") 
  elephantA = loadImage("elephant-a.png")
  elephantB = loadImage("elephant-b.png")
  cake = loadImage("cake-a.png")
  
def keyPressed():
    global x,y
    if keyCode == RIGHT: 
       x = x + 5 
    if keyCode == LEFT:
       x = x - 5        
    if keyCode == UP:
       y = y - 5               
    if keyCode == DOWN:   
       y = y + 5
	   
def draw(): 
    global cakeX, cakeY, showCake, sc, imageNumber 
    image(savanna, 0, 0, 640, 640)  
   
    sc = sc + 1 
    if sc == 1: 
        imageNumber = elephantA   
    if sc == 60: 
        imageNumber = elephantB  
    if sc == 80:
        sc = 0
        
    image(imageNumber, x, y, 200, 150)  
   
    if showCake: 
        image(cake, cakeX, cakeY, 200, 150)
      
    cakeX = cakeX - 1
    if cakeX == 0:
        cakeX = 680
   
    if cakeX == 680:
        cakeY = random(50, 600)
        showCake = True 
		
    if dist(x + 180, y, cakeX, cakeY) < 30:
        showCake = False   
```	
-------------------------------------------------------
5. svg  Кораблик
C:\web\AlicaPython\AlisaCreativica\LenaPlay\sketch_10_sketch_Image

```	
def setup(): 
    global myShip
    size(640, 360)
    myShip = loadShape("ship.svg")  

def draw():
    background(255)
    shape(myShip, 10, 10, 80, 80) #filename x y width height
```

LenaPlay\sketch_10_image_svg\ship.svg

<svg width="100" height="100" xmlns="http://www.w3.org/2000/svg"> 
   <rect width="10" height="30" x="25" y="38" fill="blue" />
   <rect width="6" height="20" x="20" y="40" fill="blue" />
   <polygon points="0,50 55,50 40,75 15,75" style="fill:blue;stroke:blue;stroke-width:3" /> 
</svg>
------------------------------------------------------
6. Движение корабликов
```	
circleList = [[10, 100], [320, 200], [520, 300]]
def setup():
    global myShip
    size(600,600)
    myShip = loadShape("ship.svg")
     
def draw():
    background(147)
    global circleList
  
    for x in circleList:
        shape(myShip, x[0], 10, x[1], 150)
        x[0] = x[0] + 1
        if x[0] == 650:
            x[0] = -50
```	  		
-------------------------------------------------------
7. Алиса. Показ для родителей
```
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
```
---------------------------------------------------------
7. #TODO: если сталкивается с пеньком, уменьшаем очки на 1
   #TODO: добавить бонус мешочки, до которых можно допрыгнуть
   #TODO: если очки будут равны нулю, то Game Over 
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
   
  if keyCode == UP:
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
***************************************************************************************************
                                            Lesson 10
                                          - Печатаем текст и он появляется на экране
***************************************************************************************************
1. Печатаем текст и он появляется на экране
```
myText = ''
def setup():
    size(600, 600)
    
def keyPressed():
    global myText
    myText += key
    
def snowman():
    fill(132, 255, 133)
    circle(100, 220, 20)
    circle(100, 250, 40)
    
def textWrap():
    fill(255)
    rect(130, 180, 150, 35, 12)                            
    
def draw():
    snowman() 
    textWrap()  
    fill(50) 
    text(myText, 135, 185, 140, 30)# Text wraps within text box 
```
***************************************************************************************************
                                             Lesson 11
                                        - Бесконечный ряд движущихся фигур											 
***************************************************************************************************
1. Для игры Стрелялка по Корабликам, рисуем ряд кораблей, используя 
- list

```
dx = 0
shipXList = [-590, -400, -320, -210, -88, 44, 200, 440, 590]
def setup():
    size(600, 600)
    
def ship(x):    
    fill(122, 89, 255)
    rect(25+x,38,10,30)
    rect(20+x,40,6,20)
    quad(x, 50, 55+x, 50, 40+x, 75, 15+x, 75)
    
def draw():
    background(155)
    global dx
    for x in shipXList:
       ship(x + dx)
    if dx == 600:
        dx = -50    
    dx = dx + 1 
``` 
------------------------------------------------
2. Бесконечное движение снеговиков

```
circleList = [[100], [320]]
def setup():
    size(600,600)
    
def snowman(x):
    circle(x, 105, 70) 
    circle(x, 200, 120)   
    
def draw():
    background(147) 
    global circleList
    for x in circleList:
        snowman(x[0]) 
        x[0] = x[0] + 1
        if x[0] == 650:
            x[0] = -50
``` 
*******************************************************************************************
                                          Lesson 12
                                          рисовалка										  
******************************************************************************************* 
1. рисовалка
```
def setup():
    background(205)
    size(600,600)
def draw():
    if mousePressed:
        line(mouseX,mouseY,pmouseX,pmouseY)
    if keyPressed:
        if key == 'w' or key == 'W':
            stroke(255)
        if key == 'e' or key == 'E':
            stroke(0,255,0)
        if key == 'r' or key == 'R':
            stroke(255,0,0)
        if key == 's' or key == 'S':
            stroke(0,0,255)
def mousePressed():
    if mouseButton == RIGHT:
        stroke(205)
    if mouseButton == LEFT:
        stroke(0)
```
*******************************************************************************************
                                          Lesson 13
*******************************************************************************************
----------------------------------------------------
1. - Слайдер
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
                                      Lesson 14
                                      Змейка
***********************************************************************************************************************
1. Змейка, на каждом шаге 
- Добавляем новый элемент в конец листа
- Убираем первый элемент.

``` 
x = [10,11,12]
y = [5,5,5]
appleX = 12
appleY = 10 
dx = 1 
dy = 0 
boxSize = 20  
gameover = False

def setup():
    size(600,600) 
    
def keyPressed():
    global dx, dy
    if keyCode == LEFT: 
       dx = -1
       dy = 0 
    elif keyCode == UP: 
       dx = 0
       dy = -1     
    elif keyCode == RIGHT: 
       dx = 1
       dy = 0    
    elif keyCode == DOWN: 
       dx = 0
       dy = 1  
    
def draw():
    background(255)
    global appleX, appleY, gameover 
    
    for i in range(0, width/boxSize):
      line(i*boxSize, 0, i*boxSize, height)
    
    for i in range(0, height/boxSize):
      line(0, i*boxSize, width, i*boxSize )
     
    for i in range(0, len(x)):  
        fill (0,255,0) 
        rect(x[i]*boxSize, y[i]*boxSize, boxSize, boxSize);
        
    fill(255,0,0);
    rect(appleX*boxSize, appleY*boxSize, boxSize, boxSize);  
   
    if not gameover:
        if(frameCount%18==0): 
            x.append(x[len(x)-1] + dx)
            y.append(y[len(y)-1] + dy)
            
            if x[len(x)-1] < 0 or x[len(x)-1] > width/boxSize or y[len(x)-1] < 0 or y[len(x)-1] > height/boxSize:
                gameover = True 
                        
            for i in range(0, len(x)-2): 
                if(x[len(x)-1] == x[i] and  y[len(y)-1] == y[i]):  #если коснется своего тела, то gameover
                   gameover = True 
            
            if x[len(x)-1]==appleX and y[len(x)-1]==appleY:
                appleX = int(random(0,width/boxSize))
                appleY = int(random(0,height/boxSize)) 
            else:    
                x.remove(x[0]) # удаляем хвост
                y.remove(y[0]) # удаляем хвост
    else:
        fill(0)
        textSize(30)
        text("GAME OVER", 20, height/2)    

```
------------------------------------------------------ 
2. #находим значение последнего элемента в listX

boxSize = 20
listX = [10,11,12]
listY = [5,5,5]	

def setup():
    size(600,600)

#находим значение последнего элемента в listX
print(listX)	
print(listX[0])	
print(listX[1])	
print(listX[2])  #последний элемент нащего листа

print(len(listX))#3 а нам надо на еденицу меньше, так как индекс листа начинается с нуля 
'''
listX[len(listX)] будет равен listX[3], а у нас нет этого элемента

и компютер будет ругаться: 
   IndexError: index out of range: 3 
   
так как последний элемет это listX[2]
то есть надо отнять еденицу
'''
print(len(listX) - 1) 

print(listX[2])
print(listX[len(listX) - 1])

-------------------------------------------------------
3.   это через занятие - не сегодня

надо добавить в конец листа listX элемен, со значением
на еденицу больще, чем последний элемен листа

надо добавить в конец листа listY элемен, со значением
таким же, как последний элемен листа

boxSize = 20
listX = [10,11,12]
listY = [5,5,5]	

def setup():
    size(600,600)

#находим значение последнего элемента в listX 
print(len(listX) - 1) 

print(listX[2])
print(listX[len(listX) - 1])

#надо добавить в конец листа элемен, со значением
#на еденицу больще, чем последний элемен листа

print(listX[len(listX) - 1] + 1)

listX.append(listX[len(listX)-1] + 1)
listY.append(listY[len(listY)-1] + 0)

print(listX)
print(listY)
-------------------------------------------------
4. 
#рисуем змейку

boxSize = 20
listX = [10,11,12]
listY = [5,5,5] 
 
def setup():
    size(600,600)  
    
def draw(): 
    background(255)
    
    for x in range(0,600,20):
        for y in range(0,600,20):
            rect(x,y,20,20) 
     
    #рисуем змейку 
    for i in range(0, len(listX)): 
        push() 
        fill (0,255,0) 
        rect(listX[i]*boxSize, listY[i]*boxSize, boxSize, boxSize)
        pop()  
-------------------------------------------------------
5. надо добавить в конец листа listX элемен, со значением
на еденицу больще, чем последний элемен листа

надо добавить в конец листа listY элемен, со значением
таким же, как последний элемен листа

boxSize = 20
listX = [10,11,12]
listY = [5,5,5]
dx = 1 
dy = 0

sc = 0
def setup():
    size(600,600)  
    
def draw(): 
    background(255)
    global sc
  
    for x in range(0,600,20):
        for y in range(0,600,20):
            fill (255)
            rect(x,y,20,20)
      
    sc = sc + 1 
    if sc == 18: 
         listX.append(listX[len(listX)-1] + dx)
         listY.append(listY[len(listY)-1] + dy)  
    if sc == 19:
        sc = 0  
     
    #рисуем змейку 
    for i in range(0, len(listX)):  
        fill (0,255,0) 
        rect(listX[i]*boxSize, listY[i]*boxSize, boxSize, boxSize)
-----------------------------------------------------
6. Сделали на занятии:
Добавляем в listX значение на еденицу больше, чем значение последнего элемента листа (7+1)
Добавляем в listY то же значение, что и значение последнего элемента листа (20)

```
listX = [5,6,7]
listY = [20,20,20]
sc = 0

def setup():
    size(600,600)
    
def draw():
    global sc, listX, listY
    for x in range(0,600,20):
        for y in range(0,600,20):
		    fill(250)
            rect(x,y,20,20)
    
    sc = sc + 1
    if sc == 18:
        listX.append(listX[len(listX)-1]+1)
        listY.append(listY[len(listY)-1]+0) 
    if sc == 19:
       sc = 0 
       
    for z in range(0,len(listX)): 
        fill(0,250,0)
        rect(listX[z]*20,listY[z]*20,20,20)
```		
-----------------------------------------------------
7. # удаляем хвост

boxSize = 20
x = [10,11,12]
y = [5,5,5]
dx = 1 
dy = 0

sc = 0
def setup():
    size(600,600)  
    
def draw(): 
    background(255)
    global sc
    for i in range(0, 600, boxSize):
      line(i, 0, i, 600)
    
    for i in range(0, 600, boxSize):
      line(0, i, 600, i)
      
    sc = sc + 1 
    if sc == 18: 
         x.append(x[len(x)-1] + dx)
         y.append(y[len(y)-1] + dy)
         
         x.remove(x[0]) # удаляем хвост
         y.remove(y[0]) # удаляем хвост  
    if sc == 19:
        sc = 0  
     
    #рисуем змейку 
    for i in range(0, len(x)):  
        fill (0,255,0) 
        rect(x[i]*boxSize, y[i]*boxSize, boxSize, boxSize);
----------------------------------------------------------------		
8. Таймер:
метод timer меняет значение глобальной переменной timerValue
что бы добавить timer() в свой проект, надо добавить глобальную переменную timerValue
и вызвать timer() в методе draw()

``` 
timerValue = 250
def setup():
    size(600,600)
    
def timer(): 
    global timerValue
    
    fill(0)
    textSize(20)
    text(timerValue, 20, 40) 
    
    if frameCount%60==0 and timerValue != 0: 
        timerValue = timerValue - 1  
    
def draw():
    background(146)
    timer()
    
    if timerValue < 240 and timerValue > 200:
        ellipse(80, 80, 30, 30)
```
-------------------------------------------
*********************************************************************************************************************************
                                                     знакомство с for
                                                     snejinka Снежинка
*********************************************************************************************************************************
1. snejinka Снежинка

```
xAll = 300
myColor = 0
def setup():
    size(600, 600)
    colorMode(HSB, 360, 100, 100)
  
def draw():
    global xAll, myColor
    background(100)
    fill(myColor, 100, 100)
    translate(xAll, 0) 
    for x in 0, 200, 400:
        ellipse(x, 100, 50, 50)
        
    for x in 100, 200, 300:
        ellipse(x, 200, 50, 50)
        
    for x in 0, 100, 200, 300, 400:
        ellipse(x, 300, 50, 50)
            
    for x in 100, 200, 300:
        ellipse(x, 400, 50, 50) 
        
    for x in 0, 200, 400:
        ellipse(x, 500, 50, 50)
    
    xAll -= 1
    myColor += 1
    if xAll == -550:
        xAll = 550
    if myColor > 360:
        myColor = 0
```		
---------------------------------------------
2. snejinka Снежинка оригинальный код		

```
xAll = 300
myColor = 0
def setup():
    size(600, 600)
    colorMode(HSB, 360, 100, 100)
	
def draw():
    global xAll, myColor
    background(100)
    fill(myColor, 100, 100)
    translate(xAll, 0)
    translate(300, 300)
    for x in -200, -100, 0, 100, 200:
        ellipse(x, 0, 50, 50)
        
    for y in -200, -100, 0, 100, 200:
        ellipse(0, y, 50, 50)
        
    for x in -200, -100, 0, 100, 200:
        ellipse(x, x, 50, 50)
        
    for x in -200, -100, 0, 100, 200:
        ellipse(x, -x, 50, 50)
    
    xAll -= 1
    myColor += 1
	if xAll == -550:
        xAll = 550
    if myColor > 360:
        myColor = 0	
```		
----------------------------------------------------
3. kvadrRyadColor Перекрывающиеся квадратики случайного цвета
 
C:\web\AlicaPython\AlisaCreativica\Skillspace\4_1\kvadrRyadColor.pyde

```
x = 0

def setup():
    size(600, 600)
    rectMode(CENTER)
    colorMode(HSB, 360, 100, 100)
    
def draw():
    global x
    
    for y in 150, 200, 250, 300, 350, 400, 450, 500:
        fill(random(360), 100, 100)
        rect(x, y, 25, 25)
    x += 5
```	
-----------------------------------------------------
4. 
ТЗ 1. Слева направо, от левого края холста, идёт ряд квадратов разных размеров.
Размеры квадратов 5, 15, 20, 50, 80. Отступ между левыми углами соседних квадратов
150, цвет квадратов — на выбор: красный, зелёный или синий. Нужно сделать, и
используя for

ТЗ 2а. По диагонали из левого в правый угол идёт ряд кругов одинакового
размера(30). Центры кругов всё дальше и дальше от краёв. Первый круг на 50 от
левого и верхнего края, второй ещё на 60(итого 110) дальше, третий ещё на 70(итого
180 от краёв), четвёртый ещё на 80, пятый ещё на 90. Цвет кругов на выбор: красный,
зелёный или синий, но не такой, как в предыдущем проекте. Сделать без translate()

2б. То же самое, но сделать через translate/
ТЗ 3. Два ряда квадратов, вертикальный и горизонтальный, образуют крест. И там и
там 5 квадратов, но центральные накладываются друг на друга и находятся ровно в
центре холста. Размеры квадратов 50 на 50, расстояние между левыми верхними
углами соседних квадратов в ряду 100. Цвет любой на выбор, кроме ранее
использованных. Сколько циклов потребуется для такого?

ТЗ 4а. Вертикальный ряд квадратов из 12 квадратов одинаковых размеров находится
на левом краю, но каждый кадр он движется вправо. При этом цвет каждого квадрата
на каждом кадре случайный и предыдущие версии квадратов не стираются. Сделать
через translate

ТЗ 4б. То же самое, но без использования translate

ТЗ 4в. То же самое, но цвет случайный на каждом кадре и при этом одинаковый для
всех квадратов на одном кадре, а не у каждого свой.

ТЗ 5. Людям с вероятностью эпилептических припадков поставить frameRate(1) или
ещё ниже(0.5, 0.25 и т.д.). Так вот:
на холсте каждый кадр в случайных местах появляется 9 кругов случайных цвета и
размера.

ТЗ 6. Вот такая снежинка, которая едет справа налево. Гораздо проще будет, если
сместить начало координат в центр холста и сделать сначала снежинку с центром в
центре холста. Цвет должен плавно меняться по ходу дела, сбрасываясь время от 
времени к начальному состоянию
--------------------------------------------------
5.
Дополнительные задания/ Задания для работы
дома
1) Ряд кругов от одного левого до правого края, минимум 5 кругов. Ряд спускается
сверху вниз
2) Диагональный ряд кругов(слева направо и сверху вниз). Движется от левого
нижнего угла к правому верхнему
3) Вертикальный ряд кругов, на цвет которых воздействует мышь. Чем мышь левее,
тем их цвет темнее, чем правее, тем цвет светлее
4) Диагональный ряд квадратов, размер квадратов растёт с каждым кадром
----------------------------------------------------------------------------------
6.
ТЗ 1. Слева направо, от левого края холста, идёт ряд квадратов разных размеров.
Размеры квадратов 5, 15, 20, 50, 80. Отступ между левыми углами соседних квадратов
150, цвет квадратов — на выбор: красный, зелёный или синий. Нужно сделать, и
используя for

```
space = 10
def setup():
    size(600, 600) 
    
def draw():
    global space
    for x in 5, 15, 20, 50, 80:
        fill(255, 0, 0)
        rect(space, 10, x, x)
        space += 150
```		
-----------------------------------------------------------------------------------
7.
ТЗ 2а. По диагонали из левого в правый угол идёт ряд кругов одинакового
размера(30). Центры кругов всё дальше и дальше от краёв. Первый круг на 50 от
левого и верхнего края, второй ещё на 60(итого 110) дальше, третий ещё на 70(итого
180 от краёв), четвёртый ещё на 80, пятый ещё на 90. Цвет кругов на выбор: красный,
зелёный или синий, но не такой, как в предыдущем проекте. Сделать без translate()

```
def setup():
    size(600, 600) 
    
def draw(): 
    i = 0
    space = 50
    dSpace = 10  
    for x in 1, 2, 3, 4, 5, 6, 7: 
        fill(0, 255, 0)
        ellipse(space, space, 30, 30) 
        i +=1
        space += 50 + dSpace*i  
```
--------------------------------------------------------------------------------------
8.
2б. То же самое, но сделать через translate/

def setup():
    size(600, 600) 
    
def draw(): 
    i = 0
    space = 50
    dSpace = 10  
    for x in 1, 2, 3, 4, 5, 6, 7:
        push() 
        fill(0, 255, 0)
        translate(space, space)
        ellipse(0, 0, 30, 30)
        pop() 
        i +=1
        space += 50 + dSpace*i
--------------------------------------------------------------------------------------
ТЗ 3. Два ряда квадратов, вертикальный и горизонтальный, образуют крест. И там и
там 5 квадратов, но центральные накладываются друг на друга и находятся ровно в
центре холста. Размеры квадратов 50 на 50, расстояние между левыми верхними
углами соседних квадратов в ряду 100. Цвет любой на выбор, кроме ранее
использованных. Сколько циклов потребуется для такого?

``` 
def setup():
    size(600, 600) 
    
def draw():
    global space
    for x in 30, 130, 230, 330, 430:
        fill(255, 0, 0)
        rect(x, 230, 50, 50)
        
    for y in 30, 130, 230, 330, 430:
        fill(255, 0, 0)
        rect(230, y, 50, 50)    
         
``` 
-------------------------------------------------------------
9.
ТЗ 4а. Вертикальный ряд квадратов из 12 квадратов одинаковых размеров находится
на левом краю, но каждый кадр он движется вправо. При этом цвет каждого квадрата
на каждом кадре случайный и предыдущие версии квадратов не стираются. Сделать
через translate	

``` 
x = 0

def setup():
    size(600, 600) 
    colorMode(HSB, 360, 100, 100)
    
def draw():
    global x
    
    translate(x, 0)
    for y in 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550:
        fill(random(360), 100, 100) 
        rect(0, y, 25, 25)
    x += 5
``` 
--------------------------------------------------------------------
10.
ТЗ 4б. То же самое, но без использования translate	

``` 
x = 0

def setup():
    size(600, 600) 
    colorMode(HSB, 360, 100, 100)
    
def draw():
    global x
    
    for y in 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550:
        fill(random(360), 100, 100)
        rect(x, y, 25, 25)
    x += 5 
``` 
-------------------------------------------------------------------------
11.
ТЗ 4в. То же самое, но цвет случайный на каждом кадре и при этом одинаковый для
всех квадратов на одном кадре, а не у каждого свой.

``` 
x = 0

def setup():
    size(600, 600) 
    colorMode(HSB, 360, 100, 100)
    
def draw():
    global x
    
    fill(random(360), 100, 100)
    for y in 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550: 
        rect(x, y, 25, 25)
    x += 5 
``` 
-----------------------------------------------------------------------------------
12.
ТЗ 5. Людям с вероятностью эпилептических припадков поставить frameRate(1) или
ещё ниже(0.5, 0.25 и т.д.). Так вот:
на холсте каждый кадр в случайных местах появляется 9 кругов случайных цвета и
размера.

``` 
def setup():
    size(600, 600) 
    colorMode(HSB, 360, 100, 100)
    frameRate(1)
    
def draw():
    global x 
    
    for y in 1, 2, 3, 4, 5, 6, 7, 8, 9: 
        fill(random(360), 100, 100)
        circleSize = random(0,100)
        ellipse(random(0,600), random(0,600), circleSize, circleSize)
``` 
-------------------------------------------------------------------------------------
13.	
ТЗ 6. Вот такая снежинка, которая едет справа налево. Гораздо проще будет, если
сместить начало координат в центр холста и сделать сначала снежинку с центром в
центре холста. Цвет должен плавно меняться по ходу дела, сбрасываясь время от 
времени к начальному состоянию

``` 
xAll = 300
myColor = 0
def setup():
    size(600, 600)
    colorMode(HSB, 360, 100, 100)
  
def draw():
    global xAll, myColor
    background(100)
    fill(myColor, 100, 100)
    translate(xAll, 0) 
    for x in 0, 200, 400:
        ellipse(x, 100, 50, 50)
        
    for x in 100, 200, 300:
        ellipse(x, 200, 50, 50)
        
    for x in 0, 100, 200, 300, 400:
        ellipse(x, 300, 50, 50)
            
    for x in 100, 200, 300:
        ellipse(x, 400, 50, 50) 
        
    for x in 0, 200, 400:
        ellipse(x, 500, 50, 50)
    
    xAll -= 1
    myColor += 1
    if xAll == -550:
        xAll = 550
    if myColor > 360:
        myColor = 0
``` 
----------------------------------------------------------		
14.
1) Ряд кругов от одного левого до правого края, минимум 5 кругов. Ряд спускается
сверху вниз

``` 
x = 20

def setup():
    size(600, 600) 
    colorMode(HSB, 360, 100, 100) 
    
def draw():
    global x  
    ellipse(x, x, 25, 25) 
    x +=30 
``` 
-------------------------------------------------------
15.	
2) Диагональный ряд кругов(слева направо и сверху вниз). Движется от левого
нижнего угла к правому верхнему

``` 
x = 20
y = 580
def setup():
    size(600, 600) 
    colorMode(HSB, 360, 100, 100) 
    
def draw():
    global x, y  
    ellipse(x, y, 25, 25) 
    x +=30
    y -=30
``` 	
----------------------------------------------------------------------------------	
3) Вертикальный ряд кругов, на цвет которых воздействует мышь. Чем мышь левее,
тем их цвет темнее, чем правее, тем цвет светлее

``` 
y = 20
colorValue = 0
def setup():
    size(600, 600) 
    colorMode(HSB, 360, 100, 100) 
    
def mouseMoved():
    global colorValue
    colorValue = mouseX 
    
def draw():
    global y   
    background(360)
    fill(colorValue/2) 
    for y in 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15:
        ellipse(20, y*40, 30, 30)
``` 
---------------------------------------------------------------	 
4) Диагональный ряд квадратов, размер квадратов растёт с каждым кадром

``` 
x = 20
rectSize = 20 
def setup():
    size(600, 600) 
    colorMode(HSB, 360, 100, 100)  
    
def draw():
    global x, rectSize  
    
    fill(360) 
    rect(x, x, rectSize, rectSize)
    x +=40
    rectSize +=5
``` 	
-------------------------------------------------------------------
*******************************************************************************************************************************
                                                   Такой удобный range
*******************************************************************************************************************************	
1. 
Определения, которые нужно запомнить
range() — функция-генератор наборов чисел
Если в range() три аргумента, то первый — начало, второй — конец(сам конец не
берётся), третий — шаг последовательности
range(5) сгенерирует набор чисел 0, 1, 2, 3, 4
range(1, 5) сгенерирует набор чисел 1, 2, 3, 4
range(1, 11, 3) сгенерирует набор 1, 4, 7, 10
range(11, 1, -2) сгенерирует набор 11, 9, 7, 5, 3
--------------------------------------------------------
2.
Пример объяснения
Этот код

``` 
def draw():
    for x in 0, 20, 40, 60, 80, 100:
        rect(x, 0, 20, 20)
``` 		

Изобразит такой код:
Смотрите, видите, каждое следующее число больше предыдущего на 20. А сможете
написать код, который выведет 50 таких прямоугольников? Не сильно муторно?
Писать 50 чисел?
К счастью, у нас есть функция, которая может генерировать такую
последовательность чисел за нас.

``` 
def draw():
    for x in range(0, 101, 20):
        rect(x, 0, 20, 20)
``` 		

Функция range() здесь возвращает набор чисел от 0 до 100. Не до 101! До 100. Всегда
оно берёт на 1 меньше второго аргумента. Итак, числа от 0 до 100. А что означает
третий аргумент, 20? Это шаг. Каждое следующее число в наборе будет больше
предыдущего на 20.
А что будет, если написать вот такой код?

``` 
def draw():
    for x in range(0, 100):
        rect(x, x, 20, 20)
``` 
		
Будет так
Видите, ошибки нет. Кто понял, как это работает? Если шаг, третий аргумент, не
указан, он равняется 1. Но погодите! Если написать так

``` 
def draw():
    for x in range(100):
        rect(x, x, 20, 20)
``` 
		
Будет то же самое.
Если аргумент у range() всего один, то начало автоматически считается 0, шаг 1. А
конец — единственный аргумент.
Поэтому! Если вы хотите, чтобы цикл просто повторил один и тот же неотличающийся
никак код, то пишите просто for i in range(n): — вместо n число повторений. он
подставит n чисел 0, 1, 2, 3…n-1
----------------------------------------------
3.
Задания по теме «Такой удобный range()»
ТЗ 1.а. С помощью for и range изобразите вот такой круг

``` 
y = 0 
def setup():
    size(600, 600) 
    colorMode(HSB, 360, 100, 100)  
    
def draw():
    global y 
    
    for x in range(0, 600, 20):
        rect(x, y, 20, 20)
        
    y += 20
``` 	
---------------------------------------------------------
4.	
ТЗ 1.б. Мозаика. То же самое, но каждую секунду каждый из квадратиков заполняется
случайным цветом

y = 0 
def setup():
    size(600, 600) 
    colorMode(HSB, 360, 100, 100)  
    
def draw():
    global y  
    for x in range(0, 600, 20):
        fill(random(0, 360), 120, 120)
        rect(x, y, 20, 20)
        
    y += 20 
-----------------------------------------------------------------	
5.
ТЗ 1.в. То же самое, что в 1а, но квадрат, на который наведена мышь, окрашивается в
жёлтый цвет. Вот ссылки на функции коллизий: shorturl.at/syQS1
rb.gy/inzu5s 
 

cellSize = 50 # Размер одного квадрата 
cols = 10
rows = 10
  
def setup():
  size(500, 500) 

def draw():
  background(255)  
  for i in range(0, cols):
    for j in range(0, rows): 
      x = i * cellSize
      y = j * cellSize

      # Проверяем, находится ли мышь над квадратом
      if (mouseX > x and mouseX < x + cellSize and mouseY > y and mouseY < y + cellSize):
        fill(255, 255, 0); # Жёлтый цвет
      else:
        fill(200) # Серый цвет 

      rect(x, y, cellSize, cellSize) # Рисуем квадрат 
-----------------------------------------------------------------	
5.2.
ТЗ 1.в. То же самое, что в 1а, но квадрат, на который наведена мышь, окрашивается в
жёлтый цвет. Вот ссылки на функции коллизий: shorturl.at/syQS1
rb.gy/inzu5s
	  
def collidePointRect(pointX, pointY, x, y, xW, yW):
#если точка находится между краёв прямоугольника:
    if (pointX >= x) and (pointX <= x + xW) and (pointY >= y) and (pointY <= y + yW): 
        return True
    return False

def setup():
    size(300,300)
    
def draw():
    for x in range(0,300,10):
        for y in range(0,300,10):
            rect(x,y,10,10)
            if collidePointRect(mouseX,mouseY,x,y,10,10):
                fill(255,255,0)
            else:
                fill(255)	  
---------------------------------------------------------------------------
6.
ТЗ 2. Круги! 17 кругов. Первый круг шириной 20, второй — 40, третий — 60 и так до
самого конца. Первый круг в центре, второй на 20 правее и ниже центра, третий на 40
правее и ниже центра, четвёртый на 60 правее и ниже центра и т.д. до конца.
Цветовая модель HSB 360 100 100. Цвет первого круга 20 100 100, второго 40 100 100,
третьего 60 100 100 и так до самого конца.

y = 0 
def setup():
    size(600, 600) 
    colorMode(HSB, 360, 100, 100)  
    
def draw():
    global y
    circleWidth = 20
    circleX = 300
    circleH = 20
    for x in range(0, 17): 
        fill(circleH, 100, 100)
        ellipse(circleX, circleX, circleWidth, circleWidth)
        circleWidth += 20
        circleX += 20
        circleH += 20
------------------------------------------------------------------------------
7. 	 
ТЗ 3. Два ряда квадратов, вертикальный и горизонтальный, образуют крест. И там и
там 5 квадратов, но центральные накладываются друг на друга и находятся ровно в
центре холста. Размеры квадратов 50 на 50, расстояние между левыми верхними
углами соседних квадратов в ряду 100. Цвет любой на выбор, кроме белого, серого и
чёрного. Сколько циклов потребуется для такого?

circleWidth = 50 
def setup():
    size(600, 600) 
    colorMode(HSB, 360, 100, 100)  
    
def draw():  
    circleX = 100
    circleY = 100
     
    for x in range(0, 5): 
        fill(360, 100, 100)
        rect(circleX, 300, circleWidth, circleWidth) 
        circleX += 100 
        
    for x in range(0, 5): 
        fill(360, 100, 100)
        rect(300, circleY, circleWidth, circleWidth) 
        circleY += 100
-----------------------------------------------------------------------------------		
8. TODO
ТЗ 4а. Горизонтальный ряд квадратов из 12 квадратов одинаковых размеров
находится на верхнем краю, но каждый кадр он движется вниз. При этом цвет каждого
квадрата на каждом кадре случайный и предыдущие версии квадратов не стираются.
Если нажать стрелки вправо или влево, все 12 квадратов смещаются вправо или
влево. Сделать через translate в цикле

circleWidth = 20 
circleY = 10
def setup():
    size(600, 600) 
    colorMode(HSB, 360, 100, 100)  
    
def draw():
    global circleY 
    circleX = 10  
    
    translate(0, circleY) 
    for x in range(0, 12):
        fill(random(0, 360),100,100)  
        rect(circleX, 0, circleWidth, circleWidth) 
        circleX += 30
    circleY += 5 
-----------------------------------------------------------------------
9.  
ТЗ 4б. То же самое, но без использования translate в цикле

circleWidth = 20 
circleY = 10
def setup():
    size(600, 600) 
    colorMode(HSB, 360, 100, 100)  
    
def draw():
    global circleY 
    circleX = 10  
     
    fill(random(0, 360),100,100) 
    for x in range(0, 12):  
        rect(circleX, circleY, circleWidth, circleWidth) 
        circleX += 30
    circleY += 30 
------------------------------------------------------------------------
*******************************************************************************************************************************
                                                      цикл While
*******************************************************************************************************************************
1.
```
def setup():
    size(600,600)
    x = 0
    while x < 600:
        line(x,599,x,x)    
        x = x + 2
```		
-----------------------------
```
listX = [5,6,7]
listY = [20,20,20]
sc = 0

def setup():
    size(600,600)
    
def draw():
    global sc, listX, listY
    for x in range(0,600,20):
        for y in range(0,600,20):
            rect(x,y,20,20)
    
    sc = sc + 1
    if sc == 18:
        listX.append(listX[len(listX)-1]+1)
    
    for z in range(0,len(listX)):
        push()
        fill(0,250,0)
        rect(listX[z]*20,listY[z]*20,20,20)
        pop()
```		
------------------------------------------		
1.
```
def setup():
    size(900, 500)
    x = 0
    while x < 900:
        rect(x, 0, 8, 8)
        x = x + 8
```

Изобразит такой код:
Это цикл While, цикл «Пока». Пока оператор while получает True, код с отступом после
него снова и снова будет выполняться, а потом будет выполняться сначала, с
заголовка — строки, которая начинается с while.
While очень похож на одиночный if, только циклится.
В While можно использовать выражения с логическими операторами

```
def setup():
    size(900, 500)
    x = 0
    y = 0
    while x < 900 and y < 500:
        rect(x, y, 8, 8)
        x = x + 8
        y = y + 4
```		
Попробуем поменять шаги с 8 и 4 на другие числа и посмотрим, как всё работает. А
давайте ещё поменяем условие x < 900 and y < 500 на x < 700 and y < 300, чтобы
увидеть результат.
--------------------------------------------------------
2.
ТЗ 1. Вертикальный ряд кругов от верхнего края до нижнего, размер круга 10, круги
ровно от края до края. Цвет каждого круга случайный

```
def setup():
    size(900, 500)
    colorMode(HSB, 360, 100, 100) 
    y = 5 
    while y < 500:
        ellipse(5, y, 10, 10)
        y = y + 10
```
-----------------------------------------------------------------------------
3. ТЗ 2. Горизонтальный ряд из вертикальных линий от левого края до середины холста.
Первая линия длиной в 5, каждая следующая длиннее на 2. При этом цвет
равномерно меняется от линии к линии(HSB)

```
def setup():
    size(900, 500)
    colorMode(HSB, 360, 100, 100)
    global x,lineHeight,lineColor
    x = 0 
    lineHeight = 5
    lineColor = 360
    strokeWeight(2) 
    while x < 900:
        stroke(lineColor, 100, 100) 
        line(x, 500, x, 500 - lineHeight)
        x = x + 4 
        lineHeight = lineHeight + 2
        lineColor = lineColor - 1  
```
------------------------------------------------------------------------------
4. ТЗ 3. Косой крест из крестиков. Этот код изобразит крест:

translate(100, 100)
strokeWeight(10)
line(-10, -10, 10, 10)
line(-10, 10, 10, -10)

Напишите программу с использованием translate(), push() и pop() и двух циклов while,
которая изобразит такой косой крест, каждый ряд крестов идёт от угла до
противоположного угла. Но цвет каждого крестика случайный. Не забывайте про 
frameRate(1)

```
def setup():
    size(500, 500)
    colorMode(HSB, 360, 100, 100)
    global x, y, x2, colorH
    strokeWeight(10)
    x = 30
    y = 480
    x2 = 20 
    while x < 900: 
        push()
        translate(x, x) 
        colorH = int(random(0, 360)) 
        stroke(colorH, 100, 100)
        line(-10, -10, 10, 10)
        line(-10, 10, 10, -10)
        x = x + 30
        pop()
    while y > 0:
        push()
        translate(x2, y)
        colorH = int(random(0, 360)) 
        stroke(colorH, 100, 100) 
        line(-10, -10, 10, 10)
        line(-10, 10, 10, -10)
        y = y - 30
        x2 = x2 + 30
        pop() 
```		
------------------------------------------------------  
ТЗ 4. Три ряда кругов, где нужно кликнуть, чтобы поменять цвет, а при снятии клика
цвет исчезает
Вот ссылки на функции коллизий: shorturl.at/syQS1
rb.gy/inzu5s

```
circle_diameter = 30
circles = []
def setup():
    size(600, 400)
    noStroke()
    createCircleList()

def collidePointCircle(x, y, cx, cy, d):
    if dist(x,y,cx,cy) <= d/2:
        return True
    else:
        return False

def createCircleList(): 
    global  circles
    row = 1 
    # Генерация координат кругов
    while row < 14:
        col = 1
        while col < 4:
            x = col * circle_diameter  
            y = row * circle_diameter  
            circles.append([x,y,False])
            col = col + 1
        row =  row + 1    

def draw():
    background(240)
    
    # Рисуем круги
    for circle in circles:
        if circle[2]:
            fill(255, 0, 0)  # Цвет активного круга
        else:
            fill(200)  # Цвет неактивного круга
        ellipse(circle[0], circle[1], circle_diameter, circle_diameter)

def mousePressed():
    # Проверяем, попал ли клик в круг
    for circle in circles: 
        mouseInCircle = collidePointCircle(mouseX,mouseY,circle[0],circle[1],30)
        if mouseInCircle:
            circle[2] = not circle[2]
         
```			
----------------------------------------------
6. ТЗ 5. Ряд из треугольников через While. На их цвет воздействует положение мыши на
холсте. Чем выше мышь, тем цвет светлее, чем ниже — тем темнее

```
def setup():
    size(900, 500)
    colorMode(HSB, 360, 100, 100)  

def draw():
    x = 30     
    while x < 900:
        translate(x, 0)
        fill(500 - mouseY)
        triangle(30, 75, 58, 20, 86, 75)
        x = x + 40
```		
---------------------------------------------------
7. 
Дополнительные задания/ Задания для работы
дома
1) Ряд кругов от одного левого до правого края, минимум 5 кругов. Ряд спускается
сверху вниз

```
def setup():
    size(900, 500)
    colorMode(HSB, 360, 100, 100)  

def draw():
    x = 30     
    while x < 500: 
        ellipse(x, x, 30, 30)
        x = x + 40
```
-------------------------------------------------
8.
2) Диагональный ряд кругов(слева направо и сверху вниз). Движется от левого
нижнего угла к правому верхнему

```
def setup():
    size(900, 500)
    colorMode(HSB, 360, 100, 100)  

def draw():
    x = 30
    y = 470     
    while x < 500: 
        ellipse(x, y, 30, 30)
        x = x + 40
        y = y - 40 
```		
---------------------------------------------
9.
3) Вертикальный ряд кругов, на цвет которых воздействует мышь. Чем мышь левее,
тем их цвет темнее, чем правее, тем цвет светлее

```
def setup():
    size(900, 500) 

def draw(): 
    y = 30 
    while y < 500: 
        fill(mouseX/4)
        ellipse(30, y, 30, 30) 
        y = y + 40
```
-----------------------------------------------------
10.
4) Диагональный ряд квадратов, размер квадратов растёт с каждым кадром

```
def setup():
    size(900, 500) 

def draw(): 
    x = 30 
    while x < 500: 
        rect(x, x, x, x) 
        x = x + 10 
```		
***************************************************************************************************************
                                                 Циклы с rotate()
***************************************************************************************************************
 Сегодня мы будем использовать циклы для ухоров, заодно повторим использование
команды rotate. Смотрите, вот сделаем проект, в котором точка 0, 0 была перенесена в
центр. Из центра у нас идёт «луч» — три круга, они на уровне 0 по второй координате,

```
def setup():
    size(600, 400)
def draw():
	translate(300, 200)
	ellipse(20, 0, 20, 20)
	ellipse(50, 0, 20, 20)
	ellipse(80, 0, 20, 20)
```	

скопируем три команды нашего «луча», поставим перед копией поворот на 5ю часть
круга:

```
def setup():
    size(600, 400)
def draw():
	translate(300, 200)
	ellipse(20, 0, 20, 20)
	ellipse(50, 0, 20, 20)
	ellipse(80, 0, 20, 20)
	rotate(radians(360/5))
	ellipse(20, 0, 20, 20)
	ellipse(50, 0, 20, 20)
	ellipse(80, 0, 20, 20)
```

Так же можно ещё добавлять лучи:

```
def setup():
    size(600, 400)
def draw():
	translate(300, 200)
	ellipse(20, 0, 20, 20)
	ellipse(50, 0, 20, 20)
	ellipse(80, 0, 20, 20)
	rotate(radians(360/5))
	ellipse(20, 0, 20, 20)
	ellipse(50, 0, 20, 20)
	ellipse(80, 0, 20, 20)
	rotate(radians(360/5))
	ellipse(20, 0, 20, 20)
	ellipse(50, 0, 20, 20)
	ellipse(80, 0, 20, 20) 
	rotate(radians(360/5))
```	

Тут повторяется четыре команды — три ellipse и одна rotate(). Повторим их с помощью
цикла 5 раз:

```
def setup():
    size(600, 400)
def draw():
	translate(300, 200)
	for i in range(5):
	    ellipse(20, 0, 20, 20)
	    ellipse(50, 0, 20, 20)
	    ellipse(80, 0, 20, 20)
	    rotate(radians(360/5))
```		

Можно получившийся узор смещать, меняя координаты в translate(), можно вращать
его, добавив rotate(), после этого translate()

```
angle = 0
def setup():
    size(600, 400)
def draw():
	global angle
	background(255)
	translate(300, 200)
	rotate(radians(angle))
	for i in range(5):
	    ellipse(20, 0, 20, 20)
	    ellipse(50, 0, 20, 20)
	    ellipse(80, 0, 20, 20)
	    rotate(radians(360/5))
	angle = angle + 1
```	
------------------------------------------------
Задания по теме «Циклы с rotate»

ТЗ 1. Сделать два проекта, и через for и через while:8 квадратов вокруг
центрального круга вот так, не забудьте закрасить круг зелёным, а
квадраты жёлтым.

```
angle = 0
def setup():
    size(600, 400)
def draw():
  global angle
  background(255)
  translate(300, 200)
  
  fill(0,255,0)
  ellipse(0, 0, 20, 20)
  
  fill(255,255,84)
  rotate(radians(angle))
  for i in range(8): 
      rect(-10, -40, 18, 18)
      rotate(radians(360/8)) 
  angle = angle + 1
```  
-----------------------------------------------
ТЗ 1. Сделать два проекта, и через  while:8 квадратов вокруг
центрального круга вот так, не забудьте закрасить круг зелёным, а
квадраты жёлтым.

```
angle = 0
def setup():
    size(600, 400)
def draw():
  background(255)
  global angle 
   
  translate(300, 200)
  
  fill(0,255,0)
  ellipse(0, 0, 20, 20) 
  rotate(radians(angle))
  fill(255,255,84)
  i = 0 
  while i < 9:
      i = i + 1 
      rect(-10, -40, 18, 18)
      rotate(radians(360/8)) 
  angle = angle + 1
```  
--------------------------------------------  
ТЗ 2. Сделать два проекта, и через for и через while.
Примерно такой узор — в каждом луче примерно такие
квадрат, треугольник и круг, узор окрашен в разные оттенки
одного цвета, от центра к краю темнеет(лучше использовать
модель HSB)

``` 
def setup():
    size(600, 400)
    colorMode(HSB, 360, 100, 100)
def draw():
  global angle
  background(255)
  translate(300, 200)
  
  fill(200,65,95)
  ellipse(0, 0, 20, 20)  
   
  for i in range(8): 
      
      fill(200,95,80)  
      rect(-10, -40, 18, 18)
      
      fill(200,60,60) 
      ellipse(-3, -80, 20, 40)
      
      fill(200,80,40)  
      triangle(-16, -110, 8, -110,  -3, -150)
      
      rotate(radians(360/8))
```	  
---------------------------------------------------
ТЗ 2. while: Сделать два проекта, и через for и через while.
Примерно такой узор — в каждом луче примерно такие
квадрат, треугольник и круг, узор окрашен в разные оттенки
одного цвета, от центра к краю темнеет(лучше использовать
модель HSB)

``` 
def setup():
    size(600, 400)
    colorMode(HSB, 360, 100, 100)
def draw():
  global angle
  background(255)
  translate(300, 200)
  
  fill(200,65,95)
  ellipse(0, 0, 20, 20)  
  
  triangle(-16, -110, 8, -110,  -3, -150)
  i = 0 
  while i < 9:
      i = i + 1  
      
      fill(200,95,80)  
      rect(-10, -40, 18, 18)
      
      fill(200,60,60) 
      ellipse(-3, -80, 20, 40)
      
      fill(200,80,40)  
      triangle(-16, -110, 8, -110,  -3, -150)
      
      rotate(radians(360/8))  
```
-------------------------------------------------
ТЗ 3.
Сделать два проекта, и через for и через while. Этот
узор(линия-quad-эллипс) должен вращаться, если держать
одну из клавиш — при нажатии на стрелку вправо крутится в
одну сторону, при нажатии на стрелку влево дожен крутиться в
другую сторону

```
angle = 0
rotateSpeed = 0
def setup():
    size(600, 400)
    colorMode(HSB, 360, 100, 100)
    
def keyPressed():
    global rotateSpeed
    if keyCode == LEFT:
       rotateSpeed = -0.2 
    if keyCode == RIGHT:
       rotateSpeed = 0.2 
          
def draw():
  global angle
  background(255)
  translate(300, 200)
  
  fill(200,65,95)
  ellipse(0, 0, 20, 20)  
   
  rotate(radians(angle)) 
  angle = angle + rotateSpeed
  
  for i in range(8): 
      line(8, 8, 15, 15)
       
      fill(200,95,80)  
      rect(13, 13, 13, 13)
      
      fill(200,60,60) 
      ellipse(-3, -100, 40, 10) 
      
      rotate(radians(360/8))
```	  
-------------------------------------------------
ТЗ 3.
Сделать два проекта, через while. Этот
узор(линия-quad-эллипс) должен вращаться, если держать
одну из клавиш — при нажатии на стрелку вправо крутится в
одну сторону, при нажатии на стрелку влево дожен крутиться в
другую сторону

```
angle = 0
rotateSpeed = 0
def setup():
    size(600, 400)
    colorMode(HSB, 360, 100, 100)
    
def keyPressed():
    global rotateSpeed
    if keyCode == LEFT:
       rotateSpeed = -0.2 
    if keyCode == RIGHT:
       rotateSpeed = 0.2 
          
def draw():
  global angle
  background(255)
  translate(300, 200)
  
  fill(200,65,95)
  ellipse(0, 0, 20, 20)  
   
  rotate(radians(angle)) 
  angle = angle + rotateSpeed
  
  i = 0 
  while i < 9:
      i = i + 1  
      
      line(8, 8, 15, 15)
       
      fill(200,95,80)  
      rect(13, 13, 13, 13)
      
      fill(200,60,60) 
      ellipse(-3, -100, 40, 10) 
      
      rotate(radians(360/8))
```	  
-------------------------------------------------
ТЗ 4. Сделать два проекта, и через for и через while. Тут
отключены обводки через noStroke(). Каждый кадр проект
немного увеличивается и поворачивается по часовой стрелке,
не стирая предыдущий кадр. Получается такая штука: 
------------------------------------------------------------

СЗ 1. Свой проект с узором через циклы на выбор
----------------------------------------------------
Дополнительные задания/ Задания для работы
дома
------------------------------------------------------
ТЗ 1. Создай анимацию на основе любого из узоров. Например, чтобы его элементы
«дышали», увеличиваясь
--------------------------------------------------------
ТЗ 2. Сделай узор, который будет следовать за курсором мыши
-------------------------------------------------













	
 
   
   


     


 

 
 








