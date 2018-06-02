import turtle
import random
import win32api

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

# Creates all test cases
generateTests()

# Screen property
windowScreen = turtle.Screen()
windowScreen.title("Fitts Law Test")
window = turtle.Screen()
window.screensize()
window.setup(width=1.0, height=1.0)

# set Turtle
drawTurtle = turtle.Turtle()
drawTurtle.hideturtle()

pointerTurtle = turtle.Turtle()
pointerTurtle.left(125)
pointerTurtle.shapesize()


# This function draw blue circle based on radius
def drawCircle(tut, rad):
    tut.color("blue", "blue")
    tut.begin_fill()
    tut.circle(rad)
    tut.end_fill()

def drawRectangle(tut, x, y, width, height):
    tut.up()
    tut.goto(x, y)
    tut.down()
    tut.forward(width)          
    tut.left(90)
    tut.forward(height)
    tut.left(90)
    tut.forward(width)
    tut.left(90)
    tut.forward(height)
    tut.left(90)
    tut.up()

# This function draw circle at a distance based on distance list
def createCircle(tur):
    tur.clear()
    
    # Get a circle to test and translates it to pixels values
    circle = getCircle()
    dimensions = {'small': 12.5, 'medium': 25, 'large': 50, 'short': 250, 'long': 500, 'right': 1, 'left': -1}
    radius = dimensions[circle[0]]
    distance = dimensions[circle[1]]
    direction = dimensions[circle[2]]
    
    #distance = [-500, -250, -100, 100, 250, 500]
    #radius = [12.5, 25, 50]
    
    tur.penup()
    tur.setx(distance * direction)
    tur.pendown()
    drawCircle(tur, radius)


# Glow the circle -- Not working
def glowCircle():
    drawTurtle.fillcolor("red")


def unglowCircle(tut):
    tut.fillcolor("blue")

def handler_goto(x, y):
    pointerTurtle.penup()
    pointerTurtle.goto(x, y)
    pointerTurtle.goto(0, 0)
    
    # Creates a recursive function calling itself until all test cases are complete
    if len(circleTestBlocks) != 0:
        resetCursor()
        createCircle(drawTurtle)
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
        
# Makes a consent warning screen
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
    drawRectangle(drawTurtle, -50, -85, 100, 25)
    drawTurtle.setpos(-18, -85)
    drawTurtle.write("I Agree", font=("Arial", 10, "bold"))
    drawTurtle.setpos(0, 0)
    

consentScreen()
windowScreen.onclick(handler_goto)

# Does not work
# drawTurtle.onclick(glowCircle())


turtle.done()
