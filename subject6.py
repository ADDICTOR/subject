def cal():
    n = 2
    count = 0
    while n <= 10000:
        i = n*3 + 1
        while i != 1:
            if i % 2 == 0:
                i /= 2
            else:
                i = i*3 + 1

            if i == n:
                count += 1
                break
        n += 1
    return count

if __name__ == "__main__":
    print(cal())