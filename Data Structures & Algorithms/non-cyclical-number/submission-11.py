class Solution:
    def isHappy(self, n: int) -> bool:
        sett={1}
        temp=n 
        while True:
            print(f'{temp}')
            print(sett)
            listt=list(str(temp))
            if temp == 1:
                return True
            elif temp in sett:
                return False
            else:
                sett.add(temp)
            num=0
            for a in listt:
                num=num+int(a)**2
            temp=num
            
            
        


        