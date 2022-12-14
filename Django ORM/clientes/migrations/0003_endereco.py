# Generated by Django 4.1.4 on 2022-12-25 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_rename_professiao_cliente_profissao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=200)),
                ('numero', models.IntegerField()),
                ('complemento', models.CharField(max_length=200)),
                ('bairro', models.CharField(choices=[('N', 'Planto diretor norte'), ('S', 'Plano diretor sul'), ('T', 'Taquaralto')], max_length=1)),
                ('cidade', models.CharField(choices=[('P', 'Palmas')], max_length=1)),
                ('pais', models.CharField(choices=[('B', 'Brasil')], max_length=1)),
            ],
        ),
    ]
