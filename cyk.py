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
    ChG = []
    file = open(modelPath).read()
    Rules = file.split('\n')
    for i in range(len(Rules)-1):
        HEAD = Rules[i].split(' -> ')[0]
        TAIL = Rules[i].split(' -> ')[1]
        TAIL = TAIL.replace(" ", "")
        CTAIL = TAIL.split('|')
        tuple = HEAD, CTAIL
        ChG.append(tuple)
    return ChG


def cyk(Token, ChG):

    TableOut = [[[] for j in range(len(Token))]for i in range(len(Token))]
    
    for i in range(len(Token)):
        for item in ChG:
            if(Token[i] in item[1]):
                TableOut[0][i].extend([item[0]])
        if len(TableOut[0][i]) == 0:
            for TestRegex in regex:
                if(re.match(TestRegex, Token[i])):
                    for item in ChG:
                        if (regexDictionary[TestRegex] in item[1]) :
                            TableOut[0][i].extend([item[0]])
        
    
    for i in range(1, len(Token)):
        for j in range(len(Token)-i):
            for k in range(i):
                for P1 in TableOut[i-k-1][j]:
                    for P2 in TableOut[k][j+i-k]:
                        for item in ChG:
                            if(P1 + P2 in item[1]):
                                TableOut[i][j].extend([item[0]])

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
