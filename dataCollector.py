""" Python automation to collect expenses data from whatsapp
An expense entry will look like:
    [9:49 AM, 11/4/2023] nivalderramas: 6000 tamal
"""

expensesFileName = "expenses.txt"
outputFileName = "out.txt"
inputFile = open(expensesFileName)
outputFile = open(outputFileName, "w")

for expense in inputFile:
    line = expense.split("]")

    rawDate = line[0]
    rawDate = rawDate.split(",")
    date = rawDate[1][1:]

    rawMessage = line[1].split(":")[1][1:]
    rawMessage = rawMessage.split(" ", maxsplit=1)
    value = rawMessage[0]
    message = rawMessage[1]
    # Remove the k and add the three zeroes
    value = (value[:-1]) + "000"
    outputLine = date + "\t" + value + "\t" + message
    outputFile.write(outputLine)
