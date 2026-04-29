# 분수 합
import sys, fractions
input = sys.stdin.readline
a, b = map(int, input().split())
c, d = map(int, input().split())
frac = fractions.Fraction(a*d+c*b, b*d)
print(frac.numerator, frac.denominator)