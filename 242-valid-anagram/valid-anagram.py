class Solution(object):
    def isAnagram(self, s, t):
        s_kv = {}
        t_kv = {}

        for char in s:
            s_kv[char] = s_kv.get(char, 0) + 1

        for char in t:
            t_kv[char] = t_kv.get(char, 0) + 1 
        return s_kv == t_kv