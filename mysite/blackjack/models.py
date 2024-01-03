from django.db import models

OPTIONS = (
    ("Hit", "Hit"), 
    ("Stand", "Stand"), 
    ("Double", "Double"), 
    ("Split", "Split"), 
    ("No Split", "No Split"),
    ("Surrender", "Surrender"),
)

MODES = (
    ("Practice", "Practice"),
    ("Iterative", "Iterative"),
    ("Endurance", "Endurance"),
    ("Hard", "Hard"),
    ("Soft", "Soft"),
    ("Split", "Split"),
)

class Card(models.Model):
    suit = models.CharField(max_length=10)
    value = models.CharField(max_length=10)
    def __str__(self):
        return self.value + " of " + self.suit
    
    def get_value(self):
        if self.value == "Ace":
            return 11
        elif self.value == "Jack" or self.value == "Queen" or self.value == "King":
            return 10
        else:
            return int(self.value)
        
class Session(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    mode = models.CharField(max_length=10, choices=MODES)
    
    def __str__(self):
        return f'{self.date} - {self.mode}'
    
class HandHistory(models.Model):
    session = models.ForeignKey(Session, related_name='session', on_delete=models.CASCADE)
    hand = models.ManyToManyField(Card, related_name='hand')
    date = models.DateTimeField(auto_now_add=True)
    decision = models.CharField(max_length=10, choices=OPTIONS)
    correct_decision = models.CharField(max_length=10, choices=OPTIONS)
    was_correct = models.BooleanField()
    bucket = models.IntegerField(null=True, blank=True) # only used for iterative mode
    
    def __str__(self):
        return f'Hand: {self.hand}, Was Correct: {self.was_correct}, Mode: {self.mode}'