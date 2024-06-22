class Solution:
    def search(self, pat, txt):
        result = []
        n, m = len(txt), len(pat)
        lps = [0] * m
        
        # step-1 (Construct LPS array)
        mainIndex, patIndex = 1, 0 
        while mainIndex < m:
            if pat[mainIndex] == pat[patIndex]:
                lps[mainIndex] = patIndex + 1 
                mainIndex += 1 
                patIndex += 1 
            else:
                if patIndex > 0:
                    patIndex = lps[patIndex - 1]
                else:
                    mainIndex += 1 
        
        # step-2 (start comparing)
        patIndex, txtIndex = 0, 0 
        while txtIndex < n:
            if pat[patIndex] == txt[txtIndex]:
                txtIndex += 1 
                patIndex += 1 
                if patIndex == m:
                    result.append(txtIndex - m + 1)
                    patIndex = lps[patIndex - 1]
            else:
                if patIndex > 0:
                    patIndex = lps[patIndex - 1]
                else:
                    txtIndex += 1 
                
        return result

# Example usage:
solution = Solution()
pattern = "ABABCABAB"
text = "ABABDABACDABABCABAB"
print(solution.search(pattern, text))  # Output: [10]
