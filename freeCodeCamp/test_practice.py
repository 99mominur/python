
import practice
a = 0
b = 0
sum, carry = practice.half_adder(a, b)
assert sum == 0 and carry == 0
a = 0
b = 1
sum, carry = practice.half_adder(a, b)
assert sum == 1 and carry == 0
a = 1
b = 0
sum, carry = practice.half_adder(a, b)
assert sum == 1 and carry == 0
a = 1
b = 1
sum, carry = practice.half_adder(a, b)
assert sum == 0 and carry == 1
