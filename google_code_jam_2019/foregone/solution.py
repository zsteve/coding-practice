T = int(input())
solutions = list()
for i in range(0, T):
    N = int(input())
    # unravel N
    R = list() # coefficients of 10^[0, 1, 2, 3.. ]
    while(N > 0):
        R += [N % 10, ]
        N = N//10
    print(R)
    P = [0, ]*len(R)
    print(P)
    for i in range(0, len(R)):
        if R[i] == 4:
            R[i] = 2;
            P[i] = 2;
        print(R)
        print(P)
    r = sum([R[i]*(10**i) for i in range(0, len(R))])
    p = sum([P[i]*(10**i) for i in range(0, len(P))])
    solutions += [(r, p), ]

for i in range(0, len(solutions)):
    print("Case #" + str(i+1) + ": " + str(solutions[i][0]) + " " + str(solutions[i][1]))
