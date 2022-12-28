from pyamaze import maze, COLOR, agent,textLabel
#Depth first search
def DFS(m1):                   #DFS() is a function that takes the maze_map as an argument and returns a dictionary that maps the parent cell to the child cell. 
    start=(m1.rows,m1.cols)    #defined the start cell as the bottom right corner of the maze.
    explored=[start]           #defined the explored list to store the cells that we have explored.
    frontier=[start]           #defined the frontier list to store the cells that we have not explored.
    dfsPath={}                 #defined the dfsPath dictionary to store the parent cell of a cell as the key and the child cell as the value. The parent cell is the cell that we explored and the child cell is the cell that we have not explored.
    while len(frontier)>0:      #defined a while loop that will stop when the frontier list is empty or when the current cell is equal to the start cell.
        currCell=frontier.pop()   #set the current cell to the last element of the frontier list.
        if currCell==(1,1):        #check if the current cell is the start cell. If it is, then we break out of the loop.
            break                     
        for d in 'ESNW':          #defined a for loop that will loop through the four directions, which are East, South, West, and North.
            if m1.maze_map[currCell][d]==True:     #check if the current cell has a wall in a certain direction. If it does not, then we continue to the next line.
                if d=='E':         #check if the direction is East. If it is, then we define the child cell as the cell to the right of the current cell.
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':       #check if the direction is West. If it is, then we define the child cell as the cell to the left of the current cell.
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='S':        #check if the direction is South. If it is, then we define the child cell as the cell below the current cell.
                    childCell=(currCell[0]+1,currCell[1])
                elif d=='N':         #check if the direction is North. If it is, then we define the child cell as the cell above the current cell.
                    childCell=(currCell[0]-1,currCell[1])
                if childCell in explored:          #check if the child cell is in the explored list. If it is, then we continue to the next line.
                    continue
                explored.append(childCell)           #append the child cell to the explored list.
                frontier.append(childCell)           #append the child cell to the frontier list.
                dfsPath[childCell]=currCell          #set the child cell as the value of the dfsPath dictionary and the current cell as the key.
    fwdPath={}                      #set the fwdPath dictionary to an empty dictionary.
    cell=(1,1)                        #set the cell variable to (1,1).
    while cell!=start:                  #defined a while loop that will stop when the cell is equal to the start cell.
        fwdPath[dfsPath[cell]]=cell     #set the child cell as the value of the fwdPath dictionary and the parent cell as the key.
        cell=dfsPath[cell]              #set the cell as the parent cell.
    return fwdPath                      #return the fwdPath dictionary.

#Breadth first search
def BFS(m2):                      #The function BFS takes a maze as input and returns the path from the starting cell to the exit cell.
    start=(m2.rows,m2.cols)       #The start is the exit cell.
    frontier=[start]              #The frontier is initially set to the start cell.
    explored=[start]              #The explored list is initially set to the start cell.
    bfsPath={}                    #The bfsPath is a dictionary that stores the path from the start cell to the exit cell.
    while len(frontier)>0:        #The while loop runs as long as there are unexplored cells in the frontier.
        currCell=frontier.pop(0)    #The currCell is the first cell in the frontier.
        if currCell==(1,1):         #The if statement checks if the currCell is the exit cell.
            break 
        for d in 'ESNW':            #If the currCell is not the exit cell, the for loop runs through the directions 'ESNW'.
            if m2.maze_map[currCell][d]==True:     #The if statement checks if the current cell has a wall in the direction d. 
                if d=='E':                         #If the current cell has a wall, then the if statement checks if the direction is 'E' and the childCell is set to the cell to the right of the current cell.
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':                       #Or if the direction is 'W' and the childCell is set to the cell to the left of the current cell.
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='N':                       #Or if the direction is 'N' and the childCell is set to the cell above the current cell.
                    childCell=(currCell[0]-1,currCell[1])
                elif d=='S':                       #Or if the direction is 'S' and the childCell is set to the cell below the current cell.
                    childCell=(currCell[0]+1,currCell[1])
                if childCell in explored:            #The if statement checks if the childCell is already in the explored set.
                    continue                            #If the childCell is in the explored set, then the program continues to the next direction.
                frontier.append(childCell)            #If the childCell is not in the explored set, then the childCell is appended to the frontier.
                explored.append(childCell)            #The childCell is also appended to the explored set.
                bfsPath[childCell]=currCell            #The bfsPath dictionary is updated with the childCell as the key and the currCell as the value.
    fwdPath={}                                    #The fwdPath dictionary is created.
    cell=(1,1)                                    #The cell variable is set to the exit cell.
    while cell!=start:                            #The while loop runs as long as the cell is not the starting cell.
        fwdPath[bfsPath[cell]]=cell                 #The fwdPath dictionary is updated with the bfsPath dictionary with the cell as the key.
        cell=bfsPath[cell]                        #The cell variable is updated to the value of the bfsPath dictionary with the cell as the key.
    return fwdPath                                #The fwdPath dictionary is returned.                             
# A-star search
from queue import PriorityQueue            #import PriorityQueue class from the queue module.
def h(cell1,cell2):                        #define the heuristic function to be the Manhattan distance between the current cell and the goal cell (1,1).
    x1,y1=cell1
    x2,y2=cell2
    return abs(x1-x2)+abs(y1-y2)
def aStar(m3):
    start=(m3.rows,m3.cols)
    g_score={cell:float('inf') for cell in m3.grid}
    g_score[start]=0                      #start by initializing the g_score and f_score dictionaries. 
    f_score={cell:float('inf') for cell in m3.grid}                                            #The g_score dictionary stores the cost of the best path from the start cell to the current cell. 
    f_score[start]=h(start,(1,1))                                              # The f_score dictionary stores the cost of the best path from the start cell to the goal cell through the current cell. 
                                                    # The initial cost of the best path from the start cell to the start cell is 0.
                                                     # the initial cost of the best path from the start cell to the goal cell through the start cell is the heuristic cost which is the Manhattan distance between the start cell and the goal cell.
    open=PriorityQueue()                            #initialize the open set which is a priority queue to store the cells that are to be explored during the search. The priority of a cell in the open set is its f_score value.
    open.put((h(start,(1,1)),h(start,(1,1)),start))
    aPath={}                              #initialize the aPath dictionary to store the path from the start cell to the goal cell.
    while not open.empty():               #The code first checks the top of the open list.
        currCell=open.get()[2]
        if currCell==(1,1):
            break                         #If the top is the goal cell, the loop is broken.
        for d in 'ESNW':                  #If the top is not the goal cell, then the four directions are checked for walls. 
           if m3.maze_map[currCell][d]==True:                         
             if d=='E':
                childCell=(currCell[0],currCell[1]+1)         
             if d=='W':
                childCell=(currCell[0],currCell[1]-1)
             if d=='N':
                childCell=(currCell[0]-1,currCell[1])
             if d=='S':
                childCell=(currCell[0]+1,currCell[1])          #The child cell is then checked to see if it is in the open list.
             temp_g_score=g_score[currCell]+1                  #If it is in the open list, the g_score is calculated.
             temp_f_score=temp_g_score+h(childCell,(1,1))      #Then the f_score is calculated.
             if temp_f_score < f_score[childCell]:            #If the f_score is less than the current f_score for the child cell, then the g_score and f_score are updated.      
                g_score[childCell]=temp_g_score           
                f_score[childCell]=temp_f_score 
                open.put((temp_f_score,h(childCell,(1,1)),childCell))     #The child cell is added to the open list.
                aPath[childCell]=currCell             #The parent of the child cell is set to the current cell.
    fwdPath={}                                        #The current cell is then set to the next cell on the open list.
    cell=(1,1)                                       #The path is then traced back from the goal cell to the start cell.
    while cell!=start:                                #The path is then traced back from the goal cell to the start cell.
        fwdPath[aPath[cell]]=cell                     #The path is returned.
        cell=aPath[cell]
    return fwdPath                 


#uniform cost search.
def UCS(m,*h,start=None):
    if start is None:       #first check if the start point is given or not. If not given, then we set the start point to (m4.rows,m4.cols)
        start=(m.rows,m.cols)

    hurdles=[(i.position,i.cost) for i in h]          #then store the hurdles in a list of tuples, where the first element of the tuple is the position of the hurdle and the second element is the cost of the hurdle.

    unvisited={n:float('inf') for n in m.grid}        #then create two dictionaries, unvisited and visited. #The dictionary unvisited will keep track of the cells that are yet to be visited and the dictionary visited will keep track of the cells that have already been visited. The value associated with each cell in the dictionary unvisited is the distance from the start point to the cell. The value associated with each cell in the dictionary visited is the distance from the start point to the cell.
    unvisited[start]=0
    visited={}
    revPath={}
    while unvisited:                                     #then loop through the unvisited dictionary until it is empty.
        currCell=min(unvisited,key=unvisited.get)     #The current cell is the cell with the least distance from the start point. We then add the current cell to the visited dictionary and remove it from the unvisited dictionary.
        visited[currCell]=unvisited[currCell]
        if currCell==m._goal:               #then check if the current cell is the goal cell. If it is, we break out of the loop.
            break
        for d in 'EWNS':                    #If it is not, then we loop through the list of directions.
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if childCell in visited:                  #then check if the next cell is in the visited dictionary. If it is, we continue to the next direction.
                    continue
                tempDist= unvisited[currCell]+1            #then calculate the distance from the start point to the next cell.
                for hurdle in hurdles:                     #then loop through the hurdles list and check if the current cell is a hurdle. If it is, we add the cost of the hurdle to the distance from the start point to the next cell.
                    if hurdle[0]==currCell:
                        tempDist+=hurdle[1]

                if tempDist < unvisited[childCell]:         #then check if the distance from the start point to the next cell is less than the distance from the start point to the next cell in the unvisited dictionary. If it is, we update the distance from the start point to the next cell in the unvisited dictionary.
                    unvisited[childCell]=tempDist
                    revPath[childCell]=currCell            #then update the revPath dictionary with the current cell as the key and the next cell as the value.
        unvisited.pop(currCell)                             #then remove the next cell from the unvisited dictionary.
    fwdPath={}
    cell=m._goal
    while cell!=start:
        fwdPath[revPath[cell]]=cell
        cell=revPath[cell]
    
    return fwdPath,visited[m._goal]        #then return the revPath dictionary and the distance from the start point to the goal cell
            
            
from timeit import timeit
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
class MazeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Maze GUI")
        self.master.geometry("700x500")
        self.master.resizable(True, True)
        self.master.configure(background='white')
        self.create_widgets()
        self.master.mainloop()

    def create_widgets(self):
        self.frame = tk.Frame(self.master, bg='black')
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.label1 = tk.Label(self.frame, text="Choose Type of Search", bg='black', fg='white', font=('Helvetica', 20))
        self.label1.place(x=200,y=50)
        self.button1 = tk.Button(self.frame, text="Breadth First Search", command=self.bfs,bg='#0278c2',width=50,height=2)
        self.button1.place(x=200,y=100)
        self.button2 = tk.Button(self.frame, text="A-Star Search", command=self.aStar,bg='#c2bb02',width=50,height=2)
        self.button2.place(x=200,y=200)
        self.button3 = tk.Button(self.frame, text="Uniform Cost Search", command=self.UCS,bg='#02bfc2',width=50,height=2)
        self.button3.place(x=200,y=300)
        self.button4 = tk.Button(self.frame, text="Depth First Search", command=self.dfs,bg='#c20202',width=50,height=2) 
        self.button4.place(x=200,y=400)
        self.button5 = tk.Button(self.frame, text="Exit", command=self.exit,width=10)
        self.button5.place(x=0,y=0)

    def bfs(self):
        self.master.destroy()
        m2=maze()
        m2.CreateMaze()
        path=BFS(m2)
        b=agent(m2,footprints=True,filled=True,shape='arrow')
        m2.tracePath({b:path},delay=150)
        l2=textLabel(m2,'Length of Shortest Path',len(path)+1)
        m2.mainloop()
    def aStar(self):
        self.master.destroy()
        m3=maze()
        m3.CreateMaze()
        path=aStar(m3)
        c=agent(m3,footprints=True,shape='arrow',color='yellow')
        m3.tracePath({c:path},delay=150)
        l3=textLabel(m3,"A Star Path Length",len(path)+1)
        m3.mainloop()
    def UCS(self):
       self.master.destroy()
       m4=maze()
       m4.CreateMaze()
       path,c=UCS(m4)
       textLabel(m4,'Total Cost',c)
       a=agent(m4,color=COLOR.cyan,filled=True,footprints=True,shape='arrow')
       m4.tracePath({a:path},delay=150)
       m4.run()
       m4.mainloop()
    def dfs(self):
        self.master.destroy()
        m1=maze()
        m1.CreateMaze()
        path=DFS(m1)
        a=agent(m1,footprints=True,shape='arrow',color='red')
        m1.tracePath({a:path},delay=150)
        l1=textLabel(m1,'Length of Shortest Path',len(path)+1)
        m1.mainloop()
    def exit(self):
        self.master.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    app = MazeGUI(root)


