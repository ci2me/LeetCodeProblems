# TASK
# Given a string s, find the length of the longest 
# substring without repeating characters

# First Solution
# High Time Complexity
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         longest = 0
#         string = ''
#         # for every index
#         for i in range(len(s)):
#             k = i
#             j = k+1
#             string = ''
#             while j <= len(s):
#                 if (s[k] in string):
#                     length = len(string)
#                     if length > longest:
#                         longest = length
#                     string = ''
#                 else:
#                     string = string + s[k]
#                     length = len(string)
#                     if length > longest:
#                         longest = length
#                 k = k + 1
#                 j = k + 1
#         return longest


# Better sliding window solution
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # initialise a set
        char_set = set()
        left = 0
        longest = 0
        
        # start window
        for right in range(len(s)):
            # if the character is in the set, remove characters from the left until it isnt repeated
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            # add the current character to the set
            char_set.add(s[right])
            length = right - left + 1
            # find the longest
            if length > longest:
                longest = length
        
        return longest
