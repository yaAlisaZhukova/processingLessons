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
     ellipse(150+x,150,155,25) 
     quad(60+x, 130, 70+x, 125, 110+x, 150, 85+x, 150)  
     quad(140+x, 110, 150+x, 100, 200+x, 140, 165+x, 140) 
     quad(140+x, 190, 150+x, 200, 200+x, 160, 165+x, 160)     
   
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
6. boxten. Метод с параметрами.

```
def setup():
    size(600, 600)
    
def boxten(x): 
    strokeWeight(2)
    stroke(0)
    fill(128,0,128)
    ellipse(150+x,160,25,25)

    fill(128,0,128)
    strokeWeight(3)
    stroke(100,0,100)
    rect(90+x,90,100,100)
    stroke(148,0,148)
    rect(96+x,96,88,88)

    strokeWeight(2)
    stroke(0)
    fill(128,0,128)
    ellipse(150+x,160,25,25)

    fill(255)
    strokeWeight(2)
    stroke(0)
    ellipse(116+x,136,38,38)
    ellipse(165+x,137,38,38)

    fill(0)
    ellipse(116+x,136,25,25)
    ellipse(165+x,137,25,25)

    strokeWeight(3)
    stroke(148,0,148)
    line(96+x,96,105+x,105)
    line(184+x,96,175+x,105)
    line(96+x,185,105+x,175)
    line(184+x,184,175+x,175)
    
def draw():
    boxten(0) 
    boxten(200) 
```
------------------------------------------
7. Машинка. Метод с параметрами. 
```
def setup():
    size(600, 600)
    
def car(x,y):  
    fill(155)
    circle(32+x, 38+y, 18) 
    circle(82+x, 38+y, 18)
    circle(32+x, 130+y, 18)
    circle(82+x, 130+y, 18)
    fill(155, 166, 255)
    rect(30+x, 20+y, 55, 135, 6, 6, 18, 18)
    fill(155) 
    rect(35+x, 115+y, 45, 30, 6, 6, 18, 18)
    
def draw():
    car(120, 50) 
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
													   Алиса - кнопки на экране
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
    y = 0
    for x in clrcleXList:
        y += 50 
        fill(255,0,0)
        circle(x,y,30)
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
    clrcleX.append(random(20, 630))    
    
def draw():
    y = 0  
    for x in clrcleX:
        y += 50 
        fill(255,0,0)
        circle(x,y,30)
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
        y += 50 
        fill(255,0,0)
        circle(x,y,30)
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
    y = 0  
    for x in clrcleX:
        y += 50 
        fill(255,0,0)
        circle(x,y,30)
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
--------------------------------------------------
9. Собираем сокровища в лабиринте
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
```
i = 0 

def setup():  
  global catImageList 
  size(640, 360)
  
  catImageList = []
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

def setup():  
  global catImageList 
  size(640, 360)
  
  catImageList = []
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
```
x = 130
y = 400
cakeX = 680
cakeY = 30
showCake = True
def setup(): 
  global savanna 
  global elephanta
  global cake
  size(640, 640)
  savanna = loadImage("Savanna.png") 
  elephanta = loadImage("elephant-a.png")
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
   global cakeX, cakeY, showCake 
   image(savanna, 0, 0, 640, 640) 
   image(elephanta, x, y, 200, 150)
   
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
------------------------------------------------
2. Для игры гонки. Да они ВСЕ по встречке едут!!!!!

```
carListY = [-1100, -810, -600, -300, -50, 250, 500]
carListY2 = [-1200, -900, -650, -220, -70, 350, 550]
carListY3 = [-680, 350, 550]
carListY4 = [-320, -110,]
lineBetweenRoads = [-50,100,250,400,550,700,900]
dy = 0
myCarX = 380

def setup():
    size(600, 600)
    
def car(x,y):  
    fill(155)
    circle(32+x, 38+y, 18) 
    circle(82+x, 38+y, 18)
    circle(32+x, 130+y, 18)
    circle(82+x, 130+y, 18)
    fill(155, 166, 255)
    rect(30+x, 20+y, 55, 135, 6, 6, 18, 18)
    fill(155) 
    rect(35+x, 115+y, 45, 30, 6, 6, 18, 18)
    
def myCar(x,y):  
    fill(155)
    circle(32+x, 38+y, 18) 
    circle(77+x, 38+y, 18)
    circle(32+x, 120+y, 18)
    circle(77+x, 120+y, 18)
    fill(255, 166, 183)
    rect(30+x, 20+y, 50, 120, 18, 18, 6, 6)
    fill(155) 
    rect(35+x, 30+y, 40, 28, 18, 18, 8, 8)    
    
def carMove():      
    global dy
    for i in range(0,6):
       fill(255)
       noStroke()
       rect(width/2,lineBetweenRoads[i],20,100)
   
    for y in carListY:
        car(120, y + dy)
    for y in carListY3:
        car(205, y + dy)
    for y in carListY2:
        car(305, y + dy) 
    for y in carListY4:
        car(395, y + dy)   
    if dy == 1000:
        dy = 0
    dy += 1  
        
def keyPressed():
    global myCarX
    if keyCode == RIGHT: 
       myCarX = myCarX + 5
    if keyCode == LEFT: 
       myCarX = myCarX - 5  
                                        
def draw():
    background(155)
    fill(100) 
    rect(140,0,350,600)  
    carMove()
    myCar(myCarX, 400) 
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
-----------------------------------------------------
2. Таймер:

```
# метод timer меняет значение глобальной переменной timerValue
# что бы добавить timer() в свой проект, надо добавить глобальную переменную timerValue
# и вызвать timer() в методе draw()

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



   
   
   
   


     


 

 
 








