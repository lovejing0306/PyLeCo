# coding=utf-8

def main(regions):
    # 对会议时间进行排序
    regions.sort(key=lambda x : (x[0], x[1]))
    count = 0
    visited = [False] * len(regions)
    i = 0
    while i < len(regions):
        if visited[i]:
            i+=1
        else:
            x1, y1 = regions[i]
            j = i+1
            while j < len(regions):
                if visited[j]:
                    j += 1
                else:
                    x2, y2 = regions[j]
                    x = max(x1, x2)
                    y = min(y1, y2)
                    if x<y:
                        j+=1
                    else:  # 如果会议不重叠，需要合并会议时间
                        visited[j] = True
                        x1 = min(x1, x2)
                        y1 = max(y1, y2)
                        j+=1
            i+=1
            count += 1
    return count



if __name__ == '__main__':
    rr = [[0, 30],[5, 10],[15, 20]]
    # rr = [[7,10],[2,4]]
    res = main(rr)
    print(res)