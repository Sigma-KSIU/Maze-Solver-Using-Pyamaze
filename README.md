# Maze-Solver-Using-Pyamaze
This is project is about solving random 10*10 mazes with 4 Types of Search,notice you have to install pyamaze library first before using code (pip install pyamaze)


![WhatsApp Image 2022-12-28 at 23 48 52](https://user-images.githubusercontent.com/94708469/209875795-924b42e7-a50f-48e5-9c95-34f1f569929c.jpg)


## 1-Breadth First Search 
Breadth-first search (BFS) is a graph traversal algorithm that starts traversing the graph from the root node and explores all the neighboring nodes. Then, it selects the nearest node and explores all the unexplored nodes. 

The Breadth first search is likely similar to the Depth first search but on BFS the Frontier was Queue (FIFO) so when the element is popped from the Frontier it will be popped from the beginning of the list unlike in DFS the frontier pops from the last element of the list. It’s order is (E -> S -> N -> W)


![image](https://user-images.githubusercontent.com/94708469/209873939-762d0a7f-87b2-4486-9dfb-955bc1185667.png)
![image](https://user-images.githubusercontent.com/94708469/209873962-639ef397-6983-46e7-ab51-efef47d08c54.png)


## 2-Depth First Search
The depth-first search (DFS) is an algorithm starts with the initial node of graph G and goes deeper until we find the goal node or the node with no children.

DFS the Frontier was Stack (LIFO) so when the element is popped from the Frontier it will be popped from the end of the list unlike in BFS the frontier pops from the first  element of the list. it’s order is (W -> N -> S-> E)​.
![image](https://user-images.githubusercontent.com/94708469/209875167-aa90be59-3065-4ac7-9efc-4a50262971d9.png)
![image](https://user-images.githubusercontent.com/94708469/209875178-babb95ff-32d8-4140-a76e-70e65820c3c0.png)


## 3-A-Star Search
A* Search Algorithm is a simple and efficient search algorithm that can be used to find the optimal path between two nodes in a graph. It will be used for the shortest path finding.
Search algorithm that expands node with lowest value of g(n) +  h(n).
g(n) = cost to reach node
h(n) = estimated cost to goal
![image](https://user-images.githubusercontent.com/94708469/209875270-64086aee-cd14-4d0a-b020-8e3a3985189b.png)


## 4-Uniform Cost Search
The Uniform-cost search is an uninformed search algorithm that uses the lowest cumulative cost to find a path from the source to the destination.
We use Uniform Cost Search to find the goal and the path including the cumulative cost to expand each node from the root node to the goal node.
The path will be : S -> A-> D-> G

![WhatsApp Image 2022-12-28 at 23 51 24](https://user-images.githubusercontent.com/94708469/209875970-46f8a547-c33b-49ef-9870-3cbc79e86adc.jpg)


