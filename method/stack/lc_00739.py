# coding=utf-8

def main(array):
    if array is None or len(array) == 0:
        return []

    res = [0] * len(array)
    stack = []
    for cur_index in range(len(array)):
        while len(stack) > 0:
            last_index = stack[-1]
            if array[cur_index] > array[last_index]:
                res[last_index] = cur_index - last_index
                stack.pop()
            else:
                break
        stack.append(cur_index)
    return res


if __name__ == '__main__':
    a = [73,74,75,71,69,72,76,73]
    print(main(a))