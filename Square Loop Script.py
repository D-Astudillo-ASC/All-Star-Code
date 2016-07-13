from Myro import *
init("sim")
sideLength = int(input("How long should the sides of the square be?"))
penDown()
i = 0
while i < 15:
  forward(1, sideLength)
  turnBy(-90)
  i = i + 1