import json

class poofs():
    """ opens a file """
    def open(self, file):
        self.path = file
        self.file = open(self.path, 'r+')
        self.raw = self.file.read()
        self.data = json.loads(self.raw)
        self.file.close()
    """ Reads raw data from file (no decoding) """
    def rawread(self):
        return self.raw
    """ Gets a file data out of the poofs file """ 
    def getdata(self, id, type):
        if type == None:
            return self.data[id]['data']
        else:
            return self.data[id, type]

        
        
        
        
file = poofs()
file.open("/home/rhino/20 Time Project/API/Outline & Examples/File.json")
print(file.rawread())
print(file.getdata(0, None))
