import sys

number = ['1','2','3','4','5','6','7','8','9','10']

def checkNumber(string):
    for item in string:
        if not (item in number):
            return False
    return True

def checkVariable(string):
    if string[0] in number:
        return False
    else:
        return True


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
        isVariable = checkVariable(Token[i])
        isNumber = checkNumber(Token[i])
        if isVariable:
            for item in ChG:
                if("variable" == item[0]):
                    TableOut[0][i].extend(item[1])
                    TableOut[0][i] = list(dict.fromkeys(TableOut[0][i]))
        if isNumber:
            for item in ChG:
                if("number" == item[0]):
                    TableOut[0][i].extend(item[1])
                    TableOut[0][i] = list(dict.fromkeys(TableOut[0][i]))
        for item in ChG:
            if("string" == item[0]):
                TableOut[0][i].extend(item[1])
                TableOut[0][i] = list(dict.fromkeys(TableOut[0][i]))

    for i in range(len(Token)):
        for P in TableOut[0][i]:
            for item in ChG:
                if(P == item[0]):
                    TableOut[0][i].extend(item[1])
                    TableOut[0][i] = list(dict.fromkeys(TableOut[0][i]))
    
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
                        
