class Solution:
    def countDigits(self, num: int) -> int:
        str_num = str(num)
        output = 0

        for number in str_num:
            if num % int(number) == 0:
                output += 1
        return output