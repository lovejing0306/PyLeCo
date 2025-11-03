# coding=utf-8

def main(bills):
    nums = [0, 0, 0]
    for bill in bills:
        if bill == 5:
            nums[0] += 1
        elif bill == 10:
            if nums[0] == 0:
                return False
            else:
                nums[1] += 1
                nums[0] -= 1
        elif bill == 20:
            if nums[0] == 0 or nums[1] == 0:
                return False
            else:
                nums[2] += 1
                nums[1] -= 1
                nums[0] -= 1
    return True


if __name__ == '__main__':
    bills = [5,5,10,10,20]
    res = main(bills)
    print(res)
