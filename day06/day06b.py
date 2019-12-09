with open('input06.txt') as file:
    orbits = {key: value for value, key in (row.strip().split(')') for row in file.readlines())}

    o = 'YOU'
    l1 = []
    while True:
        o = orbits[o]
        l1.append(o)
        if o == 'COM':
            break
    
    count = 0
    o = 'SAN'
    firstCommonOrbit = ""
    while True:
        o = orbits[o]
        if o in l1:
            firstCommonOrbit = o
            break
        count += 1
        
    for l in l1:
        if l == firstCommonOrbit:
            break
        count += 1

    print(count)
        