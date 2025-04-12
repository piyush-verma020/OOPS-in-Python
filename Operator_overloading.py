class Number:

    def __init__(self,n):
        self.n = n

    def __add__(self,num):
        return self.n + num.n
    
    def __sub__(self,num2):
        return self.n - num2.n
    
    def __mul__(self,mult):
        return self.n * mult.n
    
    def __truediv__(self,div):
        return self.n / div.n
    
    def __floordiv__(self,fdi):
        return self.n // fdi.n
    
n = Number(5)
m = Number(2)
print(n + m)
print(n - m)
print(n * m)
print(n / m)
print(n // m)

# or we could use :-

class Number:
    def __init__(self, n, m):
        self.n = n
        self.m = m

    def __add__(self, other):
        return self.n + other.n

    def __sub__(self, other):
        return self.n - other.n

    def __mul__(self, other):
        return self.n * other.n

    def __truediv__(self, other):
        return self.n / other.m   # Now we’re using .m on the right-hand side

n = Number(6, 3)
m = Number(2, 2)

print(n + m)   # 6 + 2 = 8
print(n - m)   # 6 - 2 = 4
print(n * m)   # 6 * 2 = 12
print(n / m)   # 6 / 2 = 3.0 → using m.m (which is 2)
