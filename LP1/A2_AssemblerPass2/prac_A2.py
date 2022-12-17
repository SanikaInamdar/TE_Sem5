class A2:
    def __init__(self):
        self.symtab = []
        self.littab = []
    
    def readFiles(self):
        with open("A2_AssemblerPass2/SymTab1.txt","r") as File:
            data = File.readLines()
            for line in data:
                word = line.split()
                self.symtab.append(int(word[2][:-1]))

