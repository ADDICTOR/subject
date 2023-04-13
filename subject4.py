def cut1(n,m,i):
    if i <= m:
        return 1 + cut1(n,m,i*2)
    elif i < n:
        return 1 + cut1(n,m,i+m)
    else:
        return 0

def cut2(n,m):
    i = 1
    while 2**i < m:
        i += 1
    j = (n - 2**i) // m + 1
    return i + j

if __name__ == "__main__":
    print(cut1(20,3,1))
    print(cut1(100,5,1))
    print(cut2(20,3))
    print(cut2(100,5))