# Generated by Django 4.2.7 on 2023-12-27 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_consubem', '0003_alter_produto_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='estado',
            field=models.CharField(choices=[('1', 'Novo'), ('2', 'Seminovo'), ('3', 'Desgastado')], default='1', max_length=80),
        ),
    ]