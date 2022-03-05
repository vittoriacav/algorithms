#MARIA VITTORIA CAVICCHIOLI (GENOMICS COURSE) --- ASSIGNMENT 2
#02/05/2020

import random 
import timeit
import math
import numpy
import scipy.optimize
from scipy.special import factorial

# --- Generating random instances of the problem ---

def randomObjects(numberOfObjects, minWeight, maxWeight,
                    containersCapacity):

    objects = set(range(numberOfObjects))
    weights = dict()
    totalWeight = 0

    if containersCapacity < maxWeight:
        print("\nERROR")
        return "Change maxWeight or kilogramsCarriedByEachContainers"

    while totalWeight < containersCapacity:
        for oneObject in objects:
            weights[oneObject] = round(random.random(), 3)
            totalWeight = totalWeight + weights[oneObject]
    
    return (weights)

# --- Solving the combinatorial problem ---

#EXHAUSTIVE SOLUTION
def permutation(objectsList): 

    if len(objectsList) == 0: 
        return [] 
    if len(objectsList) == 1: 
        return [objectsList] 
    
    currentPermutation = []  
  
    for i in range(len(objectsList)): 
       currentIndex = objectsList[i] 
       remainingIndexes = objectsList[:i] + objectsList[i+1:] 

       for p in permutation(remainingIndexes): 
           currentPermutation.append([currentIndex] + p) 

    return currentPermutation 

def allocator(weights, objectsList, containersCapacity):

    allocation = {1: []}
    currentContainerWeight = 0
    currentContainerObjects = [ ]

    index = 0
    while index != len(objectsList):
        trueIndex = objectsList[index]
        indexWeight = weights[trueIndex]
        currentContainerWeight += indexWeight

        if currentContainerWeight > containersCapacity:
            allocation[len(allocation)] = currentContainerObjects
            allocation[len(allocation) + 1] = []
            currentContainerObjects = []
            currentContainerWeight = 0

        else:

            if index == len(objectsList)-1:
                currentContainerObjects.append(trueIndex)
                allocation[len(allocation)] = currentContainerObjects
                index += 1

            else: 
                currentContainerObjects.append(trueIndex)
                index += 1
    
    return(allocation)

def exhaustiveAlgoGrouping(weights, containersCapacity):
    # Input:
    # - weights: a dictionary in which the keys represent the 
    #           identifiers of the objects, while the values
    #           represents the weight corresponding to a 
    #           particular object
    # - containersCapacity: a number (float) that represents
    #           the fixed capacity of each container and the 
    #           
    # Output:
    # - bestAllocation: a dictionary in which the keys represent the 
    #           identifiers of the objects, while the values
    #           are lists representing the specific objects that 
    #           are inside each container
    
    minNumberOfContainers = len(weights)
    bestAllocation = []
    allPermutations = permutation(list(range(len(weights))))
    
    for onePermutation in allPermutations:
        containersForThisPermutation = allocator(weights, onePermutation, containersCapacity)

        if len(containersForThisPermutation) < minNumberOfContainers:
            minNumberOfContainers = len(containersForThisPermutation)
            bestAllocation = containersForThisPermutation
    
    return bestAllocation

#GREEDY SOLUTION
def greedyAlgoGrouping(weights, containersCapacity):
    #INPUT & OUTPUT are identical to 'exhaustiveAlgoGrouping' function
    bestAllocation = dict()
    containersListofWeights = []


    for i in range(len(weights)):
        containersListofWeights.append(0)
        bestAllocation[i+1] = []

    for index1 in weights:

        for index2 in range(len(containersListofWeights)):

            if containersListofWeights[index2] + weights[index1] <= containersCapacity:
                containersListofWeights[index2] += weights[index1]
                bestAllocation[index2+1].append(index1)
                break

    #checking for empty continers and romoving them         
    check = len(bestAllocation)
    while check != 1:
        if bestAllocation[check] == []:
            del bestAllocation[check]
        check-=1 

    return bestAllocation

# --- Testing Rountine ---
problemInstances = [
  { 'numberOfObjects': 4,
    'weights' : {0: 0.423, 1: 0.765, 2: 0.869,
                 3: 0.751},
    'containersCapacity' : 2,
    'solution' : {1: [0, 1], 2: [2, 3]}},
  { 'numberOfObjects': 6,
    'weights' : {0: 0.567, 1: 0.759, 2: 0.354, 3: 0.222,
                 4: 0.617, 5: 0.373},
    'containersCapacity' : 2.5,
    'solution' : {1: [0, 1, 2, 3], 2: [4, 5]}}]

def runAllTests():
    passed = True
    
    for instance in problemInstances:
        proposedExhaustiveSolution = exhaustiveAlgoGrouping(instance['weights'],
                                                        instance['containersCapacity'])
        proposedNumberOfContainers = len(proposedExhaustiveSolution)
        expectedNumberOfContainers = len(instance['solution'])

        if proposedNumberOfContainers != expectedNumberOfContainers:
            passed = False
        
    return passed
    
# --- Benchmarking Rountine ---

def testOneSize(numberOfObjects, algoType):
    containersCapacity = math.sqrt(numberOfObjects)
    randomInstance = randomObjects(numberOfObjects, 0, 1,
                                    containersCapacity)
    if algoType == 'E':
        exhaustiveAlgoGrouping(randomInstance, containersCapacity)
    else:
        greedyAlgoGrouping(randomInstance, containersCapacity)

def timeOneSize(numberOfObjects, algoType):
    if algoType == 'E':
        numberOfRuns = 10
    else:
        numberOfRuns = 50
    
    def runOnce():
        testOneSize(numberOfObjects, algoType)
        
    return timeit.timeit(runOnce, number=numberOfRuns) / numberOfRuns
          
def timeMultipleSizes(sizes, algoType):
    return [ timeOneSize(numberOfObjects, algoType) for numberOfObjects in sizes ]

# --- Model building ---

def func_fact(n, a):
    return a * factorial(n, exact=False) * n

def func_quad(n,a,b,c):
  return a*numpy.power(n,2)+ b * n + c





# --- User interaction ---

if (not runAllTests()):
    exit(1)

print("\nAll tests passed\n")

#CODE TO MEASURE TIME PERFORMANCE
inputSizes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#testing exhaustive (E) algo
times = timeMultipleSizes(inputSizes, 'E')
print("\nEXHAUSTIVE ALGORITHM\n")
print("Sizes:")
print(list(inputSizes), "\n")
print("Times:")
print(list(times), "\n")

print(scipy.optimize.curve_fit(func_fact, xdata = inputSizes, ydata = times,))

inputSizes = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
#testing greedy (G) algo
times = timeMultipleSizes(inputSizes, 'G')
print("\nGREEDY ALGORITHM\n")
print("Sizes:")
print(list(inputSizes), "\n")
print("Times:")
print(list(times), "\n")

print(scipy.optimize.curve_fit(func_quad, xdata = inputSizes, ydata = times,))

#CODE FOR THE EVALUATION OF THE APPROXIMATION RATIO

inputSizes = [4, 6, 8, 10]
ARlist = []
for oneSize in inputSizes:
    containersCapacity = math.sqrt(oneSize)
    randomInstance = randomObjects(oneSize, 0, 1,
                                    containersCapacity)
    
    exhaustiveSolution = len(exhaustiveAlgoGrouping(randomInstance, containersCapacity))
    greedySolution = len(greedyAlgoGrouping(randomInstance, containersCapacity))

    ARlist.append(greedySolution/exhaustiveSolution)
print("The calculated approximation ratios are: ", ARlist)
print("Worst approximation ratios is: ", max(ARlist))


