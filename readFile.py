import re

def readInput(path):

    userinput = []
    line = []

    with open(path, 'r') as f:
        
        contents = f.read()
        contents = contents.split("\n")
        regex = re.compile(r'^(?P<indent>(?: {4})*)(?P<name>\S.*)')

        for i in range(len(contents)):
            result = contents[i]
            result = result.split()


            temporaryResult = []

            match = regex.match(contents[i])
            if not match:
                if len(contents[i]) != 0:
                    print(contents[i])
                    print("^ Indentation error at line ", i + 1)
                    exit(0)
            
            for statement in result:
                x = re.split('(\W)', statement)
                for splitStatement in x:
                    temporaryResult.append(splitStatement)

            result=temporaryResult
        
            result = [string for string in result if string != '']

            if (len(result) != 0):
                userinput.append(result)
                line.append(str(i+1))
    return userinput , line


        