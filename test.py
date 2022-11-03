x = 123
res = 0
while x > 0:
    mod = x % 10
    x = x // 10
    res = (res * 10) + mod

print(res)
