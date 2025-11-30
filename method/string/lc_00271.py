# coding=utf-8

class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        """
        result = []
        for s in strs:
            result.append(str(len(s)) + '#' + s)
        return ''.join(result)

    def decode(self, s):
        """Decodes a single string to a list of strings.
        """
        result = []
        i = 0
        while i < len(s):
            # 找到 '#' 的位置
            j = i
            while s[j] != '#':
                j += 1
            # 获取长度
            length = int(s[i:j])
            # 获取字符串
            result.append(s[j+1:j+1+length])
            # 移动指针
            i = j + 1 + length
        return result


def main():
    """ 
    请你设计一个算法，可以将一个 字符串列表 编码成为一个 字符串。
    这个编码后的字符串是可以通过网络进行高效传送的，并且可以在接收端被解码回原来的字符串列表。
    """
    codec = Codec()
    strs = ["Hello","World"]
    res = codec.encode(strs)
    print(res)
    print(codec.decode(res))


if __name__ == '__main__':
    main()