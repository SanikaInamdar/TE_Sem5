class Pass2:
    def __init__(self):
        self.symtab = []
        self.littab = []

    def readFiles(self):
        with open("A2_AssemblerPass2/SymTab1.txt", "r") as File:
            # remember indentation
            data = File.readlines()
            for line in data:   #reading every line of file
                word = line.split() #storing all words of a line splitted by space(" ")
                self.symtab.append(int(word[2][:-1]))   # appending only the word of the line that has addr stored 
                                                        # i.e the word at 2(0,1,2) index value in word list
        with open("A2_AssemblerPass2/LitTab1.txt", "r") as File:
            data = File.readlines()
            for line in data:
                word = line.split()
                self.littab.append(int(word[2][:-1]))

    def LiteralORSymbol(self, word): #after getting word like -> (L,2)/(S,3)
                                    # this function returns the addr of the literal or symbol
        index = int(word[3:-1])
        if word.find('L') != -1:
            return (self.littab[index-1])
        else:
            return (self.symtab[index-1])

    def process(self):
        with open("A2_AssemblerPass2/IC.txt", "r") as file:
            data = file.readlines()
            for line in data:
                word = line.replace("\n", "").strip().split()
                if word[0].find('AD') != -1 or word[0].find('DL,02') != -1:
                    print()
                elif word[0].find("DL,01") != -1:
                    print(f"00\t0\t{word[1][3:-1]}")
                    pass
                elif word[0].find('IS,00') != -1:
                    print("00\t0\t000")
                elif word[0].find('IS,10') != -1:
                    code = self.LiteralORSymbol(word[1])
                    print(f"10\t0\t{code}")
                elif word[0].find('IS') != -1:
                    code1 = word[0][4:6]
                    code2 = word[1][1]
                    code3 = self.LiteralORSymbol(word[2])
                    print(f"{code1}\t{code2}\t{code3}")
                else:
                    print()

            file.close()


test = Pass2()
test.readFiles()
test.process()