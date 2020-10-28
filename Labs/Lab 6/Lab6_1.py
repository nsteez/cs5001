# def gcd(a, b):
#     while a != 0 or b != 0:
#        q = a%b
#        t = b*q
#        r = a-t
#        a = b
#        b = r
#     return(a,b)

# print(gcd(270,192))

def gcd(a,b):
    while b!=0:
        (a,b)=(b, a%b)
    return a
print(gcd(192,78))

