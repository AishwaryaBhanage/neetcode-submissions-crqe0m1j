class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            count[num] = count.get(num,0)+1
        
        for n,i in count.items():
            freq[i].append(n)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        # dictt = {} 
        # lst = []

        # # for n in nums:
        # #     dictt[n] = 1 + dictt.get(n,1)

        # for i in nums:
        #     if i in dictt:
        #         dictt[i] += 1
        #     else:
        #         dictt[i] = 1

        # sort_dic = dict(sorted(dictt.items(), key=lambda x:x[1], reverse = True)[:k])

        # return (list(sort_dic.keys()))

        