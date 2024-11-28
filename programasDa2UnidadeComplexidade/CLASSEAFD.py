class AFD:
    def __init__(self):
        self.state = 'q0'

    def transition(self, symbol):
        if self.state == 'q0':
            self.state = 'q1' if symbol == 'a' else 'q0'
        elif self.state == 'q1':
            self.state = 'q2' if symbol == 'a' else 'q1'
        elif self.state == 'q2':
            self.state = 'q3' if symbol == 'a' else 'q2'
        else:
            self.state = 'q3'

    def is_accepted(self):
        return self.state == 'q2'

# Testando o AFD com algumas entradas
afd = AFD()
test_cases = ['ab', 'aab', 'ba', 'aa', 'aaa']
for case in test_cases:
    afd.state = 'q0'  # Reinicia o AFD para cada teste
    for symbol in case:
        afd.transition(symbol)
    print(f'Entrada "{case}" aceita: {afd.is_accepted()}')
