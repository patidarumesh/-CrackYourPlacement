def addBinary( a: str, b: str) -> str:
        sum = bin(int(a, 2) + int(b, 2))
        return sum[2:]

a = '1001'
b = '1100'
print(addBinary(a,b))