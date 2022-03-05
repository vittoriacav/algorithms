#MARIA VITTORIA CAVICCHIOLI (GENOMICS COURSE) --- ASSIGNMENT 3
#27/05/2020

# --- Reading the instances from a given file ----

def readInstance(fileName):
    with open(fileName, "r") as file:
        patternLength = int(file.readline())
        maxDistance = int(file.readline())
        stringS = file.readline().strip()

        if patternLength < 0: raise ValueError
        if maxDistance < 0: raise ValueError
        for character in stringS:
            if character not in 'ACTG': raise ValueError

    return (patternLength, maxDistance, stringS) 



# --- Solving the combinatorial problem ---

def charsQuantities(patternLength):
    # Input:
    # - patternLength : a number (integer) that represents the pattern length
    # Output:
    # - quantitiesList : a particular list of lists used to create combinations with 
    #                    repeats (later), given a length called 'patternLength'
    #       EXAMPLE: If my patternLength = 4
    #                quantitiesList = [
    #                                [4],
    #                                [3,1],
    #                                [2,2],
    #                                [2,1,1], 
    #                                [1,3],
    #                                [1,2,1],
    #                                [1,1,1,1]]
    #               Each list gives me the following information:
    #                   - length of the list = number of different characters I have to pick from the alphabet
    #                   - each number in the list = how many time I have to pick a particular character
    #               For the third list for example [2,2] I will get (thanks to other functions like combinationsWithRep 
    #               and permutation): 'AACC', 'CCAA', 'GGTT', 'TTGG', 'AATT', 'TTAA', 'CCGG', 'GGCC' etc.
    #

    quantitiesList = [
                    [patternLength],
                    [patternLength-1,1],
                    [patternLength-2,2],
                    [patternLength-2,1,1], 
                    [patternLength-3,3],
                    [patternLength-3,2,1],
                    [patternLength-3,1,1,1]]
    if patternLength < 4:
        i = len(quantitiesList)-1
        while i != 0:
            if quantitiesList[i][0] <= 0:
               del quantitiesList [i]
            i-=1
    return quantitiesList

#The following two functions have the same input (self-explanatory)
#They work together to produce all possible permutations of a given 
#string. combinationsNoRep is never called except by the
#permutation function

def permutation(string, length):
    if not length:
        yield ''
    else:
        for comb in combinationsNoRep(string, length):
            for i, char in enumerate(comb):
                rest = comb[:i] + comb[i+1:] 
                for perm in permutation(rest, length-1):
                    yield char + perm 

def combinationsNoRep(string, length):
    if not length:
        yield ''
    elif string:
        first, rest = string[0], string[1:]
        for comb in combinationsNoRep(rest, length-1):
            yield first + comb 
        yield from combinationsNoRep(rest, length) 

def combinationsWithRep(alphabet, quantitiesList):
    # Input:
    # - alphabet : a list of characters from which all the patterns are drawn up
    # - quantitiesList : a particular list of lists used to create combinations with 
    #                    repeats (explained above), given a length called 'patternLength' 
    # Output:
    # - allCombs : a list of strings in which are present all possible
    #              strings of length 'patternLength' drawn up from the 
    #              input alphabet


    allCombs = []

    for currentQuantities in quantitiesList:
        if len(currentQuantities) == 1:
            for one_letter in alphabet:
                allCombs.append(currentQuantities[0]*one_letter)
        elif len(currentQuantities) == 2:
            for two_letters in list(permutation(alphabet,2)):
                allCombs.append(currentQuantities[0]*two_letters[0]+currentQuantities[1]*two_letters[1])
        elif len(currentQuantities) == 3:
            for three_letters in list(permutation(alphabet,3)):
                allCombs.append(currentQuantities[0]*three_letters[0]+currentQuantities[1]*three_letters[1]+currentQuantities[2]*three_letters[2])
        else:
            for four_letters in list(permutation(alphabet,4)):
                allCombs.append(currentQuantities[0]*four_letters[0]+currentQuantities[1]*four_letters[1]+currentQuantities[2]*four_letters[2]+currentQuantities[3]*four_letters[3])
        
    return allCombs

def allPossiblePatterns(alphabet, patternLength):
    # Input:
    # - alphabet : a list of characters from which all the patterns are drawn up
    # - patternLength : a number (integer) that represents the pattern length
    # Output:
    # - allPossiblePatternsSet : a set of strings in which are present all possible
    #                            strings of length 'patternLength' drawn up from the 
    #                            input alphabet

    quantitiesList = charsQuantities(patternLength)
    allPossiblePatternsSet = set(combinationsWithRep(alphabet, quantitiesList))

    for onePattern in allPossiblePatternsSet:

        if len(onePattern) != patternLength:
            print("ERROR: something went wrong")
        else:
            allPossiblePatternsSet = allPossiblePatternsSet | set(permutation(onePattern, patternLength))

    return allPossiblePatternsSet

def HammingDistance(string1, string2, maxD):
    # Input:
    # - string1 & string 2 : two strings that should be of the same length
    # - maxD : a number (integer) that fixes the maximum Hamming Distance 
    #          between the two strings 
    # Output:
    # - hd : a number (integer) that is never greater than maxD+1 and grows until
    #       the hamming distance grows

    if len(string1) != len(string2):
        print("ERROR: lengths of the two given strings must be equal")
    
    else: 
        hd = 0
        i = 0
        while i != len(string1):
            if string1[i] != string2[i]:
                hd+=1
            if hd == maxD +1:
                break
            i+=1
        return hd

def all_StringS_Substrings(patternLength, stringS):
    # Input:
    # - patternLength : a number (integer) that represents the pattern length
    # - stringS : a string representing a long strand of DNA
    # Output:
    # - all the substrings of length 'patternLength' found in stringS

    i = 0
    while i != len(stringS) - patternLength + 1:
        yield stringS[i:i+patternLength]
        i += 1

def mostRepeatedPattern(allPossiblePatternsSet, stringS, patternLength, maxD):
    # Input:
    # - allPossiblePatternsSet : see output of "allPossiblePatterns
    #" function
    # - stringS : a string representing a long strand of DNA
    # - patternLength : a number (integer) that represents the pattern length
    # - maxD : a number (integer) that represents the maximum distance between a given 
    #       string of length patternLength and a substring of length patternLength in the stringS
    # Output:
    # - bestPattern : the string of length patternLength that is repeated the most in stringS
    #                   with up to maxD modifications
    # - maxScore : number of "matches" found between bestPattern and the substrings
    #              of length patternLength in stringS, with up to maxD modifications

    maxScore = 0
    bestPattern = ''
    for onePattern in allPossiblePatternsSet:
        counter = 0
        for oneSubstring in all_StringS_Substrings(patternLength, stringS):
            if HammingDistance(onePattern, oneSubstring, maxD) <= maxD:
                counter += 1
        if counter > maxScore:
            maxScore = counter
            bestPattern = onePattern
    
    return (bestPattern, maxScore)


# --- User interaction ---

alphabet = ['C', 'G', 'T', 'A']
data = readInstance("inputdata.txt")

stringS = data[2]
maxDistance = data[1]
patternLength = data[0]

if patternLength > len(stringS):
    print("ERROR: length of the pattern cannot be greater than the stringS itself")
else:
    result = mostRepeatedPattern(allPossiblePatterns(alphabet, patternLength), stringS, patternLength, maxDistance)
    print ("\nThe string of length ", patternLength, ", repeated most often in the input stringS, with up to", 
            maxDistance," modifications, is ", result[0], ", found ", result[1], " times in the stringS")
