txt = open("input.txt")
txtinput = txt.read()
x = 0
y = 0
house = [str(x)+", "+str(y)]
for i, c in enumerate(txtinput):
    if c == "^":
        y+=1
    elif c == ">":
        x+=1
    elif c == "v":
        y-=1
    elif c == "<":
        x-=1
    else:
        print("unexpected char")
    xy = str(x)+", "+str(y)
    if house.count(xy) == 0:
        house.append(xy)
        print("new coords added: " + xy)
    else:
        print("coords skipped: " + xy)
    print("Total houses: " + str(len(house)))
