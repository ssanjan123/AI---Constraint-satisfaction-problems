##from utils import argmin_random_tie, count, first
##mport search

import random


colors = (0,1,2,3,4)
def getNodes():
    f = open("state_neighbours.txt")
    return len(f.readlines())
    

# Creates an adjacency matrix representing all the States
    #AB BC MB NB NL NS NT NU ON.......
# AB  
# BC  
# MB  
# NB  
# NL  
# NS  
# NT  
# NU  
# ON  
#...
def AdjacencyMatrix(AllStates):

    n = getNodes() ##nodes of the graph (64 states)
    graph = []
    for obj1 in AllStates:
        vertex = []
        for obj2 in AllStates:
            if obj2.stateName in obj1.adjacentStates:
                vertex.append(1)
            else:
                vertex.append(0)    
        graph.append(vertex)
    for i in range(n):
        for j in range(0, i):
            graph[i][j] = graph[j][i]
    for i in range(n):
        graph[i][i] = 0
    for v in graph:
        print(v)
    
        ##print(obj.stateName, obj.color,obj.adjacentStates, sep =' ' )
    
##def GenerateInitPopulation(populationSize, chromosomeSize):


# def create_chromosome():
#         chromosome = []
#         for i in range(n):
#             chromosome.append(random.randint(0, 3)) #color ranging from 0 to 3 (4 colors)
#         return chromosome

class States:
    def __init__(self,stateName,color,adjacentStates):
        self.stateName = stateName
        self.adjacentStates= adjacentStates
        self.color = color
    def getColor(self):
        return self.color
# class AdjacencyStates:
#     def __init__(self, ) -> None:
#         pass

def StartState():
    f = open("state_neighbours.txt")
    ##print(f.read())
    AllStates = []
    for line in f:
        l2 = line
        try:
            AdjacentList = (l2.split(None, 1)[1]).split()
        except IndexError:
            AdjacentList = ['']
        AllStates.append(States(line.split(None, 1)[0],(random.randint(0, 3)),AdjacentList))
    return AllStates

def createInitialPopulation(populationSize):
    
    ##generation = 0
    population = []
    for i in range(populationSize):
        chromosome = StartState()
        population.append(chromosome)


def fitness(graph, chromosome): #here graph is our adjacency matrix with vertices and edged having 0 or 1
    n = getNodes()
    edges = 0
    nonViolatingEdge = 0
    for i in range(n):
        for j in range(i, n):
            if graph[i][j] == 1:
                edges += 1
                if(chromosome[i].color != chromosome[j].color):
                    nonViolatingEdge += 1
    fitness = nonViolatingEdge/edges
    return fitness

def a():
    color = ["red","green","blue","yellow"]
    
    AllStates = StartState()
    AdjacencyMatrix(AllStates)
    # for obj in AllStates:
    #     print(obj.stateName, obj.color,obj.adjacentStates, sep =' ' )
    
    
def divide():
    n = 2
    k = 1/n 
    return k   
    
def test1():
    n = divide()
    print(n)

def main():
    AllStates = StartState()
    
    for obj in AllStates:
        print(obj.stateName, obj.color,obj.adjacentStates, sep =' ' )
    AdjacencyMatrix(AllStates)

main()
#test1()
#a()
##graph2()