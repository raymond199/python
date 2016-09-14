def is_palindrome(n):
    num=list(str(n))
    mun=num[::-1]
    print(n)
    
output = filter(is_palindrome, range(1, 1000))
print(list(output))
