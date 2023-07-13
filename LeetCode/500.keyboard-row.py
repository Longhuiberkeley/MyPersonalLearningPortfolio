#
# @lc app=leetcode id=500 lang=python3
#
# [500] Keyboard Row
#

# @lc code=start
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        return [word for word in words if all(c in "qwertyuiop"  for c in word.lower()) or all(c in "asdfghjkl" for c in word.lower()) or all(c in "zxcvbnm"  for c in word.lower())]
        
# @lc code=end

