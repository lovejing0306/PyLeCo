# coding=utf-8

def main(nums, n):
    """ 
    数组nums中给定可以使用的1~9的数，返回由nums数组中的元素组成的小于n（n > 0）的最大数。
    例如：nums = {1, 2, 4, 9}，n = 2533，返回2499。
    """
    nums = sorted(nums)
    s = str(n)
    result = []
    
    def dfs(pos, is_limit, is_num):
        if pos == len(s):
            return ''.join(result) if is_num else ''
        
        if not is_limit:
            # 可以选择最大的数字填满剩余位置
            max_digit = max(nums)
            return ''.join(result) + str(max_digit) * (len(s) - pos)
        
        # 当前位置的上界
        up = int(s[pos]) if is_limit else 9
        
        # 尝试从大到小选择数字
        for num in reversed(nums):
            if num > up:
                continue
            
            result.append(str(num))
            
            if num < up:
                # 选择了比上界小的数，后面可以随意选
                res = dfs(pos + 1, False, True)
                if res:
                    return res
            else:
                # 选择了上界，继续受限
                res = dfs(pos + 1, True, True)
                if res:
                    return res
            
            result.pop()
        
        # 如果所有数字都比上界大，尝试构造位数更少的数
        if pos == 0 and len(s) > 1:
            # 构造位数少一位的最大数
            max_digit = max(nums)
            return str(max_digit) * (len(s) - 1)
        
        return ''
    
    ans = dfs(0, True, False)
    return int(ans) if ans else 0

if __name__ == '__main__':
    nums = [2, 4, 9]
    n = 23121
    res = main(nums, n)
    print(res)