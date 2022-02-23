x = 3456

class Solution2:
    def reverse(x):
        xstr = str(x)
        pHolder = ''
        
        if x >= 0:
            for num in xstr[::-1]:
                pHolder += num
            if int(pHolder) >= 2147483647:
                return 0
            else:
                return int(pHolder)
        else:
            return -abs(Solution2.reverse(abs(x)))


print(Solution2.reverse(x))