# Pair of 2 letters that appears twice without overlapping
# xyxy: yes
# aaa: no
def test1(string):
    nextCharPos = 1
    for char in string:
        if nextCharPos < len(string):
            pair = char + string[nextCharPos]
            print (pair)
        nextCharPos += 1

def main():
    with open("input.txt") as f:
        content = f.read()
    for line in content.splitlines():
        print(line)
        test1(line)
    return

main()
