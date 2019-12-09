def processInstruction(ip, opCode, instruction):
    if opCode == 1 or opCode == 2: #add or mult
        a = memory[memory[ip+1]] if int(instruction.zfill(1)[-1]) == 0 else memory[ip+1]
        b = memory[memory[ip+2]] if int(instruction.zfill(2)[-2]) == 0 else memory[ip+2]
        memory[memory[ip+3]] = a + b if opCode == 1 else a * b
        ip += 4
    elif opCode == 3:
        memory[memory[ip+1]] = 1 #input
        ip += 2
    elif opCode == 4: #output
        output = memory[memory[ip+1]] if int(instruction.zfill(1)[-1]) == 0 else memory[ip+1]
        print(output)
        ip += 2
    return ip

with open('input05.txt') as file:
    memory = list(map(int, file.read().split(',')))

    ip = 0 #instruction pointer
    instruction = str(memory[ip])
    opCode = int(instruction[-2:])
    while opCode != 99:
        ip = processInstruction(ip, opCode, instruction[:-2])
        instruction = str(memory[ip])
        opCode = int(instruction[-2:])
