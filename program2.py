class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Dictionary to map Roman numerals to integers
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        length = len(s)
        
        # Traverse each character in the string
        for i in range(length):
            # If current character is less than the next character, subtract it
            if i < length - 1 and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                total -= roman_to_int[s[i]]
            else:
                # Otherwise, add it to the total
                total += roman_to_int[s[i]]
        
        return total




