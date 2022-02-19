def visible_mountain_landscape(D, H) -> list[int]:
    if len(D) == 0:
        return []
    visible = [0]

    for i in range(1, len(D)):
        if D[i] / H[i] < D[visible[-1]] / H[visible[-1]]:
            visible.append(i)
    return visible


if __name__ == '__main__':
    print(visible_mountain_landscape([1, 2, 4, 8, 16], [5, 5, 24, 80, 160]))
    print(visible_mountain_landscape([1, 10], [1, 11]))
