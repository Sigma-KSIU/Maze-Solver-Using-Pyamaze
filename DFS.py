from pyamaze import maze, COLOR, agent,textLabel
def DFS(m1):
    start=(m1.rows,m1.cols)
    explored=[start]
    frontier=[start]
    dfsPath={}
    while len(frontier)>0:
        currCell=frontier.pop()
        if currCell==(1,1):
            break
        for d in 'ESNW':
            if m1.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if childCell in explored:
                    continue
                explored.append(childCell)
                frontier.append(childCell)
                dfsPath[childCell]=currCell
    fwdPath={}
    cell=(1,1)
    while cell!=start:
        fwdPath[dfsPath[cell]]=cell
        cell=dfsPath[cell]
    return fwdPath
m1=maze()
m1.CreateMaze()
path=DFS(m1)
a= agent(m1,shape='arrow',color='red',footprints=True)
m1.tracePath({a:path},delay=150)
l1=textLabel(m1,'Length of Shortest Path',len(path)+1)
m1.run()