from collections import defaultdict
import os
import json

JSONFILE = "data.json"

class Node:
    
    def __init__(self, nome, username, id):
        self.id = id
        self.nome = nome
        self.username = username
        self.next = None


class Graph:
    
    def __init__(self):
        self.graph = defaultdict

    def insertNode(self, nome, username, id):
        self.node = Node(nome, username, id)

    def addEdge(self, node1, node2):
        node1.next = node2
        self.graph.append(node2)

    def BSF(self):
        pass
        
    def writeFile(self):
        if not os.path.exists(JSONFILE):
            jsonDict = {}

            with open(JSONFILE, 'w') as outfile:
                json.dump(jsonDict, outfile)
            
        else:
            with open(JSONFILE) as file:
                jsonDict = json.load(file)

            with open(JSONFILE, 'w') as outfile:
                json.dump(jsonDict, outfile)


'''
if not os.path.exists(JSONFILE):
    jsonDict = {}
    jsonDict["dados"] = []
    jsonDict["mmq"] = []

    with open(JSONFILE, 'w') as outfile:
        json.dump(jsonDict, outfile)
    
else:
    with open(JSONFILE) as file:
        jsonDict = json.load(file)

    with open(JSONFILE, 'w') as outfile:
        json.dump(jsonDict, outfile)




        
        ///////////////////////////////////////////
from collections import defaultdict
class Graph:
 
    def __init__(self):
        self.graph = defaultdict(list)
 
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    def BFS(self, s):
        visited = [False] * (max(self.graph) + 1)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print (s, end = " ")
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
'''