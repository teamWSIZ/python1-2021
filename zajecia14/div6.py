
def split(x: int) -> tuple[int, int]:
    k3 = x // 3
    rest = x - k3 * 3
    # print(f'k3={k3}, k3*3={k3*3} rest={rest}')
    while rest <= 3:
        rest += 3
        k3 -= 1
    return (k3*3, rest)

if __name__ == '__main__':
    print(split(10**18))