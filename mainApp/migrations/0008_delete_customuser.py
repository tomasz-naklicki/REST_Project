# Generated by Django 4.1.7 on 2023-04-02 23:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("mainApp", "0007_remove_pokemon_move1_remove_pokemon_move2_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="CustomUser",
        ),
    ]
