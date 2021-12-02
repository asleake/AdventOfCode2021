from utils.import_data import getFileName,getInputFromFile
from utils import sonar

data = getInputFromFile('data/'+getFileName(__file__)+'.input')



# Solve Part 1
def FirstPart():
    """ Find which depth readings increase over the previous value """
    return sonar.measureIncreasingDepth([int(depth) for depth in data],1)


# Solve Part 2
def SecondPart():
    """ Find which depth readings increase over the previous 3 values """
    return sonar.measureIncreasingDepth([int(depth) for depth in data],3)


# Output answers
print("First Puzzle Answer:\t{}\nSecond Puzzle Answer:\t{}\n".format(FirstPart(),SecondPart()))