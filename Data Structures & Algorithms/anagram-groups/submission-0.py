class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt=dict()
        for string in strs:
            array=[0]*26
            print(strs.index(string))
            for a in string:
                indexx=ord(a)-97
                array[indexx]+=1
            if tuple(array)  in dictt:
                dictt[tuple(array)].append(string)
            else:
                dictt[tuple(array)]=[string]

        return (list(dictt.values()))


            

            
            
        




        
            
            

           



        