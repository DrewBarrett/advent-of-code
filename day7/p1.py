import sys

def negate(i):
    return 65535 - i
def main():
    assert(123 & 456 == 72)
    assert(123 | 456 == 507)
    assert(123 << 2 == 492)
    assert(456 >> 2 == 114)
    assert(negate(123) == 65412)
    assert(negate(456) == 65079)
    wires = {}
    for line in sys.stdin:
        print('looping...')
        # parse the line
        words = line.strip().split(" ")
        try:
            if words[0] <= '9' and words[0] >= '0':
                # first arg is a number
                # we are setting a signal
                wires[words[2]] = int(words[0])
            elif words[0] >= 'a' and words[0] <= 'z':
                # first arg is a wire
                if words[1] == "AND":
                    wires[words[4]] = wires.get(words[0]) & wires.get(words[2])
                elif words[1] == "OR":
                    wires[words[4]] = wires.get(words[0]) | wires.get(words[2])
                elif words[1] == "LSHIFT":
                    wires[words[4]] = wires.get(words[0]) << wires.get(words[2])
                elif words[1] == "RSHIFT":
                    wires[words[4]] = wires.get(words[0]) >> wires.get(words[2])
                else:
                    print("ERROR", words)
                    sys.exit(1)
            elif words[0] == "NOT":
                wires[words[3]] = negate(wires.get(words[2]))
            else:
                print("ERROR", words)
                sys.exit(1)
        except:
            print("ERROR", words)
    print(wires)
main()
