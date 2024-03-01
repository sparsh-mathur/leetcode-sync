class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s=list(s)
        countZeros=0
        countOnes=0
        for val in s:
            if val=='0': countZeros+=1
            else: countOnes+=1
        return ((countOnes-1)*'1')+(countZeros*'0')+'1'