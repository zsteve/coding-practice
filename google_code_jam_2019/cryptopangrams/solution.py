import math

def decode(N, L, A):
    primes = set()
    message = list()
    # seek one prime from first element of A
    start_idx = 0
    while A[start_idx] == A[start_idx+1]:
        start_idx+=1
    p = math.gcd(A[start_idx], A[start_idx+1])  
    primes.add(p)
    q = A[0]//p
    primes.add(q) # so message is [..., q, p, ... ]
    message += [q, p, ]
    # go backwards first
    # message[0] contains the divisor to use for prev (bw)
    for i in range(start_idx-1, -1, -1):
        p = A[i]/message[0]
        message.insert(0, p)
        primes.add(p)
    # message[-1] contains the divisor to use for next (fw)
    for i in range(start_idx + 1, L):
        p = A[i]/message[-1]
        message += [p, ]
        primes.add(p)
    
    primetable = sorted(list(primes))
    d = dict()
    for i in range(0, len(primetable)):
        d[primetable[i]] = chr(ord('A')+i);
    
    message_decoded = str('');
    for p in message:
        message_decoded += d[p]
    return message_decoded

T = int(input())
ans = list()
for i in range(0, T):
    N, L = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    ans += ["Case #" + str(i+1) + ": " + decode(N, L, A), ]

for s in ans:
    print(s)

