from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words: 
            return []
        
        n = len(words[0])
        m = len(words)
        ans = []
        target = Counter(words)
        
        for i in range(n):
            left = i
            right = i
            seen = Counter()
            count = 0
            
            while right + n <= len(s):
                word = s[right : right + n]
                right += n
                
                if word in target:
                    seen[word] += 1
                    count += 1
                    
                    while seen[word] > target[word]:
                        seen[s[left : left + n]] -= 1
                        count -= 1
                        left += n
                        
                    if count == m:
                        ans.append(left)
                else:
                    seen.clear()
                    count = 0
                    left = right
        return ans
