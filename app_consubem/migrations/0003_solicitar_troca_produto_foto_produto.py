# Generated by Django 4.2.7 on 2023-11-26 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_consubem', '0002_produto'),
    ]

    operations = [
        migrations.CreateModel(
            name='solicitar_troca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.TextField(max_length=255)),
                ('data_solicitacao', models.DateField()),
                ('hora_solicitacao', models.TimeField()),
            ],
        ),
        migrations.AddField(
            model_name='produto',
            name='foto_produto',
            field=models.ImageField(default='fotos_produto/logo.svg', upload_to='fotos_produto'),
            preserve_default=False,
        ),
    ]