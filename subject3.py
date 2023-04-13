def flop():
    lis = [False]*100
    for i in range(1,50):
        n = i
        while n <= 99:
            lis[n] = not lis[n]
            n += i+1
    for i in range(50,100):
        lis[i] = not lis[i]
    for i in range(100):
        if not lis[i]:
            print(i+1)

if __name__ == "__main__":
    flop()