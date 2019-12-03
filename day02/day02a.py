with open('input02.txt') as file:
    intcode = list(map(int, file.read().split(',')))
    intcode[1] = 12
    intcode[2] = 2

    cursor = 0
    opCode = intcode[cursor]
    while opCode != 99:
        if opCode == 1:
            intcode[intcode[cursor+3]] = intcode[intcode[cursor+1]] + intcode[intcode[cursor+2]]
        elif opCode == 2:
            intcode[intcode[cursor+3]] = intcode[intcode[cursor+1]] * intcode[intcode[cursor+2]]
        cursor += 4
        opCode = intcode[cursor]

    print(intcode[0])