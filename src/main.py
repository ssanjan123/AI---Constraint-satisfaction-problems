from cProfile import label
from ctypes import sizeof
import random
import numpy as np
import matplotlib.pyplot as plt


##Configurable Parameters/Global Variables - Change these when testing each case
###############################################
populationSize = 10
k = 2 ##How many times will the tournament run
colors = (0,1,2,3)
mutationRate = 0.01
numberOfGenerations = 35 ##getdata has a parameter for this so can be customizable there as well
#############################################
#############################################


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
# AB  0 1  0  1.....
# BC  1 0  1  0.....
# MB  0
# NB  1
# NL  .
# NS  .
# NT  .
# NU  .
# ON  .
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
    return graph
    
def StartState():
    f = open("state_neighbours.txt")
    AllStates = []
    for line in f:
        l2 = line
        try:
            AdjacentList = (l2.split(None, 1)[1]).split()
        except IndexError:
            AdjacentList = ['']
        AllStates.append(States(line.split(None, 1)[0],(random.choice(colors)),AdjacentList))
    return AllStates


def createInitialPopulation():
    population = []
    for i in range(populationSize):
        chromosome = StartState()
        population.append(chromosome)
    return population


def fitness(chromosome): 
    graph = AdjacencyMatrix(chromosome) 
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
    for i in range(0, populationSize-1, k):
        random.shuffle(population)
        if fitness(population[i]) > fitness(population[i+1]):
            parents.append(population[i])
        else:
            parents.append(population[i+1])
    return parents

def crossover(parent1, parent2):
    n = getNodes()
    position = random.randint(1, n-2)
    child1 = []
    child2 = []
    for i in range(position):
        child1.append(parent1[i])
        child2.append(parent2[i])
    for i in range(position, n):
        child1.append(parent2[i])
        child2.append(parent1[i])
    return child1, child2


def produceNewGen(parents):
    newPopulation = []
    while len(newPopulation) < populationSize:
        ## choose random parents
        random.shuffle(parents)
        x = parents[:int((len(parents)+1)*.50)]
        y = parents[int((len(parents)+1)*.50):]
        i = min(len(x),len(y))
        for j in range(i):
            if(len(newPopulation) == populationSize):
                return newPopulation
            newPopulation.extend(crossover(x[j],y[j]))
    return newPopulation         

def mutation(chromosome):
    n= getNodes()
    for i in range(n):
        check = random.uniform(0, 1) ## checks mutationRate the higher this value the lower the chance of mutation
        if(check <= mutationRate):
            chromosome[i].color = random.choice(colors)
    return chromosome

def mutateAll(population):
    mutatedPopulation =[]
    for i in range(populationSize):
        mutatedPopulation.append(mutation(population[i]))
    return mutatedPopulation
    
def Average(lst):
    return sum(lst) / len(lst)

    

def getData(numberOfGenerations,willPrint):
    bestFit = None
    avgFit = None
    worstFit = None
    fitlist =[]
    oldPopulation = createInitialPopulation()
    for i in range(numberOfGenerations):
        if(willPrint == True):
            print("Generation #",i)
        for j in range(populationSize):
            fit = fitness(oldPopulation[j])
            fitlist.append(fit)
            if(fit == 1.0):
                bestFit = 1.0
                worstfit = min(fitlist)
                avgFit = Average(fitlist)
                print("Solution found!!")
                for obj in oldPopulation[j]:
                    print(obj.stateName, obj.color,obj.adjacentStates, sep =' ' )
                print("Best fitness:", bestFit)
                print("Worst fitness:", worstFit)
                print("Average fitness:", avgFit)
                return bestFit,avgFit,worstFit
        newparents = TournamentSelection(oldPopulation)
        for j in range(len(newparents)):
            fit = fitness(newparents[j])
            fitlist.append(fit)
            if(fit == 1.0):
                bestFit = 1.0
                worstfit = min(fitlist)
                avgFit = Average(fitlist)
                print("Solution found!!")
                for obj in newparents[j]:
                    print(obj.stateName, obj.color,obj.adjacentStates, sep =' ' )
                print("Best fitness:", bestFit)
                print("Worst fitness:", worstfit)
                print("Average fitness:", avgFit)
                return bestFit,avgFit,worstfit
        newPopulations = produceNewGen(newparents)
        for j in range(populationSize):
            fit = fitness(newPopulations[j])
            fitlist.append(fit)
            if(fit == 1.0):
                bestFit = 1.0
                worstfit = min(fitlist)
                avgFit = Average(fitlist)
                print("Solution found!!")
                for obj in newPopulations[j]:
                    print(obj.stateName, obj.color,obj.adjacentStates, sep =' ' )
                print("Best fitness:", bestFit)
                print("Worst fitness:", worstfit)
                print("Average fitness:", avgFit)
                return bestFit,avgFit,worstfit
        mutatedPopulation = mutateAll(newPopulations)
        oldPopulation = mutatedPopulation
        bestFit = max(fitlist)
        worstfit = min(fitlist)
        avgFit = Average(fitlist)
        if(willPrint == True):
            print("Best fitness:", bestFit)
            print("Worst fitness:", worstfit)
            print("Average fitness:", avgFit)
    for j in range(populationSize):
            fit = fitness(oldPopulation[j])
            fitlist.append(fit)
            if(fit == 1.0):
                bestFit = 1.0
                worstfit = min(fitlist)
                avgFit = Average(fitlist)
                print("Solution found!!")
                for obj in oldPopulation[j]:
                    print(obj.stateName, obj.color,obj.adjacentStates, sep =' ' )
                print("Best fitness:", bestFit)
                print("Worst fitness:", worstfit)
                print("Average fitness:", avgFit)
                return bestFit,avgFit,worstfit
    return bestFit,avgFit,worstfit      



def plot():
    yBest = []
    yAverage = []
    yWorst = []
    xRange = 35 ##Here put the number for how many generations you want for the x axis - By default setting it to 35
    for i in range(xRange): 
        t = getData(i+1,False) 
        yBest.append(t[0])
        yAverage.append(t[1])
        yWorst.append(t[2])
        if(t[0] == 1):
            plt.plot(len(yBest), yBest, label = "Best")
            plt.plot(len(yAverage), yAverage, label = "Average")
            plt.plot(len(yWorst), yWorst, label = "Worst")
            plt.xlabel("Generation")
            plt.ylabel("Fitness")
            plt.legend()
            plt.show()
            return
    xGeneration = list(range(1,xRange+1))
    plt.plot(xGeneration, yBest, label = "Best")
    plt.plot(xGeneration, yAverage, label = "Average")
    plt.plot(xGeneration, yWorst, label = "Worst")
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.legend()
    plt.show()
####################################################
##Printing each test Cases - Change the Configurables above at the beginning to get different scenarios
def testCases(): 
    print(getData(50,False))
###################################################
####Graph plot with this
plot()
