class AFN4:
    def __init__(self):
        self.state = 'q0'

    def transition(self, char):
        if self.state == 'q0' and char == 'a':
            self.state = 'q1'
        elif self.state == 'q1' and char == 'b':
            self.state = 'q2'
        elif self.state == 'q2' and char == 'a':
            self.state = 'q3'

    def is_accepted(self):
        return self.state == 'q3'

    def test(self, input_string):
        self.state = 'q0'
        for char in input_string:
            self.transition(char)
        return self.is_accepted()

# Testes
afn4 = AFN4()
test_cases = ["aba", "baba", "ababa", "abb", "baaaba"]
print({case: afn4.test(case) for case in test_cases})
