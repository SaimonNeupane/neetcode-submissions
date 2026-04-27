class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        for i in range (len(strs[0])):
            if not strs[0]:
                return res
            temp=strs[0][i]
            for each in strs:
                if not each or i>=len(each) or temp not in each[i] :
                    return res
            res+=temp

        return res