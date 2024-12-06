mapFile = open("advent_of_code_2024/Day6/map.txt", "r")

WALK_DIR = {
    "N" : (0, -1),
    "E" : (1, 0),
    "S" : (0, 1),
    "W" : (-1, 0)
}
TURN_DIR = {
    "N" : "E",
    "E" : "S",
    "S" : "W",
    "W" : "N"
}

guard = {
    "orientation" : "N",
    "position" : [0, 0]
}
guard2 = {
    "orientation" : "N",
    "position" : [0, 0]
}

mapOfArea = [ [ i for i in j.strip() ] for j in mapFile.readlines() ]
mapOfArea2 = mapOfArea.copy()

for y in range(len(mapOfArea)) :
    for x in range(len(mapOfArea[y])) :
        if mapOfArea[y][x] == "^" : guard["position"] = [x, y]
guard2["position"] = guard["position"]
    
print(mapOfArea)

totalStops = 0
stepCount = 0

print(0, len(mapOfArea[0])-1, 0,len(mapOfArea)-1)
while guard["position"][0] > 0 and guard["position"][0] < len(mapOfArea[0])-1 and guard["position"][1] > 0 and guard["position"][1] < len(mapOfArea)-1 :
    guardPos = guard["position"]
    guardOri = guard["orientation"]
    nextPos = [guardPos[0] + WALK_DIR[guardOri][0], guardPos[1] + WALK_DIR[guardOri][1]]
    if mapOfArea[nextPos[1]][nextPos[0]] == "#" :
        guard["orientation"] = TURN_DIR[guardOri]
    else : 
        guard["position"] = nextPos
        mapOfArea[guardPos[1]][guardPos[0]] = "X"
        if mapOfArea[nextPos[1]][nextPos[0]] != "X" : totalStops += 1
        
    stepCount += 1

print(f"Total Stops: {totalStops}")

def projectBack(map, position, orientation) :
    behindPos = [position[0] - WALK_DIR[orientation][0], position[1] - WALK_DIR[orientation][1]]
    leftPos = [behindPos[0] - WALK_DIR[TURN_DIR[orientation]][0], behindPos[1] - WALK_DIR[TURN_DIR[orientation]][1]]

    while behindPos[0] >= 0 and behindPos[0] < len(map[0]) and behindPos[1] >= 0 and behindPos[1] < len(map) :
        if map[behindPos[1]][behindPos[0]] != "#" :
            if map[behindPos[1]][behindPos[0]].find(orientation) == -1 :
                map[behindPos[1]][behindPos[0]] += orientation
            if leftPos[0] >= 0 and leftPos[0] < len(map[0]) and leftPos[1] >= 0 and leftPos[1] < len(map) :
                try :
                    if map[leftPos[1]][leftPos[0]] == "#" :
                        projectBack(map, behindPos, TURN_DIR[TURN_DIR[TURN_DIR[orientation]]])
                except : print(leftPos, behindPos, (len(map[0])-1, len(map)-1))
            behindPos = [behindPos[0] - WALK_DIR[orientation][0], behindPos[1] - WALK_DIR[orientation][1]]
            leftPos = [behindPos[0] - WALK_DIR[TURN_DIR[orientation]][0], behindPos[1] - WALK_DIR[TURN_DIR[orientation]][1]]
        else : return
    return


stepCount = 0
totalObstructions = 0
while guard2["position"][0] > 0 and guard2["position"][0] < len(mapOfArea2[0])-1 and guard2["position"][1] > 0 and guard2["position"][1] < len(mapOfArea2)-1 :
    guardPos = guard2["position"]
    guardOri = guard2["orientation"]
    nextPos = [guardPos[0] + WALK_DIR[guardOri][0], guardPos[1] + WALK_DIR[guardOri][1]]

    for char in mapOfArea2[guardPos[1]][guardPos[0]] :
        if char == TURN_DIR[guardOri] :
            totalObstructions += 1
            break

    if mapOfArea2[nextPos[1]][nextPos[0]] == "#" :
        guard2["orientation"] = TURN_DIR[guardOri]
    else : 
        guard2["position"] = nextPos
        mapOfArea2[guardPos[1]][guardPos[0]] = guardOri

    projectBack(mapOfArea2, guardPos, guardOri)
    
    


print(f"Total Obstructions: {totalObstructions}")


mapFile.close()
#P1
# 5599
# 5446
# 4978
#*4977
# 

#P2
# 11000something
#*
# 628
# 398
# 389