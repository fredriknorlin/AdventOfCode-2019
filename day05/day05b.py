def processInstruction(ip, opCode, instruction):
    if opCode == 1 or opCode == 2: #add or mult
        a = memory[memory[ip+1]] if int(instruction.zfill(1)[-1]) == 0 else memory[ip+1]
        b = memory[memory[ip+2]] if int(instruction.zfill(2)[-2]) == 0 else memory[ip+2]
        if opCode == 1:
            memory[memory[ip+3]] = a + b  
        if opCode == 2:
            memory[memory[ip+3]] = a * b
        ip += 4
    elif opCode == 3: #input
        memory[memory[ip+1]] = 5 
        ip += 2
    elif opCode == 4: #output
        output = memory[memory[ip+1]] if int(instruction.zfill(1)[-1]) == 0 else memory[ip+1]
        print(output)
        ip += 2
    elif opCode == 5 or opCode == 6: #jump
        a = memory[memory[ip+1]] if int(instruction.zfill(1)[-1]) == 0 else memory[ip+1]
        b = memory[memory[ip+2]] if int(instruction.zfill(2)[-2]) == 0 else memory[ip+2]
        if opCode == 5: #if true
            ip = b if a != 0 else ip + 3
        if opCode == 6: #if false
            ip = b if a == 0 else ip + 3        
    elif opCode == 7 or opCode == 8: #compare
        a = memory[memory[ip+1]] if int(instruction.zfill(1)[-1]) == 0 else memory[ip+1]
        b = memory[memory[ip+2]] if int(instruction.zfill(2)[-2]) == 0 else memory[ip+2]
        if opCode == 7: #less than
            memory[memory[ip+3]] = 1 if a < b else 0
        if opCode == 8: #equals
            memory[memory[ip+3]] = 1 if a == b else 0
        ip += 4
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
