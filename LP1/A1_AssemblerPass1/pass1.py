optab=[
['STOP',['IS,00']],
['ADD',['IS,01']],
['SUB',['IS,02']],
['MULT',['IS,03']],
['MOVER',['IS,04']],
['MOVEM',['IS,05']],
['COMP',['IS,06']],
['BC',['IS,07']],
['DIV',['IS,08']],
['READ',['IS,09']],
['PRINT',['IS,10']],
['START',['AD,01']],
['END',['AD,02']],
['ORIGIN',['AD,03']],
['EQU',['AD,04']],
['LTORG',['AD,05']],
['DC',['DL,01']],
['DS',['DL,02']]
]

regtab_cctab=[
['AREG',['1']],
['BREG',['2']],
['CREG',['3']],
['DREG',['4']],
['LT',['1']],
['LE',['2']],
['EQ',['3']],
['GT',['4']],
['GE',['5']],
['ANY',['6']]
]

class pass1:
    lc=0
    symtab=[]
    littab=[]
    pooltab=[]
    litcount=0

    def find(self,word):
        for i in range(len(optab)):
            if optab[i][0]==word:
                return optab[i][1]
        for i in range(len(regtab_cctab)):
            if regtab_cctab[i][0]==word:
                return regtab_cctab[i][1]
        for i in range(len(self.symtab)):
            if self.symtab[i][0]==word:
                return i+1
        for i in range(len(self.littab)):
            if self.littab[i][0]==word:
                return i+1

    def insert(self,a,loc):
        self.symtab[a-1][1]=loc


    def process(self):
        with open("A1_AssemblerPass1/input2.txt", "r") as file:
            data = file.readlines()
            for line in data:
                word = line.split()
                if len(word)==1:
                    if word[0]!='END' and word[0]!='LTORG':
                        print(self.lc, end=" ")
                    if word[0]!='LTORG':
                        q=self.find(word[0])
                        print(q)
                    if word[0]=='LTORG':
                        for i in range(self.litcount):
                            print(self.lc, end=" ")
                            q=self.littab[i][1]=self.lc
                            print("['DL,01'] ['C,{}']".format(self.littab[i][0]))
                            self.lc = self.lc + 1
                    self.lc = self.lc + 1
                elif len(word)==2:
                    if word[0]=='START':
                        self.lc=int(word[1])
                        q=self.find(word[0])
                        print(q,end=" ")
                        print('[\'C,{}\']'.format(word[1]))
                    elif word[0]=='END':
                        q=self.find(word[0])
                        print(q,end=" ")
                        qq=self.find(word[1])
                        print('[\'S,{}\']'.format(qq))
                        self.lc = self.lc + 1
                    elif word[0]=='ORIGIN':
                        q1=self.find(word[0])
                        if '+' in word[1]:
                            y1 = word[1].index('+')
                        else:
                            y1 = word[1].index('-')
                        q=self.find(word[1][0:y1])
                        if '+' in word[1]:
                            self.lc=(self.symtab[q-1][1])+int(word[1][y1+1::])
                        else:
                            self.lc = (self.symtab[q - 1][1]) - int(word[1][y1 + 1::])
                        print(q1,end=" ")
                        q4 = self.find(word[1][0:y1])
                        print('[\'S,{}\']{}'.format(q4,word[1][y1::]))
                elif len(word)==3:
                    if word[1]=='EQU':
                        q = self.find(word[0])
                        if q == None:
                            a = [word[0], 0]
                            self.symtab.append(a)
                        z1=self.find(word[0])
                        if '+' in word[2]:
                            y1=word[2].index('+')
                        else:
                            y1 = word[2].index('-')
                        z2=self.find(word[2][0:y1])
                        #print(z1)
                        self.symtab[z1-1][1]=(self.symtab[z2-1][1])+int(word[2][y1+1::])
                        print("*****NO IC*****")
                    elif word[1]!='DS' and word[1]!='DC':
                        print(self.lc, end=" ")
                        q=self.find(word[0])
                        if q == None:
                            a = [word[0], 0]
                            self.symtab.append(a)
                            q = self.find(word[0])
                            self.insert(q, self.lc)
                            #print('[\'S,{}\']'.format(q))
                        else:
                            print(q,end=" ")
                        qq=self.find(word[1])
                        print(qq,end=" ")
                        qqq=self.find(word[2])
                        if qqq!=None:
                            print('[\'S,{}\']'.format(qqq))
                        else:
                            if word[2][0:1]=='=':
                                self.littab.append([word[2],0])
                                q4 = self.find(word[2])
                                self.litcount=self.litcount+1
                                print('[\'L,{}\']'.format(q4))
                            else:
                                a=[word[2],0]
                                self.symtab.append(a)
                                q4=self.find(word[2])
                                print('[\'S,{}\']'.format(q4))
                        self.lc = self.lc + 1
                    else:
                        print(self.lc, end=" ")
                        if word[1]=='DS':
                            q = self.find(word[0])
                            qq = self.find(word[1])
                            if q==None:
                                a = [word[0], 0]
                                self.symtab.append(a)
                                q = self.find(word[0])
                                self.insert(q, self.lc)
                            else:
                                self.insert(q,self.lc)
                                print('[\'S,{}\']'.format(q),end=" ")
                            qq = self.find(word[1])
                            print(qq, end=" ")
                            print("['C,{}']".format(word[2]))
                            self.lc = self.lc + int(word[2])
                        else:
                            q = self.find(word[0])
                            if q==None:
                                a = [word[0], 0]
                                self.symtab.append(a)
                                q = self.find(word[0])
                                self.insert(q, self.lc)
                            else:
                                self.insert(q, self.lc)
                                print('[\'S,{}\']'.format(q), end=" ")
                            qq = self.find(word[1])
                            print(qq, end=" ")
                            print("['C,{}']".format(word[2][1:2]))
                            self.lc = self.lc + 1

                elif len(word)==4:
                    print(self.lc,end=" ")
                    a=[word[0],self.lc]
                    self.symtab.append(a)
                    q = self.find(word[1])
                    print(q, end=" ")
                    qq = self.find(word[2])
                    print(qq, end=" ")
                    qqq = self.find(word[3])
                    if qqq!=None:
                        print('[\'S,{}\']'.format(qqq))
                    else:
                        a=[word[3],00]
                        self.symtab.append(a)
                        q4 = self.find(word[3])
                        print('[\'S,{}\']'.format(q4))
                    self.lc = self.lc + 1
            print("********SYMTAB********")
            print(self.symtab)
            print("********LITTAB********")
            print(self.littab)


p1=pass1()
p1.process()




