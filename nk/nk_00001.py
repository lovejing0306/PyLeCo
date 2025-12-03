# coding=utf-8

def main(intervals):
    if intervals is None or len(intervals) == 0:
        return []
    
    intervals.sort(key=lambda x: (x[0], x[1]))
    
    stack = []
    for i in range(len(intervals)):
        if len(stack) == 0:
            stack.append(intervals[i])
        else:
            x1, y1 = stack[-1]
            x2, y2 = intervals[i]

            x = max(x1, x2)
            y = min(y1, y2)

            if x <= y:
                stack.pop()
                x = min(x1, x2)
                y = max(y1, y2)
                stack.append([x, y])
            else:
                stack.append(intervals[i])
    return stack


if __name__ == '__main__':
    intervals = [[2,6], [1,3],[8,10],[15,18]]
    res = main(intervals)
    print(res)