def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn

    return n

class fraction:

    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        divisor = gcd(newnum, newden)

        return fraction(newnum//divisor, newden//divisor)

    def __sub__(self, otherfraction):
        newnum = self.num * otherfraction.den - self.den * otherfraction.num
        newden = self.den * otherfraction.den
        divisor = gcd(newnum, newden)

        return fraction(newnum//divisor, newden//divisor)

    def __mul__(self, otherfraction):
        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den
        divisor = gcd(newnum, newden)

        return fraction(newnum//divisor, newden//divisor)

    def __truediv__(self, otherfraction):
        newnum = self.num * otherfraction.den
        newden = self.den * otherfraction.num
        divisor = gcd(newnum, newden)

        return fraction(newnum//divisor, newden//divisor)

    def __eq__(self,other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num

        return firstnum == secondnum

    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num

        return firstnum < secondnum

    def __gt__(self, other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num

        return firstnum > secondnum

def main():
    f = fraction(3,9)
    g = fraction(4,8)

    print(f+g)
    print(f-g)
    print(f*g)
    print(f/g)
    print(f<g)
    print(f>g)
    print(f==g)

main()
    
