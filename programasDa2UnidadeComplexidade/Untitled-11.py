class AFN5:
    def __init__(self):
        self.state = 'q0'
        self.aa_count = 0

    def transition(self, char):
        if self.state == 'q0' and char == 'a':
            self.state = 'q1'
        elif self.state == 'q1' and char == 'a':
            self.state = 'q2'
            self.aa_count += 1
        elif self.state == 'q1' and char == 'b':
            self.state = 'q0'

    def is_accepted(self):
        return self.aa_count >= 2

    def test(self, input_string):
        self.state = 'q0'
        self.aa_count = 0
        for char in input_string:
            self.transition(char)
        return self.is_accepted()

# Testes
afn5 = AFN5()
test_cases = ["aaa", "bbaa", "abbbaa", "aa", "abab"]
print({case: afn5.test(case) for case in test_cases})
