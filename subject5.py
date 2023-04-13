def divide(n):
    count = 0
    for a in range(3):
        for b in range(11):
            for c in range(16):
                for d in range(16):
                    if a + b + c + d <= 15:
                        if a*500 + b*100 + c*50 + d*10 == n:
                            count += 1
    return count

def divide1():
    pass

if __name__ == "__main__":
    print(divide(1000))