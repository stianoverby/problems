"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.

"""

from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # Offset in the letter -> occurences maps
        ASCII_offset = 97
        
        # s1 can not be contained in s2 if it is larger
        if len(s1) > len(s2): return False
        
        # Maps from letters to number of occurrences as a natural number
        s1_map = [0] * 26 
        s2_map = [0] * 26
        
        # Count every letter in both strings
        for i in range(len(s1)):
            s1_map [ord(s1[i]) - ASCII_offset] += 1 
            s2_map [ord(s2[i]) - ASCII_offset] += 1 
        
        # A sliding window that matches the length of s1 over s2.
        for i in range(len(s2)- len(s1)):
            
            # if the maps are equal, then we have found a substring that cointains a permutation of s1
            if s1_map == s2_map: return True
            
            # right shift the window
            s2_map [ord(s2[i]) - ASCII_offset] -= 1 
            s2_map [ord(s2[i + len(s1)]) - ASCII_offset] += 1 
        
        return s1_map == s2_map
      
      
