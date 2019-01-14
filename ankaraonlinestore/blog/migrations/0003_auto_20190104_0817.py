# Generated by Django 2.1.4 on 2019-01-04 07:17

from django.db import migrations


class Migration(migrations.Migration):

    atomic = False

    dependencies = [
        ('blog', '0002_auto_20181231_1820'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Tag',
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-published_date']},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ('name',), 'verbose_name': 'Tag', 'verbose_name_plural': 'Tags'},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='category',
            new_name='tag',
        ),
    ]
