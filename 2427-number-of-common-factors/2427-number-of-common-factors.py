import math
class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

        
        def factors(num):
            set1 = set()
            for i in range(1,int(math.sqrt(num)) + 1):
                if num%i == 0:
                    set1.add(i)
                    if num//i != i:
                        set1.add(num//i)
            
            return set1
        
        return len((factors(a)).intersection(factors(b)))