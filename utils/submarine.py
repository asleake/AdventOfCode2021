def trackPosition(inputs):
    x,depth = 0,0
    for inputdata in inputs:
        direction,distance = inputdata.split()
        x += (direction=='forward')*int(distance)
        depth -= (direction=='up')*int(distance)
        depth += (direction=='down')*int(distance)
    return x,depth
        

def trackCorrectPosition(inputs):
    x,depth,aim = 0,0,0
    for inputdata in inputs:
        direction,distance = inputdata.split()
        aim -= (direction=='up')*int(distance)
        aim += (direction=='down')*int(distance)
        x += (direction=='forward')*int(distance)
        depth += (direction=='forward')*int(distance)*aim
    return x,depth