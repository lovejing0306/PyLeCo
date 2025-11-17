# coding=utf-8

def main(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    x1 = max(ax1, bx1)
    y1 = max(ay1, by1)
    x2 = min(ax2, bx2)
    y2 = min(ay2, by2)

    area1 = (ax2 - ax1) * (ay2-ay1)
    area2 = (bx2 - bx1) * (by2-by1)

    if x1 < x2 and y1 < y2:
        iou = (x2-x1) * (y2-y1)
        area = area1 + area2 -iou
    else:
        area = area1 + area2
    return area

if __name__ == '__main__':
    ax1 = -3
    ay1 = 0
    ax2 = 3
    ay2 = 4
    bx1 = 0
    by1 = -1
    bx2 = 9
    by2 = 2

    res = main(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
    print(res)