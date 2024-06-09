from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        prefix_sum_mod_count = {0: 1}
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num
            mod = prefix_sum % k

            if mod < 0:
                mod += k

            if mod in prefix_sum_mod_count:
                count += prefix_sum_mod_count[mod]
                prefix_sum_mod_count[mod] += 1
            else: 
                prefix_sum_mod_count[mod] = 1

        return count