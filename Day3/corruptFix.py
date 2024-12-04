corruptionFile = open('advent_of_code_2024/Day3/corruption.txt')

part2 = True

tempLines = corruptionFile.readlines()
corruptionLines = []

if part2 :
    for line in tempLines :
        line.replace("don't()", "do()GETRIDOFME")
        for i in line.split("do()") :
            if i[1][:10] != "GETRIDOFME" :
                corruptionLines.append(i)
else :
    corruptionLines = tempLines

for i in corruptionLines : print(i)

mulInstances = []
for line in corruptionLines :
    while line.find('mul(') != -1 :
        mulIndex = line.find('mul(')
        mulInstances.append(line[mulIndex:mulIndex+12])
        line = line.replace('mul(', '', 1)

#for i in corruptionLines : print(f"- {i}\n")

print("HELLO"[:4])
    

total = 0
for possible in mulInstances :
    try :
        possible = possible.split(')')[0]
        possible = possible.replace('mul(', '').replace(')', '').replace('\n', '')
        possibleList = possible.split(',')
        if len(possibleList) == 2 and possibleList[0].find(' ') == -1 and possibleList[1].find(' ') == -1 :
            total += int(possibleList[0]) * int(possibleList[1])
            print(f"{possibleList[0]} * {possibleList[1]} = ({int(possibleList[0]) * int(possibleList[1])})")
    except : pass

print(f"Total: {total}")

corruptionFile.close()

#*187194524 - part 1

# 374378353
#*187194524
# 128670117
# 112945167
# 109108832
# 44026963