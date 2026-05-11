import random
class RandomizedSet:

    def __init__(self):
        self.value = []
        self.indexMap = {}       

    def insert(self, val: int) -> bool:
        if val  in self.indexMap: 
            return False
        self.value.append(val)    
        self.indexMap[val] = len(self.value) -1
        return True    

    def remove(self, val: int) -> bool:
        if val not in self.indexMap:
            return False
        ind = self.indexMap[val]
        last_val = self.value[-1]
        self.value[ind] = last_val    
        self.indexMap[last_val] = ind   
        self.value.pop()                  
        del self.indexMap[val]            
        return True
        
    def getRandom(self) -> int:
        return self.value[random.randrange(len(self.value))]
