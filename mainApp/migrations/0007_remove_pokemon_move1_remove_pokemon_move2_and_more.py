# Generated by Django 4.1.7 on 2023-04-02 20:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mainApp", "0006_move_pokemon_move1_pokemon_move2_pokemon_move3_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pokemon",
            name="move1",
        ),
        migrations.RemoveField(
            model_name="pokemon",
            name="move2",
        ),
        migrations.RemoveField(
            model_name="pokemon",
            name="move3",
        ),
        migrations.RemoveField(
            model_name="pokemon",
            name="move4",
        ),
        migrations.AddField(
            model_name="pokemon",
            name="moves",
            field=models.ManyToManyField(to="mainApp.move"),
        ),
    ]
