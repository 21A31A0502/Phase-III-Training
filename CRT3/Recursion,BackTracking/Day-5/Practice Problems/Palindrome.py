def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0]==s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False

string =input()
print(is_palindrome(string))  

