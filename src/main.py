##from utils import argmin_random_tie, count, first
##mport search

import random










##Configurable Parameters/Global Variables
populationSize = 100
k = 4 ##How many times will the tournament run
colors = (0,1,2,3,4)

def getNodes():
    f = open("state_neighbours.txt")
    return len(f.readlines())
    
class States:
    def __init__(self,stateName,color,adjacentStates):
        self.stateName = stateName
        self.adjacentStates= adjacentStates
        self.color = color
    def getColor(self):
        return self.color

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
    return graph
    
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


############ Graph G(V,E)
graph = AdjacencyMatrix(StartState()) #here graph is our
######## adjacency matrix with vertices and edged having 0 or 1


def createInitialPopulation():
    
    ##generation = 0
    population = []
    for i in range(populationSize):
        chromosome = StartState()
        population.append(chromosome)
    return population


def fitness(chromosome): 
    n = getNodes()
    edges = 0
    nonViolatingEdge = 0
    for i in range(n):
        for j in range(i, n):
            try:
                if graph[i][j] == 1:
                    edges += 1
                    if(chromosome[i].color != chromosome[j].color):
                        nonViolatingEdge += 1
            except TypeError as e:
                print(j)
    fitness = nonViolatingEdge/edges
    return fitness

def TournamentSelection(population):
    parents = []
    for j in range(k):
        random.shuffle(population)
        for i in range(0, populationSize-1, k):
            if fitness(population[i]) > fitness(population[i+1]):
                parents.append(population[i])
            else:
                parents.append(population[i+1])
    return parents

def crossover(parent1, parent2):
    n = getNodes()
    position = random.randint(2, n-2)
    child1 = []
    child2 = []
    for i in range(position+1):
        child1.append(parent1[i])
        child2.append(parent2[i])
    for i in range(position+1, n):
        child1.append(parent2[i])
        child2.append(parent1[i])
    return child1, child2

def produceNewGen(parents):
    newChromosome = []
    #for i in range(populationSize):



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
    adj = AdjacencyMatrix(AllStates)

    e = fitness(AllStates)
    print(e)

    newpop = TournamentSelection(createInitialPopulation())
    for obj in newpop:
        for i in obj:
            print(i.stateName)

main()
#test1()
#a()
##graph2()