# coding=utf-8

def main(nums, target):
    l = 0
    r = len(nums)-1

    while l <= r:
        m = l + (r-l) // 2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m+1
        else:
            r = m-1
    return -1


if __name__ == '__main__':
    a = [1,2,3,4,7,9]
    target = 7
    print(main(a, target))
