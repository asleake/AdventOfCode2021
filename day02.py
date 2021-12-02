from utils.import_data import getFileName,getInputFromFile
from utils import submarine
from math import prod

data = getInputFromFile('data/'+getFileName(__file__)+'.input')



# Solve Part 1
part1 = prod(submarine.trackPosition(data))


# Solve Part 2
part2 = prod(submarine.trackCorrectPosition(data))


# Output answers
print('Part 1:\n'+str(part1))
print('\n\n')
print('Part 2:\n'+str(part2))