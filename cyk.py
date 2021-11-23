import re
import sys
import readFile as rf 


regex = [r'[A-z0-9]*',
             r'[0-9]*', 
             r'[A-Za-z_][A-Za-z_0-9]*']




regexDictionary = {
    r'[A-z0-9]*': "string",
    r'[0-9]*': "number",
    r'[A-Za-z_][A-Za-z_0-9]*': "variable",
}


def bacaCNF(modelPath):
    chomskyGrammar = []
    file = open(modelPath).read()
    rawRules = file.split('\n')
    for i in range (len(rawRules)-1):
        A = rawRules[i].split(' -> ')[0]
        B = rawRules[i].split(' -> ')[1]
        B = B.replace(" ","")
        C = B.split('|')
        for j in range (len(C)):
            if len(chomskyGrammar) > 0:
                found = False
                for item in chomskyGrammar:
                    if (C[j] == item[0]):
                        item[1].extend([A])
                        found = True
                        break
                if (not found):
                    tuple = C[j],[A]
                    chomskyGrammar.append(tuple)
            else:
                tuple = C[j],[A]
                chomskyGrammar.append(tuple)

    return(chomskyGrammar)


def cyk(Token, ChG):

    TableOut = [[[] for j in range(len(Token))]for i in range(len(Token))]
    
    for i in range(len(Token)):
        for item in ChG:
            if(Token[i] == item[0]):
                TableOut[0][i].extend(item[1])
                TableOut[0][i] = list(dict.fromkeys(TableOut[0][i]))
        for TestRegex in regex:
            if(re.match(TestRegex, Token[i])):
                for item in ChG:
                    if (regexDictionary[TestRegex] == item[0]) :
                        TableOut[0][i].extend(item[1])
                        TableOut[0][i] = list(dict.fromkeys(TableOut[0][i]))
                        break
    
    for i in range(1, len(Token)):
        for j in range(len(Token)-i):
            for k in range(i):
                for P1 in TableOut[i-k-1][j]:
                    for P2 in TableOut[k][j+i-k]:
                        for item in ChG:
                            if(P1+P2 == item[0]):
                                TableOut[i][j].extend(item[1])
                                break
                TableOut[i][j] = list(dict.fromkeys(TableOut[i][j]))
   
    return(TableOut)
                        


# tess
if len(sys.argv) > 1:
    input = str(sys.argv[1])
else:
    input = 'input.txt'

ChG = bacaCNF('CNF.txt')

inp = rf.readInput(input)

print("Compiling....")

Parse = cyk(inp, ChG)

if ("START" in Parse[-1][0] or "COMMENT" in Parse[-1][0]):
    print("Compile Succes!")
else:
    print("Syntax error : Invalid syntax")
