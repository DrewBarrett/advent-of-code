txt = open("input.txt")
txtinput = txt.read()
# print(txtinput)
# print(txt.readlines())
l = -1
w = -1
h = -1
start = -1
total = 0
line = 1
for i, c in enumerate(txtinput):
    # print(c)
    if c != "\n" and c != "x":
        if start == -1:
            start = i
    if c == "x":
        beforex = txtinput[int(start):int(i)]
        start = -1
        # print(beforex)
        if l == -1:
            l = beforex
        elif w == -1:
            w = beforex
        elif h == -1:
            h = beforex
        else:
            print("error no open variable")
        start = -1
    if c == "\n":
        beforen = txtinput[int(start):int(i)]
        start = -1
        if h == -1:
            h = beforen
        bow = int(w) * int(h) * int(l)
        # extra = int(l)*int(w)
        # if int(w)*int(h) < extra:
        #     extra = int(w)*int(h)
        # elif int(l)*(h) < extra:
        #     extra = int(l)*int(h)
        ribbon = min(int(l) * 2 + int(w) * 2, int(w) * 2 + int(h) * 2, int(l) * 2 + int(h) * 2)
        total += bow + ribbon
        print (str(l) + "x" + str(w) + "x" + str(h) + " bow: " + str(bow) + " ribbon: " + str(ribbon) + " total: " + str(total) + " line: " + str(line))
        line += 1
        l = -1
        w = -1
        h = -1
print(total)
