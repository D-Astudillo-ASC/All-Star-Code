from Myro import * 
Batman = makePicture("Batman.JPG") # Takes JPG image from Calico Folder and saves it as the variable "Batman".
show(Batman) # Shows image
Pixels=getPixels(Batman) # Returns a list of individual pixels from the image
# Variables that will be responsible for returning colors to make pixels from.
Obama_DarkBlue = makeColor(0,51,76)
Obama_Red = makeColor(217, 26, 33)
Obama_Blue = makeColor(112,150,158)
Obama_Yellow = makeColor(252, 227, 166)
# for loop will repeat the code in its body, or the conditional statements written below. 
for i in Pixels: # for every item in Pixels
    greyPixels = getGray(i) # This variable gets the gray value of every pixel in the image.
    if greyPixels>180: # if the gray value of a pixel is greaten than 180
         setColor(i, Obama_Yellow) # Changes the color of a pixel to yellow.
    elif greyPixels>120 and greyPixels<180: # if the gray value is between 120 and 180
         setColor(i, Obama_Blue) # Changes the color to blue .
    elif greyPixels>60 and greyPixels<120: # if gray value is between 60 and 120 
         setColor(i, Obama_Red) # Changes the color to red.
    else: # Otherwise
         setColor(i, Obama_DarkBlue) # Changes color to blue.
