s = 'abcbb'
charset = set()
res = 0
left = 0
for right in range(len(s)):
    if s[right] in charset:
        charset.remove(s[left])
        left += 1
    charset.add(s[right])
    res = max(res, len(charset))

print(res)
