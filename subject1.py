def palindrome():
    n = 11
    while True:
        n_s = str(n)
        n_sr = n_s[::-1]
        if n_s == n_sr:
            n2_s = bin(n)[2:]
            n2_sr = n2_s[::-1]
            if n2_s == n2_sr:
                n8_s = oct(n)[2:]
                n8_sr = n8_s[::-1]
                if n8_s == n8_sr:
                    print(n)
                    break
        n+=1

if __name__ == "__main__":
    palindrome()
    