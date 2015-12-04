txt = open("input.txt")
txtinput = txt.read()
print(txtinput)

level = 1
for i, c in enumerate(txtinput):
    if c == "(":
        level += 1
    elif c == ")":
        level -= 1
    else:
        print(str(i)+str(c) + "error")
    if level == -1:
        print(str(level) + " " + str(i))
        break
