# coding=utf-8

def is_sub(t1, w1):
    if len(t1) == len(w1):
        for key, val in t1.items():
            if key in w1 and w1[key] == val:
                pass
            else:
                return False
        return True
    return False


def main(s1, s2):
    target = {}
    ww = {}

    for i in range(len(s1)):
        c = s1[i]
        if c in target:
            target[c] +=1
        else:
            target[c] = 1
    
    for i in range(len(s2)):
        if i < len(s1):
            if s2[i] in ww:
                ww[s2[i]] +=1
            else:
                ww[s2[i]] =1
            
            if i == len(s1)-1:
                if is_sub(target, ww):
                    return True
        else:
            if s2[i] in ww:   # 给滑动窗口中添加尾元素
                ww[s2[i]] +=1
            else:
                ww[s2[i]] =1
            # 给滑动窗口移除之前的首元素
            j = i - len(s1)
            ww[s2[j]] -=1   
            if ww[s2[j]] == 0:
                del ww[s2[j]]   # 如果左边的字符串出现次数为 0，需要在窗口内删除该 字符
            
            if is_sub(target, ww):
                return True
    return False


if __name__ == '__main__':
    # s1 = "ab"
    # s2 = "eidbaooo"
    s1= "ab"
    s2 = "eidboaoo"

    res = main(s1, s2)
    print(res)
