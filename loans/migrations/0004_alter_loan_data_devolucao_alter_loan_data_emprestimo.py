# Generated by Django 4.2.3 on 2023-07-06 19:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0003_alter_loan_data_devolucao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='data_devolucao',
            field=models.DateField(default=datetime.datetime(2023, 7, 13, 19, 27, 40, 511637, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='loan',
            name='data_emprestimo',
            field=models.DateField(auto_now_add=True),
        ),
    ]
