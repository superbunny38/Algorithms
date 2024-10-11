import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count_dict = dict()
        for task in tasks:
            if task not in count_dict:
                count_dict[task] = 1
            else:
                count_dict[task] +=1
        pq = []
        for key,value in count_dict.items():
            heapq.heappush(pq, (-value,key))

        ret = []
        # print("pq init:",pq)

        while pq:
            space_acc = 0

            need_to_insert_back = []
            while pq and space_acc-1<n:
                popped = heapq.heappop(pq)
                ret.append(popped[1])
                value = popped[0]
                # print("popped:",popped)
                # print("ret:",ret)
                if value+1 < 0:
                    need_to_insert_back.append((value+1,popped[1]))
                space_acc +=1
            
            for back in need_to_insert_back:
                heapq.heappush(pq,(back[0],back[1]))

            if space_acc-1 < n and pq:
                ret+= ['idle']*(n-space_acc+1)
            
        #     print("pq:",pq)
        # print("ret:",ret)
        return len(ret)
