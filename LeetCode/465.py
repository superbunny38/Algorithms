class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        store_dict = dict()
        for transaction in transactions:
            p_from, p_to, amount = transaction[0],transaction[1],transaction[2]
            if p_from in store_dict:
                store_dict[p_from] -= amount
            else:
                store_dict[p_from] = -amount
            
            if p_to in store_dict:
                store_dict[p_to] += amount
            else:
                store_dict[p_to] = amount
                
        print("store_dict:",store_dict)
        Ns = [x for x in store_dict.values() if x<0]
        Ps = [x for x in store_dict.values() if x>0]
        print("Ps:",Ps)
        print("Ns:",Ns)
        
        def countWays(Negatives, Positives):
            if len(Negatives)+len(Positives) == 0:
                return 0
            
            negative = Negatives[0]
            n_count = float('inf')
            
            for positive in Positives:
                candi_positives = Positives.copy()
                candi_negatives = Negatives.copy()
                candi_negatives.remove(negative)
                candi_positives.remove(positive)
                append_value = negative + positive
                if append_value == 0:
                    pass
                else:
                    if abs(negative)>positive:
                        candi_negatives.append(append_value)
                    else:
                        candi_positives.append(append_value)
                n_count = min(countWays(candi_negatives,candi_positives),n_count)
            return n_count + 1 
        return countWays(Negatives=Ns,Positives=Ps)
