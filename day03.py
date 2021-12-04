from utils.import_data import getFileName,getInputFromFile
from utils import submarine
from math import prod
data = getInputFromFile('data/'+getFileName(__file__)+'.input')

sub = submarine.Submarine()

# Solve Part 1
def FirstPart():
    """ Find ... """

    sub.calculateDiagnostic(data)
    return sub.gamma*sub.epsilon


# Solve Part 2
def SecondPart():
    """ Find ... """
    sub.calculateLifeSupportRating(data)
    return sub.oxygenRating*sub.co2Rating


# Output answers
print("First Puzzle Answer:\t{}\nSecond Puzzle Answer:\t{}\n".format(FirstPart(),SecondPart()))