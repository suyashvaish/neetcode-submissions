class Solution:
    def hasDuplicate(self, num: list[int]) -> bool:
        hash = set()
        for i in num:
            if i in hash:
                return True
            hash.add(i)
        return False
                
      
            
       