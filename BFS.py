from pyamaze import maze, COLOR, agent,textLabel
def BFS(m2):
    start=(m2.rows,m2.cols)
    frontier=[start]
    explored=[start]
    bfsPath={}
    while len(frontier)>0:
        currCell=frontier.pop(0)
        if currCell==(1,1):
            break
        for d in 'ESNW':
            if m2.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                if childCell in explored:
                    continue
                frontier.append(childCell)
                explored.append(childCell)
                bfsPath[childCell]=currCell
    fwdPath={}
    cell=(1,1)
    while cell!=start:
        fwdPath[bfsPath[cell]]=cell
        cell=bfsPath[cell]
    return fwdPath

if __name__=='__main__':
    m2=maze()
    m2.CreateMaze()
    path=BFS(m2)
    b=agent(m2,footprints=True,filled=True,shape='arrow')
    m2.tracePath({b:path},delay=150)
    l2=textLabel(m2,'Length of Shortest Path',len(path)+1)
    m2.run()