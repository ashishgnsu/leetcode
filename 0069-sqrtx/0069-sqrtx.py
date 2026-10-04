class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1 :
            return x
        if x == 2 or x==3:
            return 1

        left = 2
        right =x//2

        while left <= right:
            mid = left + (right-left)//2
            square = mid * mid
            if square == x:
                return mid
            elif(square < x):
                ans = mid       
                left = mid + 1
            else:
                right = mid - 1
                
        return ans




        for i in range(2,(x//2)+1):
            if (i * i) == x:
                return i
            elif ((i+1) * (i+1)) > x:
                return i


