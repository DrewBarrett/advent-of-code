txt = open("input.txt")
txtinput = txt.read()
count = 0
start = -1
for i, c in enumerate(txtinput):
    if c != "\n" and start == -1:
        start = i
    if c == "\n":
        line = txtinput[start:i]
        print(line)
        firstletter = "0"
        secondletter = "0"
        test1 = False
        for letter in line:
            if firstletter == "0":
                firstletter = letter
            elif secondletter == "0":
                secondletter = letter
            elif firstletter == letter:
                test1 = True
                print("test 1 passed" + firstletter + secondletter + letter)
                firstletter = "0"
                secondletter = "0"
                break
            firstletter = secondletter
            secondletter = letter

print(str(count))
