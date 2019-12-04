def getWire(rawWire):
    x = 0
    y = 0
    wire = []

    for section in rawWire:
        direction = section[0]
        for _ in range(int(section[1:])):
            if direction == 'U':
                y += 1
            if direction == 'D':
                y -= 1
            if direction == 'L':
                x -= 1
            if direction == 'R':
                x += 1
            wire.append((x,y))
    return wire

with open("input03.txt") as file:
    rawWires = [row.strip().split(',') for row in file.readlines()]

    wire1 = getWire(rawWires[0])
    wire2 = getWire(rawWires[1])    
    
    intersections = set(wire1).intersection(wire2)
    intersectionDistances = list(map(lambda x: wire1.index(x)+wire2.index(x)+2, intersections))

    print(min(intersectionDistances))
