def calculate():
    for i in range(1000,10000):
        a = i // 1000
        b = i // 100 % 10
        c = i // 10 % 10
        d = i % 10
        if a*b*c*d == int(str(i)[::-1]):
            print(i)
        elif a*b*(c*10+d) == int(str(i)[::-1]):
            print(i)
        elif a*(b*10+c)*d == int(str(i)[::-1]):
            print(i)
        elif (a*10+b)*c*d == int(str(i)[::-1]):
            print(i)
        elif a*(b*100+c*10+d) == int(str(i)[::-1]):
            print(i)
        elif (a*100+b*10+c)*d == int(str(i)[::-1]):
            print(i)

if __name__ == "__main__":
    calculate()