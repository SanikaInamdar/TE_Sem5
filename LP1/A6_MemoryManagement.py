class memoryAllocation:    
    def firstFit(self,blockSize,processSize):
        allocated=[]
        for i in processSize:
            try:
                res = next(x for x, val in enumerate(blockSize) if val > i)
                allocated.append(res+1)
                blockSize[res]=blockSize[res]-i
            except:
                allocated.append("Not Allocated")
        print(allocated)

    def nextFit(self, blockSize, processSize):
        allocation = []
        allocation_id = 0
        for i in range(len(processSize)):
            # Loop(start, end)
            for j in range(allocation_id, len(blockSize)):
                if blockSize[j] >= processSize[i]:
                    allocation.append(j+1)
                    blockSize[j] -= processSize[i]
                    allocation_id = j
                    break
                else:
                    allocation.append("Not Allocated")
        print(allocation)

    def worstFit(self,blockSize,processSize):
        allocation=[]
        for i in processSize:
            result=max(blockSize)
            if result>i:
                a=blockSize.index(result)
                allocation.append(a+1)
                blockSize[a]=blockSize[a]-i
            else:
                allocation.append("Not Allocated")
        print(allocation)

    def bestFit(self,blockSize,processSize):
        allocated=[]
        for i in processSize:
            try:
                result= min(j for j in blockSize if j>=i)
                a=blockSize.index(result)
                allocated.append(a+1)
                blockSize[a]=blockSize[a]-i
            except:
                allocated.append("Not Allocated")
        print(blockSize)
        print(allocated)

blockSize=[]
processSize=[]
OblockSize=[]
OprocessSize=[]

# blockSize = [100, 500, 200, 300, 600]
# processSize = [212, 417, 112, 426]
print("****** MEMORY ALLOCATION ******")
m=int(input("Enter the number of blocks: "))
for i in range(0,m):
    blockSize.append(int(input("Enter the size of the block: ")))

n=int(input("Enter the number of processes: "))
for j in range(0,n):
    processSize.append(int(input("Enter the size of the process: ")))

OblockSize=blockSize.copy()
OprocessSize=processSize.copy()

obj = memoryAllocation()
while(True):
    print("1. First Fit")
    print("2. Next Fit")
    print("3. Best Fit")
    print("4. Worst Fit")
    print("5. Exit")
    ch=int(input("Enter Your Choice: "))
    if(ch==1):
        blockSize=OblockSize.copy()
        processSize=OprocessSize.copy()
        obj.firstFit(blockSize, processSize)
    elif(ch==2):
        blockSize=OblockSize.copy()
        processSize=OprocessSize.copy()
        obj.nextFit(blockSize, processSize)
    elif(ch==3):
        blockSize=OblockSize.copy()
        processSize=OprocessSize.copy()
        obj.bestFit(blockSize, processSize)
    elif(ch==4):
        blockSize=OblockSize.copy()
        processSize=OprocessSize.copy()
        obj.worstFit(blockSize, processSize)
    elif(ch==5):
        print("Thank you!")
        break   