import turtle
import random

#numNodes = 20
numNodes = 2000
#scale = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
scale = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250]

numNodesAP = []
for i in range(40):
  numNodesAP.append(0)

class Coordinates:
  def __init__(self, x, y):
    self.x = x
    self.y = y

apLocations = [Coordinates(-250, 150), Coordinates(-174, 150), Coordinates(-98, 150), Coordinates(-22, 150), Coordinates(54, 150), Coordinates(130, 150), Coordinates(206, 150), Coordinates(282, 150),   Coordinates(-250, 72), Coordinates(-174, 72), Coordinates(-98, 72), Coordinates(-22, 72), Coordinates(54, 72), Coordinates(130, 72), Coordinates(206, 72), Coordinates(282, 72),   Coordinates(-250, -6), Coordinates(-174, -6), Coordinates(-98, -6), Coordinates(-22, -6), Coordinates(54, -6), Coordinates(130, -6), Coordinates(206, -6), Coordinates(282, -6),    Coordinates(-250, -84), Coordinates(-174, -84), Coordinates(-98, -84), Coordinates(-22, -84), Coordinates(54, -84), Coordinates(130, -84), Coordinates(206, -84), Coordinates(282, -84),    Coordinates(-250, -162), Coordinates(-174, -162), Coordinates(-98, -162), Coordinates(-22, -162), Coordinates(54, -162), Coordinates(130, -162), Coordinates(206, -162), Coordinates(282, -162)]

def setAccessPoints():
  ap = turtle.Turtle()
  ra = turtle.Turtle()
  index = 0
  for i in apLocations:
    ra.speed(200000)
    ra.penup()
    ra.setpos(i.x, i.y - 35)
    if(numNodesAP[index] < scale[0]):
      ra.fillcolor('white')
    elif(numNodesAP[index] < scale[1]):
      ra.fillcolor('azure')
    elif(numNodesAP[index] < scale[2]):
      ra.fillcolor('lightcyan')
    elif(numNodesAP[index] < scale[3]):
      ra.fillcolor('paleturquoise')
    elif(numNodesAP[index] < scale[4]):
      ra.fillcolor('cyan')
    elif(numNodesAP[index] < scale[5]):
      ra.fillcolor('violet')
    elif(numNodesAP[index] < scale[6]):
      ra.fillcolor('pink')
    elif(numNodesAP[index] < scale[7]):
      ra.fillcolor('salmon')
    elif(numNodesAP[index] < scale[8]):
      ra.fillcolor('red')
    elif(numNodesAP[index] < scale[9]):
      ra.fillcolor('firebrick')
    else:
      ra.fillcolor('maroon')
    ra.pendown()
    ra.begin_fill()
    ra.circle(40)
    ra.end_fill()
    ra.penup()

    ap.speed(200000)
    ap.penup()
    ap.setpos(i.x, i.y)
    ap.fillcolor('black')
    ap.pendown()
    ap.begin_fill()
    ap.circle(5)
    ap.end_fill()
    ap.penup()
    index = index + 1
  ap.setpos(1000, 1000)
  ra.setpos(1000, 1000)
  
def moveAlongPath(t):
    ran = ''
    for k in apLocations:
          if (k.x >= t.xcor()-40 and k.x <= t.xcor()+40 and k.y >= t.ycor()-40 and k.y <= t.ycor()+40):
            if(k.x == -250 and k.y == 150):
                ran = random.choice(['south', 'east'])
            elif(k.x == 282 and k.y == 150):
                ran = random.choice(['south', 'west'])
            elif(k.x == -250 and k.y == -162):
                ran = random.choice(['north', 'east'])
            elif(k.x == 282 and k.y == -162):
                ran = random.choice(['north', 'west'])
            elif(k.y == 150):
                ran = random.choice(['south', 'west', 'east'])
            elif(k.y == -162):
                ran = random.choice(['north', 'west', 'east'])
            elif(k.x == 282):
                ran = random.choice(['south', 'west', 'north'])
            elif(k.x == -250):
                ran = random.choice(['south', 'east', 'north'])
            else:
                ran = random.choice(['north', 'east', 'south', 'west'])
    if(ran == 'north'):
        t.setpos(t.xcor(), t.ycor()+80)
    elif(ran == 'south'):
        t.setpos(t.xcor(), t.ycor()-80)
    elif(ran == 'east'):
        t.setpos(t.xcor()+80, t.ycor())
    elif(ran == 'west'):
        t.setpos(t.xcor()-80, t.ycor())
                

def outputData():
  idNum = 0
  for i in numNodesAP:
    print "AP ID: ", idNum, "... Num Nodes on Wi-Fi: ", i
    idNum = idNum + 1

print('MENU')
print('[1] Random Walk')
print('[2] Random Waypoint')
print('[3] Pathway')
modelNum = input('Choose a Model: ')
print('[1] All Wi-Fi, No App') #wifi cond is 2 for all
print('[2] All Wi-Fi, All App') #wifi cond is 1 for all
print('[3] Some Wi-Fi, Some App') #wifi cond is 0 and 2 or steady 1 switch on and off
setting = input('Choose a Setting: ')
# 0=no wifi, 1=wifi app, 2=wifi no app

wifiCond = []
if(setting == 1):
    for i in range(numNodes):
        wifiCond.append(2)
elif(setting == 2):
    for i in range(numNodes):
        wifiCond.append(1)
elif(setting == 3):
    split = numNodes / 2
    for i in range(split):
        wifiCond.append(random.choice([0, 2]))
    for i in range(split):
        wifiCond.append(1)

setAccessPoints()

nodes = []
indexN = 0
for i in range(numNodes):
  t = turtle.Turtle()
  t.shape("circle")
  t.shapesize(0.5, 0.5, 0.5)
  if(wifiCond[indexN] == 0):
    t.color("red")
  elif(wifiCond[indexN] == 1):
    t.color("blue")
  elif(wifiCond[indexN] == 2):
    t.color("green")
  t.penup()
  nodes.append(t)
  indexN = indexN + 1

if(modelNum == 1):
    for i in range(10):
      indexJ = 0
      for l in range(40):
        numNodesAP[l] = 0
      for j in nodes:
        j.penup()
        j.speed(2000)
        ranDirection = random.choice(["left", "right"])
        ranDegree = random.randrange(0, 360, 1)
        if (ranDirection == "left"):
            j.left(ranDegree)
        elif (ranDirection == "right"):
            j.right(ranDegree)
        j.forward(20)
        index = 0
        for k in apLocations:
          if (k.x >= j.xcor()-40 and k.x <= j.xcor()+40 and k.y >= j.ycor()-40 and k.y <= j.ycor()+40):
            if(wifiCond[indexJ] == 1):
                numNodesAP[index] = numNodesAP[index] + 0.5
            elif(wifiCond[indexJ] == 2):
                numNodesAP[index] = numNodesAP[index] + 1
          index = index + 1
        indexJ = indexJ + 1
      setAccessPoints()
      outputData()

if(modelNum == 2):
    for i in range(10):
      indexJ = 0
      for l in range(40):
        numNodesAP[l] = 0
      for j in nodes:
        j.penup()
        j.speed(2000)
        j.setpos(random.randrange(-290, 322, 1), random.randrange(-202, 190, 1))
        index = 0
        for k in apLocations:
          if (k.x >= j.xcor()-40 and k.x <= j.xcor()+40 and k.y >= j.ycor()-40 and k.y <= j.ycor()+40):
            if(wifiCond[indexJ] == 1):
                numNodesAP[index] = numNodesAP[index] + 0.5
            elif(wifiCond[indexJ] == 2):
                numNodesAP[index] = numNodesAP[index] + 1
          index = index + 1
        indexJ = indexJ + 1
      setAccessPoints()
      outputData()
      
if(modelNum == 3):
    for i in range(10):
      indexJ = 0
      for l in range(40):
        numNodesAP[l] = 0
      for j in nodes:
        j.penup()
        j.speed(2000)
        moveAlongPath(j)
        index = 0
        for k in apLocations:
          if (k.x >= j.xcor()-40 and k.x <= j.xcor()+40 and k.y >= j.ycor()-40 and k.y <= j.ycor()+40):
            if(wifiCond[indexJ] == 1):
                numNodesAP[index] = numNodesAP[index] + 0.5
            elif(wifiCond[indexJ] == 2):
                numNodesAP[index] = numNodesAP[index] + 1
          index = index + 1
        indexJ = indexJ + 1
      setAccessPoints()
      outputData()


input('Press ENTER to Exit')
#circle range. 
    #y goes from ycor to ycor+80
    #x goes from xcor-40 to xcor+40
