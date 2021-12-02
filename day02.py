from utils.import_data import getFileName,getInputFromFile
from utils import submarine
from math import prod

data = getInputFromFile('data/'+getFileName(__file__)+'.input')



# Solve Part 1
def FirstPart():
    """ Track the position of a submarine given forward, up, and down commands """
    return prod(submarine.trackPosition(data))


# Solve Part 2
def SecondPart():
    """ Track the position of a submarine given forward and aim (up, down) commands """
    sub = submarine.Submarine()
    sub.trackPosition(data)
    return prod(sub.getPosition()[:-1]) # prod only x and depth (x,depth,aim)

    # Original part2:
    # return prod(submarine.trackCorrectPosition(data))


# Output answers
print("First Puzzle Answer:\t{}\nSecond Puzzle Answer:\t{}\n".format(FirstPart(),SecondPart()))