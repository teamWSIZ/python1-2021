def split(x):
    if x > 6:
        for a in range(x, -1, -1):
            if a % 3 == 0:
                b = x - a
                if b <= 6 and b > 3:
                    return a, b
    else:
        print("wpisz wieksza liczbe od 6")

if __name__ == '__main__':

    print(split(13))
