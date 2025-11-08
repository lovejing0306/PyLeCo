# coding=utf-8


def main(regions):
    regions.sort(key=lambda p : p[1])
    
    visited = [False] * len(regions)
    count = 0
    for i in range(len(regions)):
        if visited[i]:
            continue
        count += 1
        x1 = regions[i][0]
        y1 = regions[i][1]
        j = i + 1
        while j < len(regions):
            x2 = regions[j][0]
            y2 = regions[j][1]
            x = max(x1, x2)
            y = min(y1, y2)
            if x <= y:
                x1 = x
                y1 = y
                visited[j] = True
            j += 1
    return count


def method2(regions):
    if not regions:
        return 0
    regions.sort(key=lambda p : p[1])

    count = 0
    x1, y1 = regions[0]
    for i in range(1, len(regions)):
        x2, y2 = regions[i]
        x = max(x1, x2)
        y = min(y1, y2)
        if x <= y:
            x1 = x
            y1 = y
        else:
            count+=1
            x1 = x2
            y1 = y2
    count += 1
    return count


if __name__ == '__main__':
    points = [[1,5],[4,8],[2,3],[6,7]]
    res = main(points)
    print(res)