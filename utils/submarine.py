class Submarine():
    def __init__(self):
        self.x = 0
        self.depth = 0
        self.aim = 0
        

    def trackPosition(self,commands):
        x,depth = 0,0
        for command in commands:
            direction,distance = command.split()
            self.aim -= (direction=='up')*int(distance)
            self.aim += (direction=='down')*int(distance)
            self.x += (direction=='forward')*int(distance)
            self.depth += (direction=='forward')*int(distance)*self.aim
        
    def getPosition(self):
        return (self.x,self.depth,self.aim)


def trackPosition(commands):
    x,depth = 0,0
    for command in commands:
        direction,distance = command.split()
        x += (direction=='forward')*int(distance)
        depth -= (direction=='up')*int(distance)
        depth += (direction=='down')*int(distance)
    return x,depth


def trackCorrectPosition(commands):
    x,depth,aim = 0,0,0
    for command in commands:
        direction,distance = command.split()
        aim -= (direction=='up')*int(distance)
        aim += (direction=='down')*int(distance)
        x += (direction=='forward')*int(distance)
        depth += (direction=='forward')*int(distance)*aim
    return x,depth