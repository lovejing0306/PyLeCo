# coding=utf-8

def main(ransomNote, magazine):
    rr = [0] * 26
    mm = [0] * 26

    for c in ransomNote:
        rr[ord(c)-ord('a')] +=1
    for c in magazine:
        mm[ord(c)-ord('a')] +=1
    
    for c1, c2 in zip(rr, mm):
        if c1 > c2:
            return False
    return True


if __name__ == '__main__':
    ransomNote = "aa"
    magazine = "aab"
    res = main(ransomNote, magazine)
    print(res)
