# 백준 12904 A와 B
s = list(map(str, input()))
t = list(map(str, input()))

while len(s) != len(t):
    
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t.reverse()

if s == t:
    print(1)
else:
    print(0)