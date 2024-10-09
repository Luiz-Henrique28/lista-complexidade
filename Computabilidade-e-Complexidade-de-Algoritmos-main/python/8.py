def afn_zeros_div_3(s):
    count_zeros = s.count('0')
    return count_zeros % 3 == 0

# Testes
print(afn_zeros_div_3("000111"))  # True
print(afn_zeros_div_3("0011"))    # False
