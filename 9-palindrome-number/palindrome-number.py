class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        list_x = list(str_x)
        
        rev_list = list_x.copy()
        list_x.reverse()

        if list_x == rev_list:
            return True
        else:
            return False
        