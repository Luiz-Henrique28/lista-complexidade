def afd_diferenca_multiplo_3(s):
    diferenca = 0
    for char in s:
        if char == 'a':
            diferenca += 1
        elif char == 'b':
            diferenca -= 1
    return diferenca % 3 == 0

# Testes
print(afd_diferenca_multiplo_3("aaabbb"))  # True
print(afd_diferenca_multiplo_3("aab"))    # False

  }
  }
