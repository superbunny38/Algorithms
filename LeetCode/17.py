class Solution:
    def recursive(self, storage, nth, acc):
        print("nth:",nth)
        
        self.check[nth] = True
        for letter in storage[nth]:
            print("acc+letter:",acc+letter)
            if nth == len(storage)-1:
                self.ret.append(acc+letter)
                
            else:
                self.recursive(storage,nth+1,acc+letter)
    
    def letterCombinations(self, digits):
        length = len(digits)
        self.ret = []
        self.check = [False]*length
        print(self.check)
        if length == 0:
            return self.ret

        d = {2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
        storage = []
        
        for digit in digits:
            storage.append(d[int(digit)])
        print("storage:",storage)
        self.recursive(storage, 0, "")
        return self.ret
