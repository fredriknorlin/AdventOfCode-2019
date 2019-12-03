def f(memory, n, v):
    memory[1] = n
    memory[2] = v

    ip = 0 #instruction pointer
    instruction = memory[ip]
    
    while instruction != 99:
        if instruction == 1:
            memory[memory[ip+3]] = memory[memory[ip+1]] + memory[memory[ip+2]]
        elif instruction == 2:
            memory[memory[ip+3]] = memory[memory[ip+1]] * memory[memory[ip+2]]
        ip += 4
        instruction = memory[ip]
    return memory[0]

with open('input02.txt') as file:
    memory = list(map(int, file.read().split(',')))
    
    for noun in range(100):
        for verb in range(100):
            if f(memory.copy(), noun, verb) == 19690720:
                print(100*noun + verb)
                break
        else:
            continue
        break
                