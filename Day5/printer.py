rulesFile = open("advent_of_code_2024/Day5/printerRules.txt", "r")

# Don't change this part2 value, i promise
part2 = True

rules = {}
orders = []

doRules = True
for line in rulesFile.readlines() :
    if line.strip() == "" : doRules = False
    else :
        if doRules :
            rules.setdefault(line.strip().split("|")[0], set())
            rules[line.strip().split("|")[0]].add(line.strip().split("|")[1])
        else : orders.append(line.strip())

def evalOrder(order) : 
    for i in range(len(order)-1) :
        for j in order[:i+1] :
            if order[i+1] not in rules[j] :
                if part2 :
                    tempVal = order[order.index(j)]
                    order[order.index(j)] = order[i+1]
                    order[i+1] = tempVal
                    return evalOrder(order)
                else : return 0
    return order[int((len(order)-1)/2)]

total = 0
for order in orders : total += int(evalOrder(order.split(',')))

if part2 :
    part2 = False
    newTotal = 0
    for order in orders : newTotal += int(evalOrder(order.split(',')))
    total -= newTotal

print(f"Part 1: {newTotal}\nPart 2: {total}")

rulesFile.close()

# 6384

# 11662
#*
# 5278