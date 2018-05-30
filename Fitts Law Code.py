import random

testCases = []

# This function returns a randomly picked circle out of a set of 12 tests with 10 test blocks (120)
# @return (diameter, distance, direction)
def getCircle():
    circle = random.randint(0, len(testCases)-1)
    return testCases.pop(circle)

def generateTests():
    
    baseTests = [('small', 'short', 'left'), ('medium', 'short', 'left'), ('large', 'short', 'left'),
                 ('small', 'long', 'left'), ('medium', 'long', 'left'), ('large', 'long', 'left'),
                 ('small', 'short', 'right'), ('medium', 'short', 'right'), ('large', 'short', 'right'),
                 ('small', 'long', 'right'), ('medium', 'long', 'right'), ('large', 'long', 'right')]
    
    for i in range(len(baseTests)):
        for y in range(10):
            testCases.append(baseTests[i])

# Runs tests
generateTests()

for i in range(len(testCases)):
    print(getCircle())