class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = [0] * len(gain)
        res = 0
        for i in range(len(gain)):
            res+=gain[i]
            alt.append(res)
        return(max(alt))
