class RangeModule:

    def __init__(self):
        self.ranges = []

    def addRange(self, left, right):
        i = 0
        new_ranges = []
        while i<len(self.ranges) and self.ranges[i][1] < left:
            new_ranges.append(self.ranges[i])
            i+=1
        
        while i< len(self.ranges) and self.ranges[i][0] <= right:
            left = min(self.ranges[i][0], left)
            right = max(self.ranges[i][1], right)
            i+=1
        new_ranges.append([left, right])

        while i<len(self.ranges):
            new_ranges.append(self.ranges[i])
            i+=1
        self.ranges = new_ranges

    def queryRange(self, left, right):
        for l , r in self.ranges:
            if left >=l and right <= r:
                return True
        return False

    def removeRange(self, left, right):
        new_ranges = []

        for l, r in self.ranges:
            if r < left:
                new_ranges.append([l, r])
            elif l > right:
                new_ranges.append([l, r])
            else:
                if l < left:
                    new_ranges.append([l, left])
                if right < r:
                    new_ranges.append([right, r])
        self.ranges = new_ranges


if __name__ == '__main__':
    range_ = RangeModule()
    range_.addRange(10, 20)
    range_.removeRange(14, 16)
    print(range_.queryRange(10, 14))
    print(range_.queryRange(13, 15))
    print(range_.queryRange(16, 17))
