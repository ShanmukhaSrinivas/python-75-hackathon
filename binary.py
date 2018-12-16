#binary

n, m =[int(i) for i in input().split()]
bin_n, bin_m = format(n,'#b'), format(m, '#b')
print(bin_n, bin_m)
n, m = int(bin_m, 2), int(bin_m, 2)
print(n, m)
# if 0b not needed replace # with 0
_or = n | m
_and = n & m
_one = ~ m
_one1 = ~ n
_xor = n ^ m
print("OR", _or, "AND", _and, "ONES COMPLIMENT", _one, _one1,'XOR', _xor, sep='\n')