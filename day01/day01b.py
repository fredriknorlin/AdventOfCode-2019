def f(n):
    if n//3-2 < 1:
        return 0
    return f(n//3-2) + n//3-2

with open('input01.txt') as file:
    print(sum([f(int(i)) for i in file]))