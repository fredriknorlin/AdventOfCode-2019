with open('input01.txt') as file:
    print(sum([int(i)//3 - 2 for i in file]))