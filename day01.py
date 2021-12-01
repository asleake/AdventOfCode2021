from utils.import_data import getFileName,getInputFromFile
from utils import sonar

data = getInputFromFile('data/'+getFileName(__file__)+'.input')



# Solve Part 1
part1 = sonar.measureIncreasingDepth([int(depth) for depth in data],1)


# Solve Part 2
part2 = sonar.measureIncreasingDepth([int(depth) for depth in data],3)


# Output answers
print('Part 1:\n'+str(part1))
print('\n\n')
print('Part 2:\n'+str(part2))