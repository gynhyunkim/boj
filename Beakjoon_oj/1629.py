#곱셈
import sys

base, index, mod = map(int, sys.stdin.readline().split())

def powmod(base, index, mod):
	if index == 1:
		return base
	if index % 2 == 0:
		r = powmod(base, index // 2, mod)
		return (r * r) % mod
	else:
		return (base * powmod(base, index - 1, mod)) % mod

if index == 1:
	print(base % mod)
else: 
	print(powmod(base, index, mod))
