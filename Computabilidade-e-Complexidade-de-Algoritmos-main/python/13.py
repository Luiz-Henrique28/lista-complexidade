def afd_mais_uns(s):
    count_1 = s.count('1')
    count_0 = s.count('0')
    return count_1 > count_0

# Testes
print(afd_mais_uns("110"))    # True
print(afd_mais_uns("10100"))  # False
