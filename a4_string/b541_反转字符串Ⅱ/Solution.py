class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i = 0
        chars = list(s)
        
        while i < len(chars):
            # 反转后，更改原值为反转后值
            chars[i:i + k] = chars[i:i + k][::-1] 
            i += k * 2

        return ''.join(chars)