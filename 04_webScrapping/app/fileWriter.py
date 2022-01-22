# File Writer
def writeInfo(fileName: str, info: str):
    file = open(fileName, 'w')
    file.write(info)
    file.close()