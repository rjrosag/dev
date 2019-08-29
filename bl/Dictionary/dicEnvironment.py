import os

class Sysenv:
    def __init__(self):
        self.PATH_REACT = "//home//rrosa//dev//gui//react//"

    def getPathReact(self):
        return (self.PATH_REACT)

    # find a file in a directory
    def find(self, name, path):
        for root, dirs, files in os.walk(path):
            if name in files:
                return os.path.join(root, name)
