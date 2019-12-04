import re

with open('input04.txt') as file:
    bounds = list(map(int, file.read().split('-')))
    
    count = 0
    for i in range(bounds[0], bounds[1]):
        if all(re.search(regex, str(i)) for regex in [r'^\d{6}$', r'(\d)\1+', r'^0*1*2*3*4*5*6*7*8*9*$']):
            count += 1
    print(count)