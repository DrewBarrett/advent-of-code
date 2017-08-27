# day6part1.py
ON = 'on'
OFF = 'off'
TOGGLE = 'toggle'
SIZE = 1000

def switch(line, lights):
    split = line.split()
    coords = []
    for word in split:
        if "," in word:
            coords.extend(word.split(","))
    currX, currY, endX, endY = coords
    currX = int(currX)
    currY = int(currY)
    endX = int(endX)
    endY = int(endY)
    startX = currX
    count = 0
    while currY <= endY:
        while currX <= endX:
            target = True
            if OFF in line:
                target = False
            elif TOGGLE in line:
                target = not lights[currX][currY]
            lights[currX][currY] = target
            count += 1
            #print(currX, currY, "is now", target)
            currX += 1
        currY += 1
        currX = startX
    print("Changed", count, "lights")
    return lights

def main():
    lights = [[False for x in range(SIZE)] for y in range(SIZE)]
    with open("input.txt") as f:
        content = f.read()
    for line in content.splitlines():
        print(line)
        lights = switch(line, lights)
    count = 0
    for y in lights:
        for x in y:
            if x == True:
                count += 1
    print(count)
    return

main()
