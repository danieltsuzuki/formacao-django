# Generated by Django 4.1.4 on 2022-12-25 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_endereco'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='endereco',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clientes.endereco'),
        ),
    ]
