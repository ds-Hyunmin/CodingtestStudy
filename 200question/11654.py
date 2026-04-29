n = input()

sign = '0123456789'
sign1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
sign2 = sign1.lower()

if n in sign:print(sign.find(n)+48)
elif n in sign1:print(sign1.find(n)+65)
else:print(sign2.find(n)+97)