import sys  # for infinity
import math # for rounding


class Graph:        #graph class
    def __init__(self,V,E):  #make empty graph
        self.V=V;
        self.E=E;
        self.graph=[[0 for col in range (V)] for row in range (V)];
        #print(self.graph);

    def max_cap_node(self, cap, sptset):    #return not visited max capacity
      max = -sys.maxsize;

      for i in range(self.V):
        if(cap[i] > max and sptset[i] == False):
          max = cap[i];
          max_index = i;
      return max_index;

    def make_Edge(self,edge):   #make an edge
        if(edge[0] == edge[1]):
            print("Same vertex:");  #same node to same node not allowed 
        self.graph[int(edge[0])-1][int(edge[1])-1] = int(edge[2]);
        self.graph[int(edge[1])-1][int(edge[0])-1] = int(edge[2]);

    def max_min_capacity(self,src,des):
        capacity = [-sys.maxsize] * self.V; #Array for capacities
        capacity[src] = sys.maxsize;        #maximum capacity for source
        sptset  = [False] * self.V;         #Mark visited vertex
        prev = [];

        for i in range(self.V):
          max_cap_node = self.max_cap_node(capacity, sptset);
          sptset[max_cap_node] = True; #node is marked as visited

          for j in range (self.V):
            if self.graph[max_cap_node][j] > 0:
              new_cap = min(capacity[max_cap_node], self.graph[max_cap_node][j]);
              if new_cap > capacity[j]:
                capacity[j]=new_cap;
                if str(max_cap_node+1) not in prev:
                  prev.append(str(max_cap_node+1));
        return capacity[des] , prev;  

    def path(self,src,des,NoS, members):
      NoStudent_max = self.max_min_capacity(src, des) [0]; #find the maximum passengers
      if(NoStudent_max == members):
        print("No solution, reduce No. of members ");

      min_trips = math.ceil(NoS / (NoStudent_max - members));
      h = "-> ";
      path_to_des = h.join(self.max_min_capacity(src, des)[1]) + h + str(des+1);
      print(f"\nNumber of trips {min_trips} \n");
      print(f"\nNumber of passengers {NoStudent_max} \n");
      print(f"Best path is {path_to_des}");









#main code
Frn_stu = input("Enter the number of foreign students: ");              #take input for foreign student
Member_stu = input("Enter the number of AIESEC students : ");             #take input for AIESEC students
N,R = input("Enter no. of cities & no. of road segments : ").split();    #N = cities R = road segments

Frn_stu = int(Frn_stu);
Member_stu = int(Member_stu);
N = int(N);             #nodes
R = int(R);             #edges

G = Graph(N,R);         #make empty graph

for i in range (R):     #Enter edges
    edge = [];
    print(i);
    edge = input("#city 1 #city 2 #capasity : ").split();
    G.make_Edge(edge);

src, des, NoS  = input("#source #destination #number of tourists: ").split();
src = int(src)-1;
des = int(des)-1;
NoS = int(NoS);
G.path(src,des,NoS,Member_stu);
#print(G.graph);
