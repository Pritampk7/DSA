class ReverseInt:
    def reverse(self, s: int) -> int:
        res = 0
        while s > 0:
            digit = int(s % 10)
            s = int(s // 10)
            res = (res * 10) + digit
        return res


obj = ReverseInt()
print(obj.reverse(s=123))
