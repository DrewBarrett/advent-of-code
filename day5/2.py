# Pair of 2 letters that appears twice without overlapping
# xyxy: yes
# aaa: no
def test1(string):
    nextCharPos = 1
    for char in string:
        if nextCharPos < len(string):
            pair = char + string[nextCharPos]
            restOfString = string[nextCharPos + 1:]
            if pair in restOfString:
                print("test 1 passed!")
                return True
        nextCharPos += 1
    return False

# contains a letter that repeats with one letter in between it
# ie aaa xyx efe
def test2(string):
    currPos = 0
    FWD_AMT = 2 # How far forward do we go to get the char we ewant to compare
    for char in string:
        # check if char to compare is even in the string
        if currPos + FWD_AMT < len(string):
            # do the comparison
            if char == string[currPos + FWD_AMT]:
                print("test 2 passed!")
                return True
        currPos += 1
    return False

def main():
    count = 0
    with open("input.txt") as f:
        content = f.read()
    for line in content.splitlines():
        print(line)
        if test1(line) and test2(line):
            count += 1
    print(count)
    return

main()
