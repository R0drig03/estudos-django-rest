# Generated by Django 5.1.2 on 2024-10-18 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sabores_pizzas',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name_sabor', models.CharField(choices=[('1', 'Calabresa'), ('2', '4 Queijos'), ('3', 'Frango Catupiry'), ('4', 'Bacon com Milho'), ('5', 'Baiana')], max_length=1)),
            ],
        ),
    ]
