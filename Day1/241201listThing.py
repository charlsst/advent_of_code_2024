listFile = open("advent_of_code_2024/Day1/lists.txt")

list1, list2 = [], []

for line in listFile.readlines() :
    line = line.strip().split('   ')
    list1.append(line[0])
    list2.append(line[1])

list1.sort()
list2.sort()

sum = 0
for i in range(len(list1)) : sum += abs(int(list1[i])-int(list2[i]))

print(f"Sum (part 1): {sum}")

score = 0

for i in list1 :
    for j in list2 :
        if i == j : score += int(j)

print(f"Similarity Score (part 2): {score}")

listFile.close()