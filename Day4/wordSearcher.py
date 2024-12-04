wordsearchFile = open("advent_of_code_2024/Day4/wordsearch.txt", "r")

wordsearchLines = [i.strip() for i in wordsearchFile.readlines()]
wsX, wsY = len(wordsearchLines[0]), len(wordsearchLines)

#PART1
xmasAppearances = 0

vertCount = 0
while vertCount < wsY :
    horiCount = 0
    while horiCount < wsX  :
        #print(f"Start: ({horiCount},{vertCount}) of ({wsX},{wsY})")
        if vertCount < wsY-3 :
            xmasText = wordsearchLines[vertCount][horiCount]+wordsearchLines[vertCount+1][horiCount]+wordsearchLines[vertCount+2][horiCount]+wordsearchLines[vertCount+3][horiCount]
            if (xmasText == "XMAS" or xmasText == "SAMX") :
                xmasAppearances += 1
                print(f"Start: ({horiCount},{vertCount}) |")
            
        if horiCount < wsX-3 :
            xmasText = wordsearchLines[vertCount][horiCount]+wordsearchLines[vertCount][horiCount+1]+wordsearchLines[vertCount][horiCount+2]+wordsearchLines[vertCount][horiCount+3]
            if (xmasText == "XMAS" or xmasText == "SAMX") :
                xmasAppearances += 1
                print(f"Start: ({horiCount},{vertCount}) -")

        if vertCount < wsY-3 and horiCount < wsX-3 :
            xmasText = wordsearchLines[vertCount][horiCount]+wordsearchLines[vertCount+1][horiCount+1]+wordsearchLines[vertCount+2][horiCount+2]+wordsearchLines[vertCount+3][horiCount+3]
            if (xmasText == "XMAS" or xmasText == "SAMX") :
                xmasAppearances += 1
                print(f"Start: ({horiCount},{vertCount}) l")
            
            xmasText = wordsearchLines[vertCount][horiCount+3]+wordsearchLines[vertCount+1][horiCount+2]+wordsearchLines[vertCount+2][horiCount+1]+wordsearchLines[vertCount+3][horiCount]
            if (xmasText == "XMAS" or xmasText == "SAMX") :
                xmasAppearances += 1
                print(f"Start: ({horiCount},{vertCount}) /")
        horiCount += 1
    vertCount += 1

#PART 2
xMasAppearances = 0

vertCount = 0
while vertCount < wsY :
    horiCount = 0
    while horiCount < wsX  :
        #print(f"Start: ({horiCount},{vertCount}) of ({wsX},{wsY})")
        if vertCount < wsY-2 and horiCount < wsX-2 :
            xmasText1 = wordsearchLines[vertCount][horiCount]+wordsearchLines[vertCount+1][horiCount+1]+wordsearchLines[vertCount+2][horiCount+2]
            xmasText2 = wordsearchLines[vertCount][horiCount+2]+wordsearchLines[vertCount+1][horiCount+1]+wordsearchLines[vertCount+2][horiCount]
            if (xmasText1 == "MAS" or xmasText1 == "SAM") and  (xmasText2 == "MAS" or xmasText2 == "SAM"):
                xMasAppearances += 1
                print(f"Centre: ({horiCount+1},{vertCount+1}) X")

        horiCount += 1
    vertCount += 1

print(f"XMAS Appearances: {xmasAppearances}")
print(f"X-MAS Appearances: {xMasAppearances}")

wordsearchFile.close()

# 
#*2458
# 2435
# 2396

#
#*
#