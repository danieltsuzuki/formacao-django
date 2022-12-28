# Generated by Django 4.1.4 on 2022-12-27 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_pedido'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=500)),
                ('descricao', models.CharField(max_length=100)),
                ('valor', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='produtos',
            field=models.ManyToManyField(to='clientes.produto'),
        ),
    ]