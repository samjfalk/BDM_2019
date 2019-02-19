import fileinput
import sys

if __name__=='__main__':
    mySum = 0
    myLen = 0
    for line in fileinput.input():
        number = int(line.strip())
        mySum += number
        myLen += 1
    print(1.0*mySum/myLen)
