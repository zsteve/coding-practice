T = int(input())
ans = list()
for i in range(0, T):
    N = int(input())
    P = input()
    Q = ''
    for i in range(0, len(P)):
       Q += ('S' if P[i] == 'E' else 'E')
    ans += [Q, ]

for i in range(0, len(ans)):
    print("Case #" + str(i+1) + ": " + ans[i])
