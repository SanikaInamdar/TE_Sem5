class Bully:
    def __init__(self,total_process):
        self.total=total_process
        self.state=[True for i in range(self.total)]
    
    def up(self,pos):
        self.state[pos-1]=True
    def down(self,pos):
        self.state[pos-1]=False
    
    def Election(self,pos):

        if(pos>self.total):
            return
        if(self.state[pos-1]==False):
            print(f"Election cannot be started by {pos} as it is down")
            return
        print(f"Election started by: p{pos}")
        for i in range(pos,self.total):
            print(f"Election message sent from p{pos} to p{i+1}")

        for i in range(pos, self.total):
            if self.state[i]==True:
                print(f"p{i+1} responds OK to p{pos}")
        
        for i in range(pos, self.total):
            if self.state[i]==True:
                self.Election(i+1)
                return

        max_process=max(i for i, val in enumerate(self.state) if val== True)
        print(f"Election is won by: p{max_process+1}")
        print(f"p{max_process+1} inform everyone that it is the new coordinator")

class Ring:
    def __init__(self,total_process):
        self.total=total_process
        





obj=Bully(8)
obj.down(6)
obj.down(8)

obj.Election(4)