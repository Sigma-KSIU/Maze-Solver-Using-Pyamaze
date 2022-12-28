from pyamaze import maze, COLOR, agent,textLabel
from queue import PriorityQueue
def h(cell1,cell2):
    x1,y1=cell1
    x2,y2=cell2
    return abs(x1-x2)+abs(y1-y2)
def aStar(m3):
    start=(m3.rows,m3.cols)
    g_score={cell:float('inf') for cell in m3.grid}
    g_score[start]=0
    f_score={cell:float('inf') for cell in m3.grid} 
    f_score[start]=h(start,(1,1))
    open=PriorityQueue()
    open.put((h(start,(1,1)),h(start,(1,1)),start))
    aPath={}
    while not open.empty():
        currCell=open.get()[2]
        if currCell==(1,1):
            break
        for d in 'ESNW':
           if m3.maze_map[currCell][d]==True:
             if d=='E':
                childCell=(currCell[0],currCell[1]+1)
             if d=='W':
                childCell=(currCell[0],currCell[1]-1)
             if d=='N':
                childCell=(currCell[0]-1,currCell[1])
             if d=='S':
                childCell=(currCell[0]+1,currCell[1])
             temp_g_score=g_score[currCell]+1
             temp_f_score=temp_g_score+h(childCell,(1,1))
             if temp_f_score < f_score[childCell]:
                g_score[childCell]=temp_g_score
                f_score[childCell]=temp_f_score
                open.put((temp_f_score,h(childCell,(1,1)),childCell))
                aPath[childCell]=currCell
    fwdPath={}
    cell=(1,1)
    while cell!=start:
        fwdPath[aPath[cell]]=cell
        cell=aPath[cell]
    return fwdPath
m3=maze()
m3.CreateMaze()
path=aStar(m3)
c=agent(m3,footprints=True,shape='arrow',color='yellow')
m3.tracePath({c:path},delay=150)
l3=textLabel(m3,"A Star Path Length",len(path)+1)
m3.run()