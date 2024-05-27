class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)

        # Start from the last digit
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        
        # If all digits were 9, we need an extra leading 1
        return [1] + digits
    
add = Solution()
print(add.plusOne([3, 5, 9]))
print(add.plusOne([9]))