class Solution:
    def climbStairs(self, n: int) -> int:
        # init = 1
        # 1 ===> 1
        # 2 ===> addition of prev two
        # 3 ===> addiition of prev two
        # 4 --> (1,1,1,1) (1,1,2) (2,1,1) (1,2,1) (2,2) ===> 5 ways
        # 5 --> (1,1,1,1,1) (1,1,1,2) (1,1,2,1) (1,2,1,1) (2,1,1,1)
        #       (1,2,2) (2,1,2) (2,2,1)===> 8 ways
        # 6 --> (1,1,1,1,1,1) (1,1,1,1,2) (1,1,1,2,1) (1,1,2,1,1)
        #       (1,2,1,1,1) (2,1,1,1,1) (1,1,2,2) (1,2,1,2) (2,1,1,2)
        #       (2,1,2,1) (2,2,1,1) (2,2,2) ===> 13 ways
        # 7 ===> 21 ways
        # 8 ===> 34 ways
        # 9 ===> 55


        # so basically fibonacci!!

        prev2 = 1
        if n == 1:
            return 1
        prev1 = 1

        for i in range(n-1):
            new = prev1 + prev2
            prev2 = prev1
            prev1 = new
        
        return new
        

        
        