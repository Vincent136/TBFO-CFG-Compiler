import sys
import readFile as rf
import cyk

if len(sys.argv) > 1:
    Path = str(sys.argv[1])
else:
	Path = 'input.txt'

userinput , line = rf.readInput(Path)

special = ['for', 'if', 'elif', 'else', 'while', 'with', 'def', 'class']

new = []
for i in range(len(line)):
    new.extend(userinput[i])
    new.extend("$")

    ChG = cyk.bacaCNF('CNF.txt')

    Parse = cyk.cyk(new,ChG)

    if not ("START" in Parse[-1][0]):
        if not ((userinput[i][0] in special) and (i != len(line)-1)):
            print("Syntax error: syntax error in line ", line[i])
            exit(0)

print("Compile success")