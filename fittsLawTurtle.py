import turtle
import random
import win32api
import time

# Stores all unfinished test (120 test cases in total)
circleTestBlocks = []

# This function returns a randomly picked circle out of a set of 12 tests with 10 test blocks (120 tests)
# @return (diameter, distance, direction)
def getCircle():
    circle = random.randint(0, len(circleTestBlocks)-1)
    return circleTestBlocks.pop(circle)

# Makes 120 test from 12 base cases repeating each 10 times
def generateTests():
    circleBaseTests = [('small', 'short', 'left'), ('medium', 'short', 'left'), ('large', 'short', 'left'),
                       ('small', 'long', 'left'), ('medium', 'long', 'left'), ('large', 'long', 'left'),
                       ('small', 'short', 'right'), ('medium', 'short', 'right'), ('large', 'short', 'right'),
                       ('small', 'long', 'right'), ('medium', 'long', 'right'), ('large', 'long', 'right')]
    
    for i in range(len(circleBaseTests)):
        for y in range(10):
            circleTestBlocks.append(circleBaseTests[i])

# Translates a circles dimensions to pixel values
# @parm circleDim a tuple of dimensions values
# @return a tuple in pixel equivalents of circle
def translateCircle(circleDim):
    dimensions = {'small': 12.5, 'medium': 25, 'large': 50, 'short': 100, 'long': 250, 'right': 1, 'left': -1}
    radius = dimensions[circle[0]]
    distance = dimensions[circle[1]]
    direction = dimensions[circle[2]]
    return (radius, distance, direction)

# Sets up screen property
windowScreen = turtle.Screen()
windowScreen.title("Fitts Law Test")
window = turtle.Screen()
window.screensize()
window.setup(width=1.0, height=1.0)

# Sets up Turtles
drawTurtle = turtle.Turtle()
drawTurtle.hideturtle()
drawTurtle.speed(0)

# pointerTurtle = turtle.Turtle()
# pointerTurtle.left(125)
# pointerTurtle.shapesize()

progressTurtle = turtle.Turtle()
progressTurtle.hideturtle()
progressTurtle.penup()
progressTurtle.setpos(0,-250)


# This function draw blue circle based on radius
def drawCircle(tur, rad):
    tur.color("blue", "blue")
    tur.begin_fill()
    tur.circle(rad)
    tur.end_fill()

# This function draw a rectangle on screen based on given values
def drawRectangle(tur, x, y, width, height):
    tur.up()
    tur.goto(x, y)
    tur.pendown()
    tur.forward(width)          
    tur.left(90)
    tur.forward(height)
    tur.left(90)
    tur.forward(width)
    tur.left(90)
    tur.forward(height)
    tur.left(90)
    tur.penup()

# This function draw circle at a distance based on distance list
# @parm tur the turtle that draws
# @parm circlePix a tuple of pixel valuse
def createCircle(tur, circlePix):
    tur.clear()
    
    # Old code
    # distance = [-500, -250, -100, 100, 250, 500]
    # radius = [12.5, 25, 50]
    
    tur.penup()
    tur.setx(circlePix[1] * circlePix[2])
    tur.pendown()
    drawCircle(tur, circlePix[0])


# Glow the circle -- Not working
def glowCircle(tur):
    tur.fillcolor("red")


def unglowCircle(tur):
    tur.fillcolor("blue")

def handler_goto(x, y):
    # pointerTurtle.penup()
    # pointerTurtle.goto(x, y)
    # pointerTurtle.goto(0, 0)
    
    # Gives feedback to users with tracked progress
    testsLeft = len(circleTestBlocks)
    progressTurtle.clear()
    progressTurtle.write("Test left: " + str(testsLeft), font=("Arial", 12, "normal"), align="center")
    
    # Creates a recursive function calling itself until all test cases are complete
    if testsLeft > 0:
        resetCursor()
            
        # Get a circle to test and translates it to pixel values
        circleDim = getCircle()
        circlePix = translateCircle(circleDim)
        
        # Draws the circle and finds clicked position
        createCircle(drawTurtle, circlePix)
        windowScreen.onclick(handler_goto)
    else:
        endScreen()
    
# Resets cursor to the center of the screen
def resetCursor():
    halfScreenWidth = int(round(win32api.GetSystemMetrics(0)/2))
    halfScreenHight = int(round(win32api.GetSystemMetrics(1)/2))
    win32api.SetCursorPos((halfScreenWidth,halfScreenHight))

# Clears window at the end and displays a thank you
def endScreen():
        drawTurtle.clear()
        turtle.write("Thank you", font=("Arial", 30, "normal"), align="center")
        
# Makes a consent screen
def consentScreen():
    # Title
    drawTurtle.up()
    drawTurtle.setpos(0, 250)
    drawTurtle.write("Consent", font=("Arial", 30, "bold"), align="center")
    drawTurtle.setpos(0, 0)
    
    # Body 
    drawTurtle.write("You have been chose to participate in a research study at Minnesota State University, Mankato." + 
    "\nThe purpose of this study is to examine users’ abilities to point and click on random circles shown on a screen." +
    "\nParticipating in this study is voluntary. You can decide to stop at any time. To withdraw from the study," +
    "\nyou can close the window before finishing. Results of the study will include only people willing to participate." +
    "\nIf you have any questions, you may ask the Levi or Shankar." +
    "\n\nThe responses will be anonymous. There are no direct benefits for participation. The study will include at least 15" +
    "\nother individuals and should take about 30 minutes per person to complete." +
    "\n\nIf you agree to participate in the study and are at least 18 years of age, click anywhere to begin." +
    "\n", font=("Arial", 11, "normal"), align="center")
    
    # Agreement box
    drawRectangle(drawTurtle, -54, -85, 100, 25)
    drawTurtle.setpos(0, -82)
    drawTurtle.write("I Agree", font=("Arial", 10, "bold"), align="center")
    drawTurtle.setpos(0, 0)
    

# Creates all test cases
generateTests()

# Starts running the program
consentScreen()
windowScreen.onclick(handler_goto)

# Does not work
# drawTurtle.onclick(glowCircle())

turtle.done()
