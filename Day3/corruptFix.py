corruptionFile = open('advent_of_code_2024/Day3/corruption.txt')

part2 = True

tempLines = corruptionFile.readlines()
corruptionLines = []

if part2 :
    line = ''.join(tempLines).replace("don't()", "do()GETRIDOFME")
    for i in line.split("do()") :
        if i[:10] != "GETRIDOFME" :
            corruptionLines.append(i)
else :
    corruptionLines = tempLines

mulInstances = []
for line in corruptionLines :
    while line.find('mul(') != -1 :
        mulIndex = line.find('mul(')
        mulInstances.append(line[mulIndex:mulIndex+12])
        line = line.replace('mul(', '', 1)

total = 0
for possible in mulInstances :
    try :
        possible = possible.split(')')[0]
        possible = possible.replace('mul(', '').replace(')', '').replace('\n', '')
        possibleList = possible.split(',')
        if len(possibleList) == 2 and possibleList[0].find(' ') == -1 and possibleList[1].find(' ') == -1 :
            total += int(possibleList[0]) * int(possibleList[1])
    except : pass

print(f"Total: {total}")

corruptionFile.close()