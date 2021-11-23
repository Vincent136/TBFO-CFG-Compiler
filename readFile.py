
import re

def readInput(fileName):
    # Read from file
    with open(fileName, 'r') as f:
        contents = f.read()
        contents = contents.split()

        result = contents
        # For each operator..
        temporaryResult = []
        # For each statement..
        for statement in result:
            x = re.split('(\W)', statement)
            # add the split result to temporaryResult
            for splitStatement in x:
                temporaryResult.append(splitStatement)

        result = temporaryResult

        # remove empty string
        result = [string for string in result if string != '']
        print(result)
        return result


