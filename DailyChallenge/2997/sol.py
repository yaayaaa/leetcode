class Solution:
    """
        the problem definition is to find the least steps of flipping one bit on number at a time of the list,
        to reach the input number k so what I did is that I XORed the list and counted the bits needing to be shifted
        and always the least number of steps is equal to the number of bits to be flipped.
    """

    def minOperations(self, nums: List[int], k: int) -> int:
        output_elements_xor_ed = reduce(lambda x, y: x ^ y, nums)
        output_xored_k = output_elements_xor_ed ^ k


        count = 0

        while output_xored_k:
            count += output_xored_k & 1
            output_xored_k >>= 1

        return count