def reverse_string(s):
    if len(s) == 0:
        return ""
    else:
        return s[-1] + reverse_string(s[:-1]) # s[:1] - all elements except the last element

reversed_str = reverse_string('vijay')
print(reversed_str)


def fibonaci(n):
    if n <= 1:
        return n
    else:
        return fibonaci(n-1) + fibonaci(n-2)
    
print(fibonaci(10))


def fibonaci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonaci_memo(n-1, memo) + fibonaci_memo(n-2, memo)
    return memo[n]

print(fibonaci_memo(10))