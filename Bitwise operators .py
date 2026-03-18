## BITWISE OPERATORS :- these operators are applied after turning the decimal value to binary,
# operators are applied to each binary value(bit), then the ans is later converted to decimal..

# Bitwise "AND" operator(&) :- follows 'and gate' truth table for each bit
a = 5
b = 9
print(a & b)
x = 12
y = 6
print(x & y)

# Bitwise "OR" operator(|) :- follows 'or gate'  truth table for each bit
a = 10
b = 12
a_or_b = a | b
print(a_or_b)

# Bitwise Xor operator(^) :- same bits produce 0, whereas diff. bits produce 1
x = 5
y = 9
print(x^y)
a = 10
b = 20
c = a^b
print(c, ',', c^a)

# Complement Operator(~) :- [a~ = -(a+1), -(b)~ = b+1]
a = -2345
print(~a)

# Bitwise Left Shift operator(<<) :- shifting each bits of the binary value leftward, [a << n = a * 2^n]
x = 14
print(x << 2)

# Bitwise Right Shift(>>) :- shifting each bits of the binary value rightward [a >> n = a // 2^n]
x = 14
print(x >> 2)
