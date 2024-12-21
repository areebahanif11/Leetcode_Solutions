class Solution:
    def calculate(self, s: str) -> int:
        number = 0 
        result = 0 
        sign = 1 
        stack = []

        for value in s:
            if '0' <= value <= '9':
                number = number * 10 + int(value)
            elif value == '+':
                result += (number * sign)
                sign = 1
                number = 0
            elif value == '-':
                result += (number * sign )
                sign = -1
                number = 0
            elif value == '(':
                stack.append(result)
                stack.append(sign)
                number = 0
                result = 0
                sign = 1
            elif value == ')':
                result += (number * sign )
                number = 0
                result *= stack.pop()
                result += stack.pop()
    
        result += (number * sign)

        return result 




        