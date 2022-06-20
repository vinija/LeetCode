class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = {}
        left = 0

        for right, value in enumerate(fruits):
            count[value] = count.get(value,0)+1
            
            if len(count) >2:
                count[fruits[left]] -=1
                if count[fruits[left]] == 0: del count[fruits[left]]
                left +=1
                
        
        return right - left +1
            

   