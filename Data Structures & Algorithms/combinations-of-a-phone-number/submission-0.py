class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        res,sol=[],[]
        dictt= {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
            }   
        def backtrack(i):
            if len(sol)==len(digits):
                res.append("".join(sol))
                return
            for digit in dictt[digits[i]]:
                print(digit)
                sol.append(digit)
                backtrack(i+1)
                sol.pop()
        backtrack(0)
        return res
                