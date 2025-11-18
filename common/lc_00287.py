# coding=utf-8

def main(nums):
    counter = set()
    for num in nums:
        if num in counter:
            return num
        counter.add(num)
    return None


if __name__ == '__main__':
    nums = [1,3,4,2,2]
    print(main(nums))