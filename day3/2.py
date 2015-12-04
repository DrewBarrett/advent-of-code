txt = open("input.txt")
txtinput = txt.read()
x1 = 0
y1 = 0
x2 = 0
y2 = 0
house = [str(0) + ", " + str(0)]
for i, c in enumerate(txtinput):
    y = 0
    x = 0
    if c == "^":
        y += 1
    elif c == ">":
        x += 1
    elif c == "v":
        y -= 1
    elif c == "<":
        x -= 1
    else:
        print("unexpected char")
    if i % 2 == 0:
        x1 += x
        y1 += y
        x = x1
        y = y1
    else:
        x2 += x
        y2 += y
        x = x2
        y = y2
    xy = str(x) + ", " + str(y)
    if house.count(xy) == 0:
        house.append(xy)
        print("new coords added: " + xy)
    else:
        print("coords skipped: " + xy)
    print("Total houses: " + str(len(house)))
