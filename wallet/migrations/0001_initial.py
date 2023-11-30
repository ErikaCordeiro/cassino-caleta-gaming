# Generated by Django 4.2.7 on 2023-11-29 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('player_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transaction_type', models.CharField(choices=[('bet', 'Bet'), ('win', 'Win'), ('deposit', 'Deposit'), ('rollback', 'Rollback')], max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.player')),
            ],
        ),
    ]