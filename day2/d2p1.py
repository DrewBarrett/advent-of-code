txt = open("input.txt")
txtinput = txt.read()
# print(txtinput)
# print(txt.readlines())
l=-1
w=-1
h=-1
start = -1
for i,c in enumerate(txtinput):
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
        int sa = 2*l*w + 2*w*h + 2*l*h
        print (str(l) + "x" + str(w) + "x" + str(h))
        l = -1
        w = -1
        h = -1
