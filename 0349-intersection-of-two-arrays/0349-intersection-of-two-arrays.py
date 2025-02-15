class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        my_dic = {}
        for num in nums1:
            if num in my_dic:
                my_dic[num] += 1
            else:
                my_dic[num] = 1
        for i in nums2:
            if i in my_dic and my_dic[i] != 0:
                result.append(i)
                my_dic[i] = 0
        
        return result
        