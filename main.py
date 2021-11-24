import sys
import readFile as rf
import cyk

if len(sys.argv) > 1:
    Path = str(sys.argv[1])
else:
	Path = 'input.txt'

userinput , line = rf.readInput(Path)

special = ['for', 'if', 'elif', 'else', 'while', 'with', 'def', 'class']
multi = ['"""',"'''"]

isMulti = False

new = []
for i in range(len(line)):
    new.extend(userinput[i])
    new.extend("$")

    ChG = cyk.bacaCNF('CNF.txt')

    if len(userinput[i]) > 2 and ((userinput[i][0] + userinput[i][1] + userinput[i][2]) in multi) and not ((userinput[i][-1] + userinput[i][-2] + userinput[i][-3]) in multi):
        isMulti= True

    if isMulti:
        if len(userinput[i]) > 2 and((userinput[i][-1] + userinput[i][-2] + userinput[i][-3]) in multi):
            isMulti = False
            Parse = cyk.cyk(new,ChG)

            if not ("START" in Parse[-1][0]):
                print("Syntax error: syntax error in line ", line[i])
                exit(0)
        elif (i == len(line)-1):
            Parse = cyk.cyk(new,ChG)

            if not ("START" in Parse[-1][0]):
                print("Syntax error: syntax error in line ", line[i])
                exit(0)
    else:
        Parse = cyk.cyk(new,ChG)

        if not ("START" in Parse[-1][0]):
            if not ((userinput[i][0] in special) and (i != len(line)-1)):
                print("Syntax error: syntax error in line ", line[i])
                exit(0)

print("Compile success")