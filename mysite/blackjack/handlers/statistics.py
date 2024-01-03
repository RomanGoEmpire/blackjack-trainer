class Statistics:
    def __init__(self):
        self.total = 0
        self.correct = 0
        self.wrong = 0
        
    def update(self, is_correct):
        self.total += 1
        if is_correct:
            self.correct += 1
        else:
            self.wrong += 1
        