class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        my_dic = {}
        for n in nums1:
            if n in my_dic:
                my_dic[n] += 1
            else:
                my_dic[n] = 1
        
        for i in nums2:
            if i in my_dic and my_dic[i]!=0:    # Count should not equals to zero because its mean it is now present in nums1, if it is not present in nums1 but present in nums2, we cannot add it to result.  
                my_dic[i] -= 1
                result.append(i)
        
        return result
        