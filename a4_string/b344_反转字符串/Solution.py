class Solution:
    def reverseString(self, s: list[str]) -> None:
        # 用list模仿栈
        stack = []
        for char in s:
            stack.append(char)
        for i in range(len(s)):
            s[i] = stack.pop()