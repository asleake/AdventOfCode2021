def trackPosition(inputs):
    x,y = 0,0
    for inputdata in inputs:
        direction,distance = inputdata.split()
        x += (direction=='forward')*int(distance)
        y += (direction=='up')*int(distance)
        y -= (direction=='down')*int(distance)
    return x,y
        

def trackCorrectPosition(inputs):
    x,y,aim = 0,0,0
    for inputdata in inputs:
        direction,distance = inputdata.split()
        aim += (direction=='up')*int(distance)
        aim -= (direction=='down')*int(distance)
        x += (direction=='forward')*int(distance)
        y += (direction=='forward')*int(distance)*aim
    return x,y