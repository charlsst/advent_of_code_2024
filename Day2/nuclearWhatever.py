reportFile = open("advent_of_code_2024/Day2/report.txt", "r")

numOfSafe, numOfDangerous = 0, 0

# Set to true to get answer for part 2, false to get answer for part 1
part2 = True

for line in reportFile.readlines() :
    reportLine = line.strip().split(" ")
    asc = True
    isSafe = True
    if int(reportLine[1]) < int(reportLine[0]) : asc = False
    for i in range(1, len(reportLine)) : 
        if (asc and int(reportLine[i]) > int(reportLine[i-1])) or (not asc and int(reportLine[i]) < int(reportLine[i-1])) :
            if abs(int(reportLine[i]) - int(reportLine[i-1])) > 3 :
                isSafe = False
                break
        else :
            isSafe = False
            break
    
    if not isSafe and part2 :
        for i in range(len(reportLine)) :
            newReportLine = reportLine.copy()
            newReportLine.pop(i)
            asc = True
            secondSafeCheck = True
            if int(newReportLine[1]) < int(newReportLine[0]) : asc = False
            for i in range(1, len(newReportLine)) : 
                if (asc and int(newReportLine[i]) > int(newReportLine[i-1])) or (not asc and int(newReportLine[i]) < int(newReportLine[i-1])) :
                    if abs(int(newReportLine[i]) - int(newReportLine[i-1])) > 3 :
                        secondSafeCheck = False
                        break
                else :
                    secondSafeCheck = False
                    break
            if secondSafeCheck :
                isSafe = True
                break
    
    if isSafe : numOfSafe += 1
    else : numOfDangerous += 1

print(f"Safe: {numOfSafe}\nDangerous: {numOfDangerous}")

reportFile.close()