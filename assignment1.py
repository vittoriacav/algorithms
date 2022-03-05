#MARIA VITTORIA CAVICCHIOLI (GENOMICS COURSE) --- ASSIGNMENT 1
#05/04/2020

import random 
import timeit
import numpy
import scipy.optimize

#MAIN ALGORITHM
'''
In this implemetation we find all possible combinations of suppliers using lists of 0 and 1 
0 = supplier not present in this combination
1 = supplier present in this combination
'''
def purchasePlan(n):
    global s, c, w, inc
    s = []
    c = []
    w = []
    inc = []

    #creation of the random weights, suppliers list and combination zero
    for i in range(n):
        s.append(i)
        c.append(0)
        w.append(round(random.random(), 2))

    #creation of the list of lists containing the incompatibilities for each suplier
    for i in range(n):  
        L = random.sample(s[:i]+s[i+1:], n//2)
        inc.append(L)
    
    global bestScore, bestSuppliers
    bestScore = 0
    bestSuppliers = []
    for i in range(2**n-1):
        combinator()

'''
Combinator function calls remainder function that check the current combination.
Depending on ith position combinaiton content (0 or 1) it updates the combination
'''
def combinator():
    i = 0
    while remainder(i) == 1:
        i+=1

def remainder(elem):
    r = 0
    if c[elem] == 0:
        c[elem]=1
        
        #creation of the combination of "real" suppliers depending on 0/1 combination and check for its compatibility
        supp_list = []
        for i in range(len(c)):
            if c[i] == 1:
                supp_list.append(i)
        x = compatibility(supp_list)
        
        #if the "real" suppliers combination is compatible, the program check for its total amount of weigth 
        #and possibly it assigns it to the bestScore and updates the bestSuppliers
        if x == "compatible":
            score = calculate_score(supp_list)
            global bestScore
            global bestSuppliers
            if score > bestScore:
                bestScore = score
                bestSuppliers = supp_list
    else:
        c[elem] = 0
        r = 1
    return r

#Compatibility function check if any of the suppliers present in the list of suppliers is present in any 
#other incompatibility list of the other suppliers
def compatibility(suppliers):
    for j in suppliers:
        for k in suppliers:
            if j in inc[k]:
                return "incompatible"
    return "compatible"

#This function calculate the total sum of the weigths associated to a list of suppliers
def calculate_score(suppliers):
    score = 0
    for i in suppliers:
        score = score + w[i]
    return score

#test function to get an average execution time for each input size
def Test(n):
    n_cycles = 100//n
    tot = timeit.timeit("purchasePlan(item)", number = n_cycles, setup='from __main__ import purchasePlan, item')
    return tot / n_cycles

#exponential function used by scipy to find an approxixmate value for the coefficients 
def func_exp(x, a, b):
    return a * numpy.exp(numpy.log(b) * x)

#function to print coordinates of the points that will be plotted on the LaTeX file
def printAlgoData():
    for (n,t) in zip(tests, times):
        print((n, round(t, 3)), end=' ')
    print()


tests = [4, 8, 12, 16, 20, 24]
times=[]
for item in tests:
    times.append(Test(item))
print(tests)
print(times)
print(scipy.optimize.curve_fit(func_exp, xdata = tests, ydata = times, ))
printAlgoData()

