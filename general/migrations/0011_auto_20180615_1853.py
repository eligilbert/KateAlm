# Generated by Django 2.0.4 on 2018-06-15 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0010_auto_20180615_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.CharField(choices=[('Not Applicable', 'Not Applicable'), ('Marketing', 'Marketing'), ('Tech', 'Tech'), ('Production', 'Production'), ('Customer Service', 'Customer Service'), ('Accounting', 'Accounting')], default='Not Applicable', max_length=50),
        ),
    ]
