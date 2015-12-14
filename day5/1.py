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
        twice = 0
        three = 0
        start = -1
        if line.find("ab") == -1 and line.find("cd") == -1 and line.find("pq") == -1 and line.find("xy") == -1:
            lastletter = "0"
            for letter in line:
                if lastletter == "0":
                    lastletter = letter
                else:
                    if lastletter == letter:
                        twice = 1
                        print("double letters true")
                        break;
                    lastletter = letter
            if line.count("a") + line.count("e") + line.count("i") + line.count("o") + line.count("u") >= 3:
                three = 1
                print("three vowels true")
            if three and twice:
                count += 1
                print("string accepted, total: " + str(count))
print(str(count))
