maxPalValue = 0
numValue = 0

def palRes(number):
    tempNumber = str(number)
    for i in range(len(tempNumber)):
        if tempNumber[i] != tempNumber[len(tempNumber) - i - 1]:
            return 0
    return number

iterValue = 100
for i in range(100, 999):
    for j in range(iterValue, 999):
        numValue = i * j
        if maxPalValue < palRes(numValue):
            maxPalValue = palRes(numValue)
        numValue = 0
    iterValue += 1
print(maxPalValue)