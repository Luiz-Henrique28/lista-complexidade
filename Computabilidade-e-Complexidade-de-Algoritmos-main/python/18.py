def afd_impar_zeros_uns(s):
    count_0 = s.count('0')
    count_1 = s.count('1')
    return count_0 % 2 != 0 and count_1 % 2 != 0

# Testes
print(afd_impar_zeros_uns("101"))   # True
print(afd_impar_zeros_uns("1100"))  # False
