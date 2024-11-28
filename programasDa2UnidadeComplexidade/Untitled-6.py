class AFN1:
    def __init__(self):
        self.state = 'q0'

    def transition(self, char):
        if self.state == 'q0':
            if char == 'a':
                self.state = 'q1'
        elif self.state == 'q1':
            if char == 'b':
                self.state = 'q2'

    def is_accepted(self):
        return self.state == 'q2'

    def test(self, input_string):
        self.state = 'q0'
        for char in input_string:
            self.transition(char)
        return self.is_accepted()

# Testes
afn1 = AFN1()
test_cases = ["ab", "aab", "bba", "bb", "aaab"]
print({case: afn1.test(case) for case in test_cases})
