with open('input06.txt') as file:
    orbits = {key: value for value, key in (row.strip().split(')') for row in file.readlines())}
    tot = 0
    for o in orbits:
        while True:
            tot += 1
            o = orbits[o]
            if o == 'COM':
                break
    print(tot)