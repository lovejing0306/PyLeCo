# coding=utf-8

def main(points):
    max_v = 0

    for i in range(len(points)):
        mapping_1 = {}  # 存放斜率无效的情况
        mapping_2 = {}
        for j in range(len(points)):
            if i == j:
                continue
            x1, y1 = points[i]
            x2, y2 = points[j]

            if x1 == x2:
                if x1 in mapping_1:
                    mapping_1[x1] += 1
                else:
                    mapping_1[x1] = 1
                max_v = max(max_v, mapping_1[x1])
            else:
                k = (y2-y1) / (float(x2)-float(x1))
                if k in mapping_2:
                    mapping_2[k] +=1
                else:
                    mapping_2[k] = 1
                max_v = max(max_v, mapping_2[k])
    return max_v + 1


if __name__ == '__main__':
    points = [[1,1],[2,2],[3,3]]
    res = main(points)
    print(res)
        
