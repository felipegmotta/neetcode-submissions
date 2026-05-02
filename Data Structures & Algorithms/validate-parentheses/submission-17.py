class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        for char in s:
            if len(stack) == 0:
                stack.append(char)
                continue

            print(char)
            print(stack)
            print(stack[-1])

            if char in [")", "]", "}"]:
                if ((char == ")" and stack[-1] != "(") or
                    (char == "]" and stack[-1] != "[") or
                    (char == "}" and stack[-1] != "{")):
                    return False

                stack.pop()
                continue

            stack.append(char)
        
        return len(stack) == 0
