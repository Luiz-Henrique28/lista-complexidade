class AFD_par_de_a:
    def __init__(self):
        self.state = 'q0'

    def transition(self, symbol):
        if self.state == 'q0':
            self.state = 'q1' if symbol == 'a' else 'q0'
        elif self.state == 'q1':
            self.state = 'q0' if symbol == 'a' else 'q1'

    def is_accepted(self):
        return self.state == 'q0'

# Testando o AFD
afd_par_a = AFD_par_de_a()
test_cases = ['a', 'aa', 'aba', 'ba']
for case in test_cases:
    afd_par_a.state = 'q0'
    for symbol in case:
        afd_par_a.transition(symbol)
    print(f'Entrada "{case}" aceita: {afd_par_a.is_accepted()}')
