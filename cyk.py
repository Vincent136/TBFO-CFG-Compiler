import re
import sys
import readFile as rf

# Regex List
regexList = [r'[A-z0-9]*', r'[0-9]*', r'[A-Za-z_][A-Za-z_0-9]*']

# Maps regex into valid key
regexMap = {
    r'[A-z0-9]*': ["string"],
    r'[0-9]*': ["number"],
    r'[A-Za-z_][A-Za-z_0-9]*': ["variable"],
}

global ChG
ChG = {}


def LoadCNF(modelPath):
    file = open(modelPath).read()
    rawRules = file.split('\n')
    for i in range(len(rawRules)-1):
        A = rawRules[i].split(' -> ')[0]
        B = rawRules[i].split(' -> ')[1]
        B = B.replace(" ", "")
        C = B.split('|')
        for j in range(len(C)):
            value = ChG.get(C[j])
            if (value == None):
                ChG.update({C[j]: [A]})
            else:
                ChG[C[j]].append(A)


def cyk(Token):

    TableOut = [[[] for j in range(i)]
                for i in range(len(Token), 0, -1)]
    for i in range(len(Token)):
        try:
            TableOut[0][i].extend(ChG[Token[i]])
        except KeyError:
            for P in regexList:
                if(re.match(P, Token[i])):
                    for regexType in regexMap[P]:
                        try:
                            TableOut[0][i].extend(ChG[regexType])
                        except KeyError:
                            continue

    for i in range(1, len(Token)):
        for j in range(len(Token)-i):
            for k in range(i):
                for P1 in TableOut[i-k-1][j]:
                    for P2 in TableOut[k][j+i-k]:
                        try:
                            TableOut[i][j] = ChG[P1 + P2]
                        except KeyError:
                            continue
    return TableOut


def checkValidity(table, wanted):
    return wanted in table[-1][-1]


# tess
if len(sys.argv) > 1:
    modelPath = str(sys.argv[1])
else:
    modelPath = 'cnf.txt'

LoadCNF(modelPath)

inp = rf.readInput("test.txt")
inp2 = cyk(inp)

if (checkValidity(inp2, "S")):
    print("Verdict accepted! Compile success!")
else:
    print("Compile error, wrong syntax!")
