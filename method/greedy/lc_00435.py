# coding=utf-8

def main(regions):
    if not regions:
        return 0
    
    regions.sort(key=lambda p:p[1])

    count = 0
    x1, y1 = regions[0]
    for i in range(1, len(regions)):
        x2, y2 = regions[i]
        x = max(x1, x2)
        y = min(y1, y2)
        if x < y:
            x1 = x
            y1 = y
        else:
            count+=1
            x1 = x2
            y1 = y2
    count += 1
    return len(regions) - count


if __name__ == '__main__':
    intervals = [[1,2],[2,3],[3,4],[1,3]]
    res = main(intervals)
    print(res)