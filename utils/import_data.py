from os.path import basename

def getInputFromFile(file):
    f = open(file)
    data = f.readlines()
    f.close()
    return [line.strip() for line in data]

def getFileName(file_to_find):
    return basename(file_to_find).split('.')[0]