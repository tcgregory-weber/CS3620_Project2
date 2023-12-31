# Generated by Django 4.1.9 on 2023-07-11 19:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mad_libs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='madlib',
            old_name='text',
            new_name='story',
        ),
        migrations.AddField(
            model_name='madlib',
            name='word_types',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='MadLibsPrompt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prompt', models.TextField()),
                ('mad_lib', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mad_libs.madlib')),
            ],
        ),
    ]
