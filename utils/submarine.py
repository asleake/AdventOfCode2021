from copy import deepcopy
class Submarine():
    """Class to define a submarine"""
    def __init__(self):
        self.x = 0
        self.depth = 0
        self.aim = 0
        self.gamma = 0
        self.epsilon = 0
        self.oxygenRating = 0
        self.co2Rating = 0
        

    def trackPosition(self,commands):
        """Track the position of the submarine, given that up and down control aim and forward
           moves the submarine in a direction as follows: x += distance, y+=distance*aim."""
        x,depth = 0,0
        for command in commands:
            direction,distance = command.split()
            self.aim -= (direction=='up')*int(distance)
            self.aim += (direction=='down')*int(distance)
            self.x += (direction=='forward')*int(distance)
            self.depth += (direction=='forward')*int(distance)*self.aim
        
    def getPosition(self):
        """Return the position of the submarine, including aim"""
        return (self.x,self.depth,self.aim)

    def calculateDiagnostic(self,data):
        gamma = [determineBinaryMajority(line) for line in zip(*data)]
        epsilon = [not elem for elem in gamma]

        self.gamma = binToDec(gamma)
        self.epsilon = binToDec(epsilon)

    def calculateLifeSupportRating(self,data):
        oxyData = deepcopy(data)
        co2Data = deepcopy(data)
        
        oxygenRating = calculateRating(oxyData,oxygen=True)
        co2Rating = calculateRating(co2Data,oxygen=False)
        
        self.oxygenRating = binToDec(oxygenRating)
        self.co2Rating = binToDec(co2Rating)



        

    def getLifeSupportRating(self):
        return int(self.oxygenRating,2)*int(self.co2Rating,2)

        
def calculateRating(data,oxygen=True):
    rating = []
    currentDigitIndex = 0
    while True:
        if len(data) < 2: 
            diff = len(data[0]) - len(rating)
            for i in range(diff):
                rating.append(data[0][currentDigitIndex+i]=='1')
            break
        currentDigits = list(zip(*data))[currentDigitIndex]
        binaryMajority = int(not determineBinaryMajority(currentDigits))
        if oxygen==True:
            binaryMajority = int(determineBinaryMajority(currentDigits))
        rating.append(binaryMajority==1)

        valuesToRemove = []
        for i in range(len(currentDigits)):
            if currentDigits[i] != str(binaryMajority):
                valuesToRemove.append(i)
        for index in sorted(valuesToRemove, reverse=True):
            data.pop(index)
        currentDigitIndex += 1
    return rating

def determineBinaryMajority(list):
    zeroes = list.count('0')
    ones = list.count('1')
    binaryMajority = ones>=zeroes

    return binaryMajority

def binToDec(binNum):
    decNum = 0
    for b in binNum:
        decNum = (decNum << 1) | b
    return decNum

def trackPosition(commands):
    """Track the position of the submarine, given up, down, and forward directions"""
    x,depth = 0,0
    for command in commands:
        direction,distance = command.split()
        x += (direction=='forward')*int(distance)
        depth -= (direction=='up')*int(distance)
        depth += (direction=='down')*int(distance)
    return x,depth


def trackCorrectPosition(commands):
    """Track the position of the submarine, given that up and down control aim and forward
           moves the submarine in a direction as follows: x += distance, y+=distance*aim."""
    x,depth,aim = 0,0,0
    for command in commands:
        direction,distance = command.split()
        aim -= (direction=='up')*int(distance)
        aim += (direction=='down')*int(distance)
        x += (direction=='forward')*int(distance)
        depth += (direction=='forward')*int(distance)*aim
    return x,depth