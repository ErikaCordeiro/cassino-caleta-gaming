from django.db import models

class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
def __str__(self):
    return self.username

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('bet', 'Bet'),
        ('win', 'Win'),
        ('deposit', 'Deposit'),
        ('rollback', 'Rollback'),
    )

    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    timestamp = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return f"{self.transaction_type} - {self.value} by {self.player.username}"

