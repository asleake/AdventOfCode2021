from os.path import basename

def getInputFromFile(file):
    """Open and return the data in the input file"""
    f = open(file)
    data = f.readlines()
    f.close()
    return [line.strip() for line in data]

def getFileName(file_to_find):
    """Get the filename of the file input"""
    return basename(file_to_find).split('.')[0]