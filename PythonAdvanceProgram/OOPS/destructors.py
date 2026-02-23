# destructors - when we want to destroy the object
# destructors are used for post conditions - closing of the browser, db connection closing, releasing of certain resources
#clean up operations
# for proper memory usage des shld be used
# when db connection has to be closed
# free the memory (garbage collection ) which is automatically called

class Dest:
    def __init__(self):
        print("Obj created")


    def __del__(self):
        print("Closing the db connection")

a = Dest()
print("end of program")
del a
# dest in file handling

class FileHandler:
    def __init__(self,filename):
        self.file = open(filename , 'w')
        print("File is opened")

    def readfile(self,filename):
        print("File reading")

    def __del__(self):
        self.file.close()
        print("File closed")

f = FileHandler("test.txt")
f.readfile("test.txt")
del f


